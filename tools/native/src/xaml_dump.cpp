#include "common.h"
#include <tlhelp32.h>
#include <iostream>
#include <string>
#include <vector>
#include <memory>
#include <algorithm>
#include <sstream>
#include <fstream>
#include <map>

// Target process info
struct ProcessInfo {
    DWORD pid;
    std::wstring name;
    bool isApproved;
};

// Find running approved processes
static std::vector<ProcessInfo> GetRunningProcesses() {
    std::vector<ProcessInfo> list;
    HANDLE snapshot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);
    if (snapshot == INVALID_HANDLE_VALUE) return list;

    PROCESSENTRY32W entry;
    entry.dwSize = sizeof(entry);

    if (Process32FirstW(snapshot, &entry)) {
        do {
            std::wstring name = entry.szExeFile;
            if (IsApprovedProcess(name)) {
                list.push_back({ entry.th32ProcessID, name, true });
            }
        } while (Process32NextW(snapshot, &entry));
    }

    CloseHandle(snapshot);
    return list;
}

// Find process by PID or name
static DWORD ResolveProcess(const std::wstring& target, std::wstring& outName) {
    bool isNum = !target.empty() && std::all_of(target.begin(), target.end(), ::iswdigit);
    if (isNum) {
        DWORD pid = std::stoul(target);
        HANDLE snapshot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);
        if (snapshot != INVALID_HANDLE_VALUE) {
            PROCESSENTRY32W entry;
            entry.dwSize = sizeof(entry);
            if (Process32FirstW(snapshot, &entry)) {
                do {
                    if (entry.th32ProcessID == pid) {
                        outName = entry.szExeFile;
                        CloseHandle(snapshot);
                        return pid;
                    }
                } while (Process32NextW(snapshot, &entry));
            }
            CloseHandle(snapshot);
        }
        return pid;
    }

    auto procs = GetRunningProcesses();
    for (const auto& p : procs) {
        if (_wcsicmp(p.name.c_str(), target.c_str()) == 0) {
            outName = p.name;
            return p.pid;
        }
    }

    std::wstring withExe = target + L".exe";
    for (const auto& p : procs) {
        if (_wcsicmp(p.name.c_str(), withExe.c_str()) == 0) {
            outName = p.name;
            return p.pid;
        }
    }

    return 0;
}

static std::wstring GetExecutableDir() {
    WCHAR path[MAX_PATH];
    GetModuleFileNameW(nullptr, path, MAX_PATH);
    std::wstring s = path;
    size_t pos = s.find_last_of(L"\\/");
    return (pos != std::wstring::npos) ? s.substr(0, pos) : L"";
}

static bool CreateAppContainerSecurityAttributes(SECURITY_ATTRIBUTES& sa) {
    ZeroMemory(&sa, sizeof(sa));
    sa.nLength = sizeof(sa);
    sa.bInheritHandle = FALSE;

    return ConvertStringSecurityDescriptorToSecurityDescriptorW(
        L"D:(A;;GA;;;WD)(A;;GA;;;AC)",
        SDDL_REVISION_1,
        &sa.lpSecurityDescriptor,
        nullptr
    ) != FALSE;
}

// UI Automation Helper: Sends keyboard chord to open shell surfaces
static void SendKeyChord(const std::vector<WORD>& keys) {
    std::vector<INPUT> inputs;
    inputs.reserve(keys.size() * 2);

    for (WORD k : keys) {
        INPUT inp = {};
        inp.type = INPUT_KEYBOARD;
        inp.ki.wVk = k;
        inputs.push_back(inp);
    }

    for (auto it = keys.rbegin(); it != keys.rend(); ++it) {
        INPUT inp = {};
        inp.type = INPUT_KEYBOARD;
        inp.ki.wVk = *it;
        inp.ki.dwFlags = KEYEVENTF_KEYUP;
        inputs.push_back(inp);
    }

    SendInput((UINT)inputs.size(), inputs.data(), sizeof(INPUT));
}

