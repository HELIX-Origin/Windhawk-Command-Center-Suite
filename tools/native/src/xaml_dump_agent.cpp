#include "common.h"
#include <xamlom.h>
#include <atomic>
#include <mutex>
#include <sstream>
#include <iomanip>
#include <vector>

static HMODULE g_hModule = nullptr;

struct ElementRecord {
    InstanceHandle handle;
    InstanceHandle parent;
    unsigned int childIndex;
    std::wstring type;
    std::wstring name;
    unsigned int numChildren;
};

static std::vector<ElementRecord> g_elements;
static std::mutex g_elementsMutex;
static std::atomic<ULONGLONG> g_lastElementTime{ 0 };
static std::atomic<size_t> g_elementCount{ 0 };
static IVisualTreeService* g_pVisualTreeService = nullptr;

static std::wstring EscapeJson(const std::wstring& s) {
    std::wostringstream o;
    for (wchar_t c : s) {
        if (c == L'"') o << L"\\\"";
        else if (c == L'\\') o << L"\\\\";
        else if (c == L'\b') o << L"\\b";
        else if (c == L'\f') o << L"\\f";
        else if (c == L'\n') o << L"\\n";
        else if (c == L'\r') o << L"\\r";
        else if (c == L'\t') o << L"\\t";
        else if (c >= 0 && c <= 0x1f) {
            o << L"\\u" << std::hex << std::setw(4) << std::setfill(L'0') << (int)c;
        } else {
            o << c;
        }
    }
    return o.str();
}

static std::atomic<bool> g_siteCalled{ false };
static std::atomic<HRESULT> g_adviseHr{ E_FAIL };

class VisualTreeCallback : public IVisualTreeServiceCallback2 {
public:
    std::atomic<ULONG> m_refCount{ 1 };

    HRESULT STDMETHODCALLTYPE QueryInterface(REFIID riid, void** ppvObject) override {
        if (!ppvObject) return E_POINTER;
        if (riid == IID_IUnknown || riid == __uuidof(IVisualTreeServiceCallback) || riid == __uuidof(IVisualTreeServiceCallback2)) {
            *ppvObject = static_cast<IVisualTreeServiceCallback2*>(this);
            AddRef();
            return S_OK;
        }
        *ppvObject = nullptr;
        return E_NOINTERFACE;
    }

    ULONG STDMETHODCALLTYPE AddRef() override {
        return ++m_refCount;
    }

    ULONG STDMETHODCALLTYPE Release() override {
        ULONG ref = --m_refCount;
        if (ref == 0) delete this;
        return ref;
    }

    HRESULT STDMETHODCALLTYPE OnVisualTreeChange(ParentChildRelation relation, VisualElement element, VisualMutationType mutationType) override {
        if (mutationType == Add) {
            ElementRecord rec;
            rec.handle = element.Handle;
            rec.parent = relation.Parent;
            rec.childIndex = relation.ChildIndex;
            rec.type = element.Type ? element.Type : L"";
            rec.name = element.Name ? element.Name : L"";
            rec.numChildren = element.NumChildren;

            {
                std::lock_guard<std::mutex> lock(g_elementsMutex);
                g_elements.push_back(std::move(rec));
                g_elementCount = g_elements.size();
                g_lastElementTime = GetTickCount64();
            }
        }
        return S_OK;
    }

    HRESULT STDMETHODCALLTYPE OnElementStateChanged(InstanceHandle element, VisualElementState elementState, LPCWSTR context) override {
        return S_OK;
    }
};

static VisualTreeCallback* g_pCallback = nullptr;

class XamlDumpTap : public IObjectWithSite {
public:
    std::atomic<ULONG> m_refCount{ 1 };
    IUnknown* m_pSite = nullptr;

    ~XamlDumpTap() {
        if (m_pSite) {
            m_pSite->Release();
            m_pSite = nullptr;
        }
    }

    HRESULT STDMETHODCALLTYPE QueryInterface(REFIID riid, void** ppvObject) override {
        if (!ppvObject) return E_POINTER;
        if (riid == IID_IUnknown || riid == IID_IObjectWithSite) {
            *ppvObject = static_cast<IObjectWithSite*>(this);
            AddRef();
            return S_OK;
        }
        *ppvObject = nullptr;
        return E_NOINTERFACE;
    }

    ULONG STDMETHODCALLTYPE AddRef() override {
        return ++m_refCount;
    }

    ULONG STDMETHODCALLTYPE Release() override {
        ULONG ref = --m_refCount;
        if (ref == 0) delete this;
        return ref;
    }

