#pragma once

#include <windows.h>
#include <sddl.h>
#include <string>

// Approved shell target processes per Rule 01
static const wchar_t* APPROVED_PROCESSES[] = {
    L"StartMenuExperienceHost.exe",
    L"SearchHost.exe",
    L"SearchApp.exe",
    L"LockApp.exe",
    L"ShellExperienceHost.exe",
    L"ShellHost.exe",
    L"SystemSettings.exe",
    L"explorer.exe"
};

// Check if a process name is in the approved targets list
inline bool IsApprovedProcess(const std::wstring& procName) {
    for (const auto* approved : APPROVED_PROCESSES) {
        if (_wcsicmp(procName.c_str(), approved) == 0) {
            return true;
        }
    }
    return false;
}

// Named pipe prefix for communication between xaml_dump.exe and xaml_dump_agent.dll
#define XAML_DUMP_PIPE_PREFIX L"\\\\.\\pipe\\WindhawkXamlDumpPipe_"

// Diagnostic TAP CLSID
// {E5D3454B-E08A-4B6A-95E0-0E0000000001}
static const GUID CLSID_XamlDumpTap = 
    { 0xe5d3454b, 0xe08a, 0x4b6a, { 0x95, 0xe0, 0x0e, 0x00, 0x00, 0x00, 0x00, 0x01 } };
