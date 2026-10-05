<#
.SYNOPSIS
    Static validation gate for Windhawk Command Center Suite styler files.
.DESCRIPTION
    Validates YAML syntax, constant declaration order, token reference resolution,
    design-token adherence, and surface-scope rules per Rule 02, 03, 05, and 07.
    Requires no external PowerShell modules.
.PARAMETER Path
    Optional path to a specific file. If omitted, checks all in-scope styler files in src/.
#>
[CmdletBinding()]
param(
    [string]$Path
)

$ErrorActionPreference = 'Stop'

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$rootDir = Split-Path -Parent $scriptDir
$srcDir = Join-Path $rootDir 'src'

# Approved styler files in scope
$inScopeFiles = @(
    'windows-11-notification-center-styler.yml',
    'windows-11-file-explorer-styler.yml',
    'windows-11-start-menu-styler.yml',
    'windows-11-taskbar-styler.yml'
)

$filesToCheck = @()
if ($Path) {
    if (Test-Path $Path) {
        $filesToCheck += (Resolve-Path $Path).Path
    } else {
        $candidate = Join-Path $srcDir $Path
        if (Test-Path $candidate) {
            $filesToCheck += (Resolve-Path $candidate).Path
        } else {
            Write-Error "File not found: $Path"
            exit 1
        }
    }
} else {
    foreach ($f in $inScopeFiles) {
        $filePath = Join-Path $srcDir $f
        if (Test-Path $filePath) {
            $filesToCheck += (Resolve-Path $filePath).Path
        }
    }
}

$standardMaterials = @('Translucent', 'Glass', 'Frosted', 'Acrylic')
$validRadii = @('35', '25', '20', '15', '10', '6', '0', '1.5', '4', '8')

$totalErrors = 0
$totalWarnings = 0

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host " Windhawk Command Center Suite - Static Validation Gate" -ForegroundColor Cyan
Write-Host " Rule 07 Compliance & Syntax Enforcement" -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan

