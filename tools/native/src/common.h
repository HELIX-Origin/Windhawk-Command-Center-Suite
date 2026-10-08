#pragma once

#include <windows.h>
#include <sddl.h>
#include <string>
#include <vector>

// CLSID for XamlDumpTap COM Class
// {B4C81132-732C-4A82-9B7E-76FDFD66A901}
static constexpr CLSID CLSID_XamlDumpTap = {
    0xb4c81132, 0x732c, 0x4a82, { 0x9b, 0x7e, 0x76, 0xfd, 0xfd, 0x66, 0xa9, 0x01 }
};

// Named Pipe Prefix
#define XAML_DUMP_PIPE_PREFIX L"\\\\.\\pipe\\XamlDumpPipe_"

// Approved Target Processes per Rule 01
inline const wchar_t* APPROVED_PROCESSES[] = {
    L"StartMenuExperienceHost.exe",
    L"SearchApp.exe",
    L"SearchHost.exe",
    L"ShellHost.exe",
    L"ShellExperienceHost.exe",
    L"explorer.exe",
    L"LockApp.exe"
};

inline bool IsApprovedProcess(const std::wstring& procName) {
    for (const auto* approved : APPROVED_PROCESSES) {
        if (_wcsicmp(procName.c_str(), approved) == 0) {
            return true;
        }
    }
    return false;
}
