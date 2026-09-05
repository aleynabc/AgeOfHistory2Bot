$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $ScriptDir

function Step($text) { Write-Host "`n==> $text" -ForegroundColor Cyan }
function Has-Command($name) { return [bool](Get-Command $name -ErrorAction SilentlyContinue) }

$isAdmin = ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
if (-not $isAdmin) {
    Start-Process powershell -Verb RunAs -ArgumentList "-NoProfile -ExecutionPolicy Bypass -File `"$PSCommandPath`""
    exit
}

Write-Host "=============================================" -ForegroundColor Green
Write-Host " Age Of History 2 Bot - Professional Build" -ForegroundColor Green
Write-Host "=============================================" -ForegroundColor Green

Step "Python kontrol ediliyor..."
$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
    if (Has-Command winget) {
        winget install -e --id Python.Python.3.14 --scope user --silent --accept-package-agreements --accept-source-agreements
    } else {
        $url = "https://www.python.org/ftp/python/3.14.0/python-3.14.0-amd64.exe"
        $installer = Join-Path $env:TEMP "python-aoh2bot-installer.exe"
        Invoke-WebRequest -UseBasicParsing $url -OutFile $installer
        Start-Process $installer -ArgumentList "/quiet InstallAllUsers=0 PrependPath=1 Include_test=0 Include_pip=1" -Wait
        Remove-Item $installer -Force -ErrorAction SilentlyContinue
    }
    $env:Path = "$env:LOCALAPPDATA\Programs\Python\Python314;$env:LOCALAPPDATA\Programs\Python\Python314\Scripts;$env:Path"
}
$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) { throw "Python otomatik kurulamadı." }

Step "Python bağımlılıkları otomatik kuruluyor..."
python -m ensurepip --upgrade
python -m pip install --upgrade pip --disable-pip-version-check
python -m pip install --upgrade -r requirements.txt --disable-pip-version-check

Step "EXE derleniyor..."
Remove-Item build,dist,installer_output -Recurse -Force -ErrorAction SilentlyContinue
python -m PyInstaller --clean --noconfirm AgeOfHistory2Bot.spec
if (-not (Test-Path "dist\AgeOfHistory2Bot.exe")) { throw "EXE oluşturulamadı." }

Step "Inno Setup kontrol ediliyor..."
$iscc = @(
    "$env:ProgramFiles(x86)\Inno Setup 6\ISCC.exe",
    "$env:ProgramFiles\Inno Setup 6\ISCC.exe"
) | Where-Object { Test-Path $_ } | Select-Object -First 1

if (-not $iscc) {
    if (Has-Command winget) {
        winget install -e --id JRSoftware.InnoSetup --silent --accept-package-agreements --accept-source-agreements
    } else {
        $url = "https://jrsoftware.org/download.php/is.exe"
        $installer = Join-Path $env:TEMP "innosetup-aoh2bot.exe"
        Invoke-WebRequest -UseBasicParsing $url -OutFile $installer
        Start-Process $installer -ArgumentList "/VERYSILENT /SUPPRESSMSGBOXES /NORESTART /SP-" -Wait
        Remove-Item $installer -Force -ErrorAction SilentlyContinue
    }
    $iscc = @(
        "$env:ProgramFiles(x86)\Inno Setup 6\ISCC.exe",
        "$env:ProgramFiles\Inno Setup 6\ISCC.exe"
    ) | Where-Object { Test-Path $_ } | Select-Object -First 1
}
if (-not $iscc) { throw "Inno Setup otomatik kurulamadı." }

Step "Kurulum paketi oluşturuluyor..."
& $iscc "installer.iss"
$final = Join-Path $ScriptDir "installer_output\AgeOfHistory2Bot_Kurulum.exe"
if (-not (Test-Path $final)) { throw "Kurulum paketi oluşturulamadı." }

Write-Host "`n=============================================" -ForegroundColor Green
Write-Host " TAMAMLANDI" -ForegroundColor Green
Write-Host " Kurulum: $final" -ForegroundColor Green
Write-Host "=============================================" -ForegroundColor Green
Start-Process explorer.exe (Split-Path $final -Parent)