static void OpenSurface(const std::wstring& surface) {
    if (surface == L"start") {
        std::wcout << L"[UI-AUTOMATION] Opening Start Menu (Win)... Please do not touch your mouse/keyboard.\n";
        SendKeyChord({ VK_LWIN });
    } else if (surface == L"action-center" || surface == L"quick-settings") {
        std::wcout << L"[UI-AUTOMATION] Opening Quick Settings / Action Center (Win+A)... Please wait.\n";
        SendKeyChord({ VK_LWIN, 'A' });
    } else if (surface == L"notification-center" || surface == L"calendar") {
        std::wcout << L"[UI-AUTOMATION] Opening Notification Center / Calendar (Win+N)... Please wait.\n";
        SendKeyChord({ VK_LWIN, 'N' });
    } else if (surface == L"search") {
        std::wcout << L"[UI-AUTOMATION] Opening Search (Win+S)... Please wait.\n";
        SendKeyChord({ VK_LWIN, 'S' });
    } else if (surface == L"settings") {
        std::wcout << L"[UI-AUTOMATION] Opening Windows Settings (Win+I)... Please wait.\n";
        SendKeyChord({ VK_LWIN, 'I' });
    }
    Sleep(1200); // Allow window to create and render XAML visual tree
}

static void CloseSurface() {
    INPUT inps[2] = {};
    inps[0].type = INPUT_KEYBOARD;
    inps[0].ki.wVk = VK_ESCAPE;
    inps[1].type = INPUT_KEYBOARD;
    inps[1].ki.wVk = VK_ESCAPE;
    inps[1].ki.dwFlags = KEYEVENTF_KEYUP;
    SendInput(2, inps, sizeof(INPUT));
    Sleep(300);
}

struct JsonElement {
    std::string handle;
    std::string parent;
    unsigned int childIndex = 0;
    std::string type;
    std::string name;
    unsigned int numChildren = 0;
};

static std::vector<JsonElement> ParseElements(const std::string& json) {
    std::vector<JsonElement> elements;
    size_t pos = json.find("\"elements\":");
    if (pos == std::string::npos) return elements;

    size_t arrayStart = json.find('[', pos);
    if (arrayStart == std::string::npos) return elements;

    size_t curr = arrayStart + 1;
    while (curr < json.size()) {
        size_t objStart = json.find('{', curr);
        if (objStart == std::string::npos) break;
        size_t objEnd = json.find('}', objStart);
        if (objEnd == std::string::npos) break;

        std::string obj = json.substr(objStart, objEnd - objStart + 1);
        JsonElement el;

        auto extractStr = [&](const std::string& key) -> std::string {
            size_t kpos = obj.find("\"" + key + "\":");
            if (kpos == std::string::npos) return "";
            size_t vstart = obj.find('"', kpos + key.size() + 3);
            if (vstart == std::string::npos) return "";
            size_t vend = obj.find('"', vstart + 1);
            if (vend == std::string::npos) return "";
            return obj.substr(vstart + 1, vend - vstart - 1);
        };

        auto extractNum = [&](const std::string& key) -> unsigned int {
            size_t kpos = obj.find("\"" + key + "\":");
            if (kpos == std::string::npos) return 0;
            size_t numStart = kpos + key.size() + 3;
            while (numStart < obj.size() && (obj[numStart] == ' ' || obj[numStart] == ':')) numStart++;
            return std::strtoul(&obj[numStart], nullptr, 10);
        };

        el.handle = extractStr("handle");
        el.parent = extractStr("parent");
        el.type = extractStr("type");
        el.name = extractStr("name");
        el.childIndex = extractNum("childIndex");
        el.numChildren = extractNum("numChildren");

        elements.push_back(std::move(el));
        curr = objEnd + 1;
    }

    return elements;
}

struct TreeNode {
    JsonElement element;
    std::vector<std::shared_ptr<TreeNode>> children;
};

static std::vector<std::shared_ptr<TreeNode>> BuildTree(const std::vector<JsonElement>& elements) {
    std::map<std::string, std::shared_ptr<TreeNode>> nodeMap;
    std::vector<std::shared_ptr<TreeNode>> roots;

    for (const auto& el : elements) {
        auto node = std::make_shared<TreeNode>();
        node->element = el;
        nodeMap[el.handle] = node;
    }

    for (const auto& el : elements) {
        auto node = nodeMap[el.handle];
        if (el.parent.empty() || el.parent == "0x0" || nodeMap.find(el.parent) == nodeMap.end()) {
            roots.push_back(node);
        } else {
            nodeMap[el.parent]->children.push_back(node);
        }
    }

    return roots;
}

