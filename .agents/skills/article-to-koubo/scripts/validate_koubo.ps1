param(
    [Parameter(Mandatory = $true)]
    [string]$Path
)

$ErrorActionPreference = "Stop"

if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) {
    Write-Error "Target file does not exist: $Path"
}

$content = Get-Content -LiteralPath $Path

if ($content.Count -eq 0 -or (($content -join "").Trim().Length -eq 0)) {
    Write-Error "Target file is empty: $Path"
}

$hasError = $false

for ($i = 0; $i -lt $content.Count; $i++) {
    $line = $content[$i]
    if ($line.Length -gt 15) {
        Write-Output ("LINE_LENGTH {0}: {1} ({2})" -f ($i + 1), $line, $line.Length)
        $hasError = $true
    }
}

$markdownPattern = '^\s{0,3}#|^\s*[-*_]{3,}\s*$|!\[\[|!\[[^\]]*\]\(|```|\*\*|^\s*>|^\s*[-*+]\s+|^\s*\d+\.\s+|^\s*\|.*\|\s*$|【|】'
for ($i = 0; $i -lt $content.Count; $i++) {
    $line = $content[$i]
    if ($line -match $markdownPattern) {
        Write-Output ("MARKDOWN_RESIDUE {0}: {1}" -f ($i + 1), $line)
        $hasError = $true
    }
}

if ($hasError) {
    exit 1
}

Write-Output "OK"
