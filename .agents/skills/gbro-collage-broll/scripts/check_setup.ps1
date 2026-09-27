$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()

$failed = $false

function Write-Pass([string]$Message) {
    Write-Output "PASS  $Message"
}

function Write-Fail([string]$Message) {
    Write-Output "FAIL  $Message"
    $script:failed = $true
}

if (-not [string]::IsNullOrWhiteSpace($env:GEMINI_API_KEY)) {
    Write-Pass "GEMINI_API_KEY 已设置"
} else {
    Write-Fail "GEMINI_API_KEY 未设置（到 https://aistudio.google.com/apikey 创建后设置为当前进程或用户环境变量）"
}

if ((Get-Command ffmpeg -ErrorAction SilentlyContinue) -and
    (Get-Command ffprobe -ErrorAction SilentlyContinue)) {
    Write-Pass "ffmpeg / ffprobe 可用"
} else {
    Write-Fail "ffmpeg / ffprobe 缺失"
}

$pythonOk = $false
if (Get-Command py -ErrorAction SilentlyContinue) {
    & py -3 -c "import sys; raise SystemExit(0 if sys.version_info >= (3, 10) else 1)" 2>$null
    $pythonOk = ($LASTEXITCODE -eq 0)
}

if ($pythonOk) {
    Write-Pass "Python >= 3.10"
} else {
    Write-Fail "Python 缺失或版本低于 3.10"
}

$venvPython = if (-not [string]::IsNullOrWhiteSpace($env:GBRO_OMNI_PYTHON)) {
    $env:GBRO_OMNI_PYTHON
} else {
    Join-Path $env:USERPROFILE "hyperframes-projects\.omni-venv\Scripts\python.exe"
}

$venvOk = $false
if (Test-Path -LiteralPath $venvPython -PathType Leaf) {
    & $venvPython -c "from importlib.metadata import version; parts=tuple(int(x) for x in version('google-genai').split('.')[:2]); raise SystemExit(0 if parts >= (2, 10) else 1)" 2>$null
    $venvOk = ($LASTEXITCODE -eq 0)
}

if ($venvOk) {
    Write-Pass "共享 venv 就绪（google-genai >= 2.10.0）"
} else {
    Write-Fail "共享 venv 未创建或 google-genai 版本过旧（Windows 路径：$venvPython）"
}

if ($failed) {
    exit 1
}

exit 0