    HRESULT STDMETHODCALLTYPE SetSite(IUnknown* pUnkSite) override {
        if (pUnkSite) {
            g_siteCalled = true;
        }

        if (m_pSite) {
            m_pSite->Release();
            m_pSite = nullptr;
        }

        m_pSite = pUnkSite;
        if (m_pSite) {
            m_pSite->AddRef();

            // Decrease refcount increased by InitializeXamlDiagnosticsEx
            FreeLibrary(g_hModule);

            IVisualTreeService* vts = nullptr;
            if (SUCCEEDED(m_pSite->QueryInterface(__uuidof(IVisualTreeService3), (void**)&vts)) ||
                SUCCEEDED(m_pSite->QueryInterface(__uuidof(IVisualTreeService2), (void**)&vts)) ||
                SUCCEEDED(m_pSite->QueryInterface(__uuidof(IVisualTreeService), (void**)&vts))) {
                
                g_pVisualTreeService = vts;
                g_pCallback = new VisualTreeCallback();

                HANDLE hThread = CreateThread(nullptr, 0, [](LPVOID) -> DWORD {
                    if (g_pVisualTreeService && g_pCallback) {
                        g_adviseHr = g_pVisualTreeService->AdviseVisualTreeChange(g_pCallback);
                    }
                    return 0;
                }, nullptr, 0, nullptr);

                if (hThread) {
                    CloseHandle(hThread);
                }
            }
        }
        return S_OK;
    }

    HRESULT STDMETHODCALLTYPE GetSite(REFIID riid, void** ppvSite) override {
        if (!m_pSite) return E_FAIL;
        return m_pSite->QueryInterface(riid, ppvSite);
    }
};

class TapFactory : public IClassFactory {
public:
    HRESULT STDMETHODCALLTYPE QueryInterface(REFIID riid, void** ppvObject) override {
        if (!ppvObject) return E_POINTER;
        if (riid == IID_IUnknown || riid == IID_IClassFactory) {
            *ppvObject = static_cast<IClassFactory*>(this);
            return S_OK;
        }
        *ppvObject = nullptr;
        return E_NOINTERFACE;
    }

    ULONG STDMETHODCALLTYPE AddRef() override { return 1; }
    ULONG STDMETHODCALLTYPE Release() override { return 1; }

    HRESULT STDMETHODCALLTYPE CreateInstance(IUnknown* pUnkOuter, REFIID riid, void** ppvObject) override {
        if (pUnkOuter) return CLASS_E_NOAGGREGATION;
        XamlDumpTap* tap = new XamlDumpTap();
        HRESULT hr = tap->QueryInterface(riid, ppvObject);
        tap->Release();
        return hr;
    }

    HRESULT STDMETHODCALLTYPE LockServer(BOOL) override {
        return S_OK;
    }
};

static TapFactory g_factory;

STDAPI DllGetClassObject(REFCLSID rclsid, REFIID riid, LPVOID* ppv) {
    if (rclsid == CLSID_XamlDumpTap) {
        return g_factory.QueryInterface(riid, ppv);
    }
    return CLASS_E_CLASSNOTAVAILABLE;
}

STDAPI DllCanUnloadNow() {
    return S_OK;
}

using PFN_INITIALIZE_XAML_DIAGNOSTICS_EX = decltype(&InitializeXamlDiagnosticsEx);