static bool MatchesFilter(const JsonElement& el, const std::string& filter) {
    if (filter.empty()) return true;
    auto toLower = [](std::string s) {
        std::transform(s.begin(), s.end(), s.begin(), ::tolower);
        return s;
    };
    std::string fLow = toLower(filter);
    return toLower(el.name).find(fLow) != std::string::npos ||
           toLower(el.type).find(fLow) != std::string::npos;
}

static bool SubtreeMatches(const std::shared_ptr<TreeNode>& node, const std::string& filter) {
    if (filter.empty()) return true;
    if (MatchesFilter(node->element, filter)) return true;
    for (const auto& c : node->children) {
        if (SubtreeMatches(c, filter)) return true;
    }
    return false;
}

static void PrintTextTree(const std::shared_ptr<TreeNode>& node, int depth, int maxDepth, const std::string& filter, std::ostream& out) {
    if (maxDepth >= 0 && depth > maxDepth) return;
    if (!filter.empty() && !SubtreeMatches(node, filter)) return;

    for (int i = 0; i < depth; ++i) out << "  ";

    out << node->element.type;
    if (!node->element.name.empty()) {
        out << " [#" << node->element.name << "]";
    }
    out << "\n";

    for (const auto& c : node->children) {
        PrintTextTree(c, depth + 1, maxDepth, filter, out);
    }
}

static void PrintMarkdownTree(const std::shared_ptr<TreeNode>& node, int depth, int maxDepth, const std::string& filter, std::ostream& out) {
    if (maxDepth >= 0 && depth > maxDepth) return;
    if (!filter.empty() && !SubtreeMatches(node, filter)) return;

    for (int i = 0; i < depth; ++i) out << "  ";
    out << "- `" << node->element.type << "`";
    if (!node->element.name.empty()) {
        out << " (**#" << node->element.name << "**)";
    }
    out << "\n";

    for (const auto& c : node->children) {
        PrintMarkdownTree(c, depth + 1, maxDepth, filter, out);
    }
}

static void PrintHelp() {
    std::wcout << L"Windhawk Command Center Suite - Native Hybrid XAML Inspector\n\n"
               << L"Usage:\n"
               << L"  xaml_dump.exe [options]\n\n"
               << L"Options:\n"
               << L"  -p, --process <name|pid>  Target process name or PID (e.g. StartMenuExperienceHost.exe)\n"
               << L"  -s, --surface <name>      Auto-open surface with UI automation (start, action-center, notification-center, search)\n"
               << L"  -l, --list                List active approved shell processes\n"
               << L"  -f, --filter <text>       Filter elements by Name or Type (case-insensitive)\n"
               << L"  -d, --depth <n>           Maximum visual tree depth to display\n"
               << L"  --leave-open              Keep opened surface visible after inspection (default: closes with Escape)\n"
               << L"  --format <text|json|md>   Output format (default: text)\n"
               << L"  -o, --output <file>       Write output to file instead of stdout\n"
               << L"  -h, --help                Show this help message\n";
}

static void EnsureAgentUnloaded(DWORD pid) {
    HANDLE snap = CreateToolhelp32Snapshot(TH32CS_SNAPMODULE | TH32CS_SNAPMODULE32, pid);
    if (snap != INVALID_HANDLE_VALUE) {
        MODULEENTRY32W me = { sizeof(me) };
        if (Module32FirstW(snap, &me)) {
            do {
                if (wcsstr(me.szModule, L"xaml_dump_agent")) {
                    HANDLE hProc = OpenProcess(PROCESS_CREATE_THREAD | PROCESS_VM_OPERATION | PROCESS_QUERY_INFORMATION, FALSE, pid);
                    if (hProc) {
                        LPTHREAD_START_ROUTINE pfnFree = (LPTHREAD_START_ROUTINE)GetProcAddress(GetModuleHandleW(L"kernel32.dll"), "FreeLibrary");
                        HANDLE hEject = CreateRemoteThread(hProc, nullptr, 0, pfnFree, me.modBaseAddr, 0, nullptr);
                        if (hEject) {
                            WaitForSingleObject(hEject, 500);
                            CloseHandle(hEject);
                        }
                        CloseHandle(hProc);
                    }
                }
            } while (Module32NextW(snap, &me));
        }
        CloseHandle(snap);
    }
}

