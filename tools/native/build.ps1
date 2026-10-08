<#
.SYNOPSIS
    Builds the native XAML inspection toolchain for Windhawk Command Center Suite.
.DESCRIPTION
    Compiles xaml_dump.exe (CLI driver) and xaml_dump_agent.dll (in-process XAML TAP agent)
    using Microsoft Visual Studio 2026 MSVC and Windows 11 SDK.
    Applies AppContainer permissions (*S-1-15-2-1:RX) to the agent DLL.
#>
[CmdletBinding()]
param(
    [switch]$Clean
)

$ErrorActionPreference = 'Stop'

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$srcDir = Join-Path $scriptDir 'src'
$buildDir = Join-Path $scriptDir 'build'
$binDir = Join-Path $scriptDir 'bin'

if ($Clean) {
    Write-Host "[BUILD] Cleaning build and bin directories..." -ForegroundColor Yellow
    if (Test-Path $buildDir) { Remove-Item -Path $buildDir -Recurse -Force }
    if (Test-Path $binDir) { Remove-Item -Path $binDir -Recurse -Force }
}

New-Item -ItemType Directory -Force -Path $buildDir | Out-Null
New-Item -ItemType Directory -Force -Path $binDir | Out-Null

# Stop any running xaml_dump CLI
Get-Process -Name "xaml_dump" -ErrorAction SilentlyContinue | Stop-Process -Force

# Auto-eject old agent DLL if in use
$ejectScript = Join-Path $scriptDir 'eject_agent.ps1'
if (Test-Path $ejectScript) {
    try { & $ejectScript | Out-Null } catch {}
}

# Locate Visual Studio 2026 vcvars64.bat
$vcvarsCandidates = @(
    "C:\Program Files\Microsoft Visual Studio\18\Insiders\VC\Auxiliary\Build\vcvars64.bat",
    "C:\Program Files\Microsoft Visual Studio\18\Community\VC\Auxiliary\Build\vcvars64.bat",
    "C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\Build\vcvars64.bat",
    "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvars64.bat"
)

$vcvarsPath = $null
foreach ($cand in $vcvarsCandidates) {
    if (Test-Path $cand) {
        $vcvarsPath = $cand
        break
    }
}

if (-not $vcvarsPath) {
    throw "Visual Studio Developer Environment (vcvars64.bat) could not be located."
}

Write-Host "[BUILD] Using compiler environment: $vcvarsPath" -ForegroundColor Cyan

# Batch compile script running inside vcvars64 context
$compileBatch = Join-Path $buildDir 'compile.bat'
$batchContent = @"
@echo off
call "$vcvarsPath" || exit /b 1

echo [BUILD] Compiling xaml_dump_agent.dll...
cl.exe /nologo /O2 /W3 /EHsc /MD /std:c++17 /LD "$srcDir\xaml_dump_agent.cpp" /Fo"$buildDir\\" /Fd"$buildDir\\" /link /OUT:"$binDir\xaml_dump_agent.dll" /EXPORT:DllGetClassObject /EXPORT:DllCanUnloadNow ole32.lib oleaut32.lib advapi32.lib user32.lib kernel32.lib || exit /b 1

echo [BUILD] Compiling xaml_dump.exe...
cl.exe /nologo /O2 /W3 /EHsc /MD /std:c++17 "$srcDir\xaml_dump.cpp" /Fo"$buildDir\\" /Fd"$buildDir\\" /link /OUT:"$binDir\xaml_dump.exe" advapi32.lib user32.lib kernel32.lib || exit /b 1

exit /b 0
"@

Set-Content -Path $compileBatch -Value $batchContent -Encoding ASCII

cmd.exe /c $compileBatch
if ($LASTEXITCODE -ne 0) {
    throw "Compilation failed with exit code $LASTEXITCODE"
}

# Grant ALL APPLICATION PACKAGES access to xaml_dump_agent.dll for UWP/AppContainer
$agentDll = Join-Path $binDir 'xaml_dump_agent.dll'
if (Test-Path $agentDll) {
    Write-Host "[BUILD] Granting AppContainer permissions to $agentDll..." -ForegroundColor Cyan
    & icacls "$agentDll" /grant "*S-1-15-2-1:(RX)" | Out-Null
}

Write-Host "[BUILD] Build succeeded!" -ForegroundColor Green
Write-Host "  Driver CLI: $binDir\xaml_dump.exe" -ForegroundColor Green
Write-Host "  Agent DLL:  $binDir\xaml_dump_agent.dll" -ForegroundColor Green