static DWORD WINAPI AgentWorkerThread(LPVOID) {
    CoInitializeEx(nullptr, COINIT_MULTITHREADED);

    std::wstring pipeName = std::wstring(XAML_DUMP_PIPE_PREFIX) + std::to_wstring(GetCurrentProcessId());
    HANDLE hPipe = INVALID_HANDLE_VALUE;

    // Retry connecting to named pipe created by driver for up to 10 seconds
    for (int i = 0; i < 100; i++) {
        hPipe = CreateFileW(pipeName.c_str(), GENERIC_WRITE, 0, nullptr, OPEN_EXISTING, 0, nullptr);
        if (hPipe != INVALID_HANDLE_VALUE) break;
        Sleep(100);
    }

    if (hPipe == INVALID_HANDLE_VALUE) {
        CoUninitialize();
        return 1;
    }

    HMODULE hXaml = GetModuleHandleW(L"Windows.UI.Xaml.dll");
    if (!hXaml) {
        hXaml = GetModuleHandleW(L"Microsoft.UI.Xaml.dll");
    }

    if (!hXaml) {
        std::string err = "{\"error\": \"No XAML runtime (Windows.UI.Xaml or Microsoft.UI.Xaml) loaded in process.\"}";
        DWORD written = 0;
        WriteFile(hPipe, err.c_str(), (DWORD)err.size(), &written, nullptr);
        CloseHandle(hPipe);
        CoUninitialize();
        return 1;
    }

    auto pfnInit = reinterpret_cast<PFN_INITIALIZE_XAML_DIAGNOSTICS_EX>(GetProcAddress(hXaml, "InitializeXamlDiagnosticsEx"));
    if (!pfnInit) {
        std::string err = "{\"error\": \"InitializeXamlDiagnosticsEx not found in XAML runtime.\"}";
        DWORD written = 0;
        WriteFile(hPipe, err.c_str(), (DWORD)err.size(), &written, nullptr);
        CloseHandle(hPipe);
        CoUninitialize();
        return 1;
    }

    WCHAR location[MAX_PATH];
    if (!GetModuleFileNameW(g_hModule, location, MAX_PATH)) {
        CloseHandle(hPipe);
        CoUninitialize();
        return 1;
    }

    HRESULT hr = E_FAIL;
    for (int i = 0; i < 1000; i++) {
        WCHAR connName[64];
        wsprintfW(connName, L"VisualDiagConnection%d", i + 1);
        hr = pfnInit(connName, GetCurrentProcessId(), L"", location, CLSID_XamlDumpTap, nullptr);
        if (hr != HRESULT_FROM_WIN32(ERROR_NOT_FOUND)) {
            break;
        }
    }

    if (FAILED(hr)) {
        std::ostringstream ss;
        ss << "{\"error\": \"InitializeXamlDiagnosticsEx failed with HRESULT 0x" << std::hex << hr << "\"}";
        std::string err = ss.str();
        DWORD written = 0;
        WriteFile(hPipe, err.c_str(), (DWORD)err.size(), &written, nullptr);
        CloseHandle(hPipe);
        CoUninitialize();
        return 1;
    }

    // Wait for visual tree enumeration to populate and settle
    ULONGLONG startWait = GetTickCount64();
    while (GetTickCount64() - startWait < 3000) {
        Sleep(50);
        if (g_elementCount > 0 && (GetTickCount64() - g_lastElementTime > 300)) {
            break;
        }
    }

    if (g_pVisualTreeService && g_pCallback) {
        g_pVisualTreeService->UnadviseVisualTreeChange(g_pCallback);
    }

    // Serialize elements to JSON
    std::wostringstream json;
    json << L"{\"pid\": " << GetCurrentProcessId()
         << L", \"siteCalled\": " << (g_siteCalled.load() ? L"true" : L"false")
         << L", \"adviseHr\": \"0x" << std::hex << (ULONG)g_adviseHr.load() << L"\""
         << L", \"count\": " << std::dec << g_elements.size()
         << L", \"elements\": [";

    {
        std::lock_guard<std::mutex> lock(g_elementsMutex);
        for (size_t i = 0; i < g_elements.size(); ++i) {
            const auto& el = g_elements[i];
            if (i > 0) json << L",";
            json << L"{"
                 << L"\"handle\":\"0x" << std::hex << el.handle << L"\","
                 << L"\"parent\":\"0x" << std::hex << el.parent << L"\","
                 << L"\"childIndex\":" << std::dec << el.childIndex << L","
                 << L"\"type\":\"" << EscapeJson(el.type) << L"\","
                 << L"\"name\":\"" << EscapeJson(el.name) << L"\","
                 << L"\"numChildren\":" << el.numChildren
                 << L"}";
        }
    }
    json << L"]}";

    std::wstring wstr = json.str();
    int utf8Len = WideCharToMultiByte(CP_UTF8, 0, wstr.c_str(), (int)wstr.size(), nullptr, 0, nullptr, nullptr);
    if (utf8Len > 0) {
        std::string utf8Str(utf8Len, '\0');
        WideCharToMultiByte(CP_UTF8, 0, wstr.c_str(), (int)wstr.size(), &utf8Str[0], utf8Len, nullptr, nullptr);
        DWORD written = 0;
        WriteFile(hPipe, utf8Str.c_str(), (DWORD)utf8Str.size(), &written, nullptr);
    }

    FlushFileBuffers(hPipe);
    CloseHandle(hPipe);
    CoUninitialize();

    // Self-unload cleanly
    FreeLibraryAndExitThread(g_hModule, 0);
    return 0;
}

BOOL WINAPI DllMain(HINSTANCE hinstDLL, DWORD fdwReason, LPVOID) {
    if (fdwReason == DLL_PROCESS_ATTACH) {
        DisableThreadLibraryCalls(hinstDLL);
        g_hModule = (HMODULE)hinstDLL;
        HANDLE hThread = CreateThread(nullptr, 0, (LPTHREAD_START_ROUTINE)AgentWorkerThread, nullptr, 0, nullptr);
        if (hThread) {
            CloseHandle(hThread);
        }
    }
    return TRUE;
}