int wmain(int argc, wchar_t* argv[]) {
    std::wstring targetProcess = L"StartMenuExperienceHost.exe";
    std::wstring surface = L"";
    std::wstring filter = L"";
    int maxDepth = -1;
    std::wstring format = L"text";
    std::wstring outputFile = L"";
    bool doList = false;
    bool leaveOpen = false;

    for (int i = 1; i < argc; ++i) {
        std::wstring arg = argv[i];
        if (arg == L"-h" || arg == L"--help") {
            PrintHelp();
            return 0;
        } else if (arg == L"-l" || arg == L"--list") {
            doList = true;
        } else if ((arg == L"-p" || arg == L"--process") && i + 1 < argc) {
            targetProcess = argv[++i];
        } else if ((arg == L"-s" || arg == L"--surface") && i + 1 < argc) {
            surface = argv[++i];
        } else if ((arg == L"-f" || arg == L"--filter") && i + 1 < argc) {
            filter = argv[++i];
        } else if ((arg == L"-d" || arg == L"--depth") && i + 1 < argc) {
            maxDepth = std::stoi(argv[++i]);
        } else if (arg == L"--format" && i + 1 < argc) {
            format = argv[++i];
        } else if ((arg == L"-o" || arg == L"--output") && i + 1 < argc) {
            outputFile = argv[++i];
        } else if (arg == L"--leave-open") {
            leaveOpen = true;
        }
    }

    if (doList) {
        auto list = GetRunningProcesses();
        std::wcout << L"Active Approved Shell Processes:\n";
        std::wcout << L"-----------------------------------------\n";
        for (const auto& p : list) {
            std::wcout << L"  PID: " << p.pid << L"\t" << p.name << L"\n";
        }
        return 0;
    }

    // Auto-map surface if not explicitly given
    if (surface.empty()) {
        if (_wcsicmp(targetProcess.c_str(), L"StartMenuExperienceHost.exe") == 0 ||
            _wcsicmp(targetProcess.c_str(), L"StartMenuExperienceHost") == 0) {
            surface = L"start";
        } else if (_wcsicmp(targetProcess.c_str(), L"SearchHost.exe") == 0 ||
                   _wcsicmp(targetProcess.c_str(), L"SearchHost") == 0) {
            surface = L"search";
        } else if (_wcsicmp(targetProcess.c_str(), L"SystemSettings.exe") == 0 ||
                   _wcsicmp(targetProcess.c_str(), L"SystemSettings") == 0) {
            surface = L"settings";
        }
    }

    // UI Automation: Open surface if specified
    bool surfaceOpened = false;
    if (!surface.empty()) {
        OpenSurface(surface);
        surfaceOpened = true;
    }

    std::wstring resolvedName;
    DWORD pid = ResolveProcess(targetProcess, resolvedName);
    if (!pid) {
        std::wcerr << L"[ERROR] Target process '" << targetProcess << L"' is not running.\n";
        if (surfaceOpened && !leaveOpen) CloseSurface();
        return 1;
    }

    if (!IsApprovedProcess(resolvedName)) {
        std::wcerr << L"[ERROR] Process '" << resolvedName << L"' is NOT an approved target per Rule 01.\n";
        if (surfaceOpened && !leaveOpen) CloseSurface();
        return 1;
    }

    std::wstring exeDir = GetExecutableDir();
    std::wstring agentDllPath = exeDir + L"\\xaml_dump_agent.dll";

    if (GetFileAttributesW(agentDllPath.c_str()) == INVALID_FILE_ATTRIBUTES) {
        std::wcerr << L"[ERROR] Agent DLL not found at: " << agentDllPath << L"\n";
        if (surfaceOpened && !leaveOpen) CloseSurface();
        return 1;
    }

    EnsureAgentUnloaded(pid);

    std::wstring pipeName = std::wstring(XAML_DUMP_PIPE_PREFIX) + std::to_wstring(pid);
    SECURITY_ATTRIBUTES sa;
    if (!CreateAppContainerSecurityAttributes(sa)) {
        std::wcerr << L"[ERROR] Failed to create security descriptor for named pipe.\n";
        if (surfaceOpened && !leaveOpen) CloseSurface();
        return 1;
    }

    HANDLE hPipe = CreateNamedPipeW(
        pipeName.c_str(),
        PIPE_ACCESS_INBOUND | FILE_FLAG_OVERLAPPED,
        PIPE_TYPE_BYTE | PIPE_WAIT,
        1,
        512 * 1024,
        512 * 1024,
        45000,
        &sa
    );

    if (sa.lpSecurityDescriptor) {
        LocalFree(sa.lpSecurityDescriptor);
    }

    if (hPipe == INVALID_HANDLE_VALUE) {
        std::wcerr << L"[ERROR] Failed to create named pipe. Error: " << GetLastError() << L"\n";
        if (surfaceOpened && !leaveOpen) CloseSurface();
        return 1;
    }

    HANDLE hProcess = OpenProcess(
        PROCESS_CREATE_THREAD | PROCESS_QUERY_INFORMATION | PROCESS_VM_OPERATION | PROCESS_VM_WRITE | PROCESS_VM_READ | PROCESS_SUSPEND_RESUME,
        FALSE,
        pid
    );

    if (!hProcess) {
        hProcess = OpenProcess(
            PROCESS_CREATE_THREAD | PROCESS_QUERY_INFORMATION | PROCESS_VM_OPERATION | PROCESS_VM_WRITE | PROCESS_VM_READ,
            FALSE,
            pid
        );
    }

    if (!hProcess) {
        std::wcerr << L"[ERROR] Failed to open process " << pid << L" (" << resolvedName << L"). Error: " << GetLastError() << L"\n";
        CloseHandle(hPipe);
        if (surfaceOpened && !leaveOpen) CloseSurface();
        return 1;
    }

    typedef LONG (NTAPI *pfnNtResumeProcess)(HANDLE);
    auto pNtResume = (pfnNtResumeProcess)GetProcAddress(GetModuleHandleW(L"ntdll.dll"), "NtResumeProcess");
    if (pNtResume) {
        pNtResume(hProcess);
    }

    size_t pathBytes = (agentDllPath.size() + 1) * sizeof(wchar_t);
    LPVOID remoteMem = VirtualAllocEx(hProcess, nullptr, pathBytes, MEM_COMMIT | MEM_RESERVE, PAGE_READWRITE);
    if (!remoteMem) {
        std::wcerr << L"[ERROR] VirtualAllocEx failed. Error: " << GetLastError() << L"\n";
        CloseHandle(hProcess);
        CloseHandle(hPipe);
        if (surfaceOpened && !leaveOpen) CloseSurface();
        return 1;
    }

    if (!WriteProcessMemory(hProcess, remoteMem, agentDllPath.c_str(), pathBytes, nullptr)) {
        std::wcerr << L"[ERROR] WriteProcessMemory failed. Error: " << GetLastError() << L"\n";
        VirtualFreeEx(hProcess, remoteMem, 0, MEM_RELEASE);
        CloseHandle(hProcess);
        CloseHandle(hPipe);
        if (surfaceOpened && !leaveOpen) CloseSurface();
        return 1;
    }

    OVERLAPPED ov = { 0 };
    ov.hEvent = CreateEventW(nullptr, TRUE, FALSE, nullptr);
    ConnectNamedPipe(hPipe, &ov);

    LPTHREAD_START_ROUTINE pfnLoadLibrary = (LPTHREAD_START_ROUTINE)GetProcAddress(GetModuleHandleW(L"kernel32.dll"), "LoadLibraryW");
    HANDLE hThread = CreateRemoteThread(hProcess, nullptr, 0, pfnLoadLibrary, remoteMem, 0, nullptr);
    if (!hThread) {
        std::wcerr << L"[ERROR] CreateRemoteThread failed. Error: " << GetLastError() << L"\n";
        CancelIo(hPipe);
        CloseHandle(ov.hEvent);
        VirtualFreeEx(hProcess, remoteMem, 0, MEM_RELEASE);
        CloseHandle(hProcess);
        CloseHandle(hPipe);
        if (surfaceOpened && !leaveOpen) CloseSurface();
        return 1;
    }

    std::wcout << L"[INFO] Connecting to target process (" << resolvedName << L" PID " << pid << L")...\n";
    std::wcout << L"[INFO] If prompted for permission, please grant it now...\n";

    // Generous connection loop (up to 30 seconds with heartbeat)
    BOOL connected = FALSE;
    for (int waitSec = 0; waitSec < 30; ++waitSec) {
        DWORD waitRes = WaitForSingleObject(ov.hEvent, 1000);
        if (waitRes == WAIT_OBJECT_0) {
            connected = TRUE;
            break;
        }
        std::wcout << L".";
        std::wcout.flush();
    }
    std::wcout << L"\n";

    if (!connected) {
        CancelIo(hPipe);
        std::wcerr << L"[ERROR] Timeout waiting for target process connection.\n";
    }
    CloseHandle(ov.hEvent);

    std::string jsonPayload;
    if (connected) {
        std::wcout << L"[INFO] Reading XAML visual tree stream...\n";
        char buffer[4096];
        DWORD bytesRead = 0;
        OVERLAPPED readOv = { 0 };
        readOv.hEvent = CreateEventW(nullptr, TRUE, FALSE, nullptr);
        while (true) {
            ResetEvent(readOv.hEvent);
            BOOL readOk = ReadFile(hPipe, buffer, sizeof(buffer), &bytesRead, &readOv);
            if (!readOk) {
                DWORD rerr = GetLastError();
                if (rerr == ERROR_IO_PENDING) {
                    if (WaitForSingleObject(readOv.hEvent, 4000) == WAIT_OBJECT_0) {
                        GetOverlappedResult(hPipe, &readOv, &bytesRead, FALSE);
                    } else {
                        CancelIo(hPipe);
                        break;
                    }
                } else {
                    break;
                }
            }
            if (bytesRead > 0) {
                jsonPayload.append(buffer, bytesRead);
            } else {
                break;
            }
        }
        CloseHandle(readOv.hEvent);
    }

    WaitForSingleObject(hThread, 500);
    CloseHandle(hThread);
    VirtualFreeEx(hProcess, remoteMem, 0, MEM_RELEASE);
    CloseHandle(hProcess);
    CloseHandle(hPipe);

    // Close surface if opened and not requested to leave open
    if (surfaceOpened && !leaveOpen) {
        CloseSurface();
    }

    if (jsonPayload.empty()) {
        std::wcerr << L"[ERROR] Received empty response from target process.\n";
        return 1;
    }

    if (jsonPayload.find("\"error\":") != std::string::npos) {
        std::cerr << "[AGENT ERROR] " << jsonPayload << "\n";
        return 1;
    }

    if (format == L"json") {
        if (!outputFile.empty()) {
            std::ofstream out(outputFile);
            out << jsonPayload;
            std::wcout << L"[INFO] Saved JSON dump to " << outputFile << L"\n";
        } else {
            std::cout << jsonPayload << "\n";
        }
        return 0;
    }

    auto elements = ParseElements(jsonPayload);
    std::wcout << L"[INFO] Captured " << elements.size() << L" XAML visual tree elements.\n";

    auto roots = BuildTree(elements);
    std::string narrowFilter(filter.begin(), filter.end());

    std::stringstream ss;
    if (format == L"md" || format == L"markdown") {
        ss << "# Visual Tree: " << std::string(resolvedName.begin(), resolvedName.end()) 
           << " (PID " << pid << ")\n\n";
        for (const auto& r : roots) {
            PrintMarkdownTree(r, 0, maxDepth, narrowFilter, ss);
        }
    } else {
        ss << "=== Visual Tree: " << std::string(resolvedName.begin(), resolvedName.end()) 
           << " (PID " << pid << ", Elements: " << elements.size() << ") ===\n\n";
        for (const auto& r : roots) {
            PrintTextTree(r, 0, maxDepth, narrowFilter, ss);
        }
    }

    if (!outputFile.empty()) {
        std::ofstream out(outputFile);
        out << ss.str();
        std::wcout << L"[INFO] Saved visual tree to " << outputFile << L"\n";
    } else {
        std::cout << ss.str() << "\n";
    }

    return 0;
}