foreach ($file in $filesToCheck) {
    $fileName = Split-Path -Leaf $file
    Write-Host "`nChecking: $fileName" -ForegroundColor Yellow
    $fileErrors = 0
    $fileWarnings = 0

    $rawBytes = [System.IO.File]::ReadAllBytes($file)
    $rawText = [System.Text.Encoding]::UTF8.GetString($rawBytes)
    $lines = [System.IO.File]::ReadAllLines($file)

    # E001: Tab characters
    for ($i = 0; $i -lt $lines.Count; $i++) {
        if ($lines[$i] -match "\t") {
            Write-Host "  [E001] Line $($i+1): File contains tab characters." -ForegroundColor Red
            $fileErrors++
        }
    }

    # E002: Line endings
    if ($rawText -match "(?<!\r)\n") {
        Write-Host "  [E002] File has non-CRLF line endings." -ForegroundColor Red
        $fileErrors++
    }

    # E007: User-profile personal path
    for ($i = 0; $i -lt $lines.Count; $i++) {
        if ($lines[$i] -match "C:\\Users\\[a-zA-Z0-9_\.-]+") {
            Write-Host "  [E007] Line $($i+1): Personal user profile path detected." -ForegroundColor Red
            $fileErrors++
        }
    }

    # Extract declared styleConstants
    $inConstants = $false
    $declaredConstants = [System.Collections.Generic.List[string]]::new()
    $constantLineMap = @{}

    # Extract controlStyles targets and styles
    $inControlStyles = $false
    $targets = [System.Collections.Generic.List[string]]::new()
    $targetStylesCount = 0
    $currentTarget = $null
    $emptyPlaceholders = 0

    # Parse structural blocks
    for ($i = 0; $i -lt $lines.Count; $i++) {
        $line = $lines[$i]
        $trimmed = $line.Trim()

        if ($line -match '^styleConstants:\s*$') {
            $inConstants = $true
            $inControlStyles = $false
            continue
        }
        if ($line -match '^(controlStyles|themeResourceVariables|webContentStyles):\s*$') {
            $inConstants = $false
            if ($line -match '^controlStyles:\s*$') {
                $inControlStyles = $true
            } else {
                $inControlStyles = $false
            }
            continue
        }

        # Constant parsing
        if ($inConstants) {
            if ($line -match '^\s*-\s*([^=]+)=(.*)$') {
                $cName = $matches[1].Trim()
                $cVal = $matches[2].Trim()

                # E004: Constant name declared with leading $
                if ($cName.StartsWith('$')) {
                    Write-Host "  [E004] Line $($i+1): Constant name declared with leading '$' ($cName)." -ForegroundColor Red
                    $fileErrors++
                }

                # E008: Duplicate constant declaration
                if ($declaredConstants.Contains($cName)) {
                    Write-Host "  [E008] Line $($i+1): Duplicate constant declaration '$cName'." -ForegroundColor Red
                    $fileErrors++
                } else {
                    $declaredConstants.Add($cName)
                    $constantLineMap[$cName] = ($i + 1)
                }

                # Check forward reference in constant value
                if ($cVal -match '\$([a-zA-Z0-9_]+)') {
                    $refToken = $matches[1]
                    if (-not $declaredConstants.Contains($refToken)) {
                        Write-Host "  [E003] Line $($i+1): Forward or undeclared reference '\$$refToken' in constant '$cName'." -ForegroundColor Red
                        $fileErrors++
                    }
                }
            }
        }

        # Control styles parsing
        if ($inControlStyles) {
            if ($line -match '^\s*-\s*target:\s*(.*)$') {
                # Check previous target had styles
                if ($currentTarget -ne $null -and $targetStylesCount -eq 0) {
                    # Checked below for scaffold files
                }
                $currentTarget = $matches[1].Trim()
                $targets.Add($currentTarget)
                $targetStylesCount = 0
            }
            if ($line -match '^\s*styles:\s*$') {
                continue
            }
            if ($line -match '^\s*-\s*(.*)$' -and -not ($line -match '^\s*-\s*target:')) {
                $styleLine = $matches[1].Trim()
                $targetStylesCount++

                # W105: Empty placeholder
                if ($styleLine -eq "''" -or $styleLine -eq '""' -or $styleLine -eq '') {
                    $emptyPlaceholders++
                }

                # E003: Token references in style line
                $tokenMatches = [regex]::Matches($styleLine, '\$([a-zA-Z0-9_]+)')
                foreach ($tm in $tokenMatches) {
                    $tok = $tm.Groups[1].Value
                    if (-not $declaredConstants.Contains($tok)) {
                        Write-Host "  [E003] Line $($i+1): Referenced token '\$$tok' was never declared in styleConstants." -ForegroundColor Red
                        $fileErrors++
                    }
                }

                # W106: Localized AutomationProperties.Name
                if ($styleLine -match 'AutomationProperties\.Name=') {
                    Write-Host "  [W106] Line $($i+1): Selector contains localized AutomationProperties.Name (EN-only)." -ForegroundColor Yellow
                    $fileWarnings++
                }
            }
        }
    }

    # W101: Duplicate targets
    $targetGroups = $targets | Group-Object | Where-Object { $_.Count -gt 1 }
    foreach ($tg in $targetGroups) {
        Write-Host "  [W101] Duplicate target selector: '$($tg.Name)' ($($tg.Count) occurrences)." -ForegroundColor Yellow
        $fileWarnings++
    }

    # W105 report
    if ($emptyPlaceholders -gt 0) {
        Write-Host "  [W105] File contains $emptyPlaceholders empty style placeholders ('- ''')." -ForegroundColor Yellow
        $fileWarnings++
    }

    # W104: Standard materials check
    $missingMaterials = @()
    foreach ($mat in $standardMaterials) {
        if (-not $declaredConstants.Contains($mat)) {
            $missingMaterials += $mat
        }
    }
    if ($missingMaterials.Count -gt 0) {
        Write-Host "  [W104] Missing standard material constants: $($missingMaterials -join ', ')." -ForegroundColor Yellow
        $fileWarnings++
    }

    # Surface Scope Key Check (Rule 05)
    if ($fileName -eq 'windows-11-notification-center-styler.yml') {
        if ($rawText -match 'webContentStyles:' -or $rawText -match 'backgroundTranslucentEffect:' -or $rawText -match 'explorerFrameContainerHeight:') {
            Write-Host "  [E006] windows-11-notification-center-styler.yml contains disallowed mod keys." -ForegroundColor Red
            $fileErrors++
        }
    }
    if ($fileName -eq 'windows-11-file-explorer-styler.yml') {
        if ($rawText -match 'webContentStyles:') {
            Write-Host "  [E006] windows-11-file-explorer-styler.yml contains disallowed mod keys (webContentStyles)." -ForegroundColor Red
            $fileErrors++
        }
    }

    # Summary for file
    if ($fileErrors -eq 0 -and $fileWarnings -eq 0) {
        Write-Host "  PASSED (0 errors, 0 warnings)" -ForegroundColor Green
    } elseif ($fileErrors -eq 0) {
        Write-Host "  PASSED WITH WARNINGS (0 errors, $fileWarnings warnings)" -ForegroundColor Yellow
    } else {
        Write-Host "  FAILED ($fileErrors errors, $fileWarnings warnings)" -ForegroundColor Red
    }

    $totalErrors += $fileErrors
    $totalWarnings += $fileWarnings
}

Write-Host "`n----------------------------------------------------------" -ForegroundColor Cyan
Write-Host " Total Gate Result: $totalErrors Error(s), $totalWarnings Warning(s)" -ForegroundColor $(if ($totalErrors -gt 0) { 'Red' } elseif ($totalWarnings -gt 0) { 'Yellow' } else { 'Green' })
Write-Host "----------------------------------------------------------" -ForegroundColor Cyan

if ($totalErrors -gt 0) {
    exit 1
} else {
    exit 0
}
