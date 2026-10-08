# Eject xaml_dump_agent.dll from all processes that loaded it
Add-Type @"
using System;
using System.Runtime.InteropServices;

public class NativeEject {
    [DllImport("kernel32.dll", SetLastError = true)]
    public static extern IntPtr OpenProcess(uint processAccess, bool bInheritHandle, int processId);

    [DllImport("kernel32.dll", SetLastError = true)]
    public static extern IntPtr GetProcAddress(IntPtr hModule, string lpProcName);

    [DllImport("kernel32.dll", SetLastError = true)]
    public static extern IntPtr GetModuleHandle(string lpModuleName);

    [DllImport("kernel32.dll", SetLastError = true)]
    public static extern IntPtr CreateRemoteThread(IntPtr hProcess, IntPtr lpThreadAttributes, uint dwStackSize, IntPtr lpStartAddress, IntPtr lpParameter, uint dwCreationFlags, out IntPtr lpThreadId);

    [DllImport("kernel32.dll", SetLastError = true)]
    public static extern uint WaitForSingleObject(IntPtr hHandle, uint dwMilliseconds);

    [DllImport("kernel32.dll", SetLastError = true)]
    public static extern bool CloseHandle(IntPtr hObject);
}
"@

$approvedPids = @(7980, 21744, 20100, 1816, 23376)
foreach ($pidNum in $approvedPids) {
    try {
        $p = Get-Process -Id $pidNum -ErrorAction SilentlyContinue
        if ($p) {
            foreach ($mod in $p.Modules) {
                if ($mod.ModuleName -like "*xaml_dump_agent*") {
                    Write-Host "Found xaml_dump_agent in $($p.Name) (PID: $pidNum) at $($mod.BaseAddress)"
                    $hProcess = [NativeEject]::OpenProcess(0x1F0FFF, $false, $pidNum)
                    if ($hProcess -ne [IntPtr]::Zero) {
                        $freeLib = [NativeEject]::GetProcAddress([NativeEject]::GetModuleHandle("kernel32.dll"), "FreeLibrary")
                        $tId = [IntPtr]::Zero
                        $hThread = [NativeEject]::CreateRemoteThread($hProcess, [IntPtr]::Zero, 0, $freeLib, $mod.BaseAddress, 0, [ref]$tId)
                        if ($hThread -ne [IntPtr]::Zero) {
                            [NativeEject]::WaitForSingleObject($hThread, 2000) | Out-Null
                            [NativeEject]::CloseHandle($hThread) | Out-Null
                            Write-Host "Ejected xaml_dump_agent from $($p.Name)"
                        }
                        [NativeEject]::CloseHandle($hProcess) | Out-Null
                    }
                }
            }
        }
    } catch {}
}
