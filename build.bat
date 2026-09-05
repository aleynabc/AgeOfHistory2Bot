@echo off
setlocal EnableExtensions EnableDelayedExpansion
cd /d "%~dp0"

rem Inno Setup kurulumu ve kurulum paketi icin yonetici yetkisi gerekir.
rem Script kendini otomatik olarak yukselterek tek tik build akisini korur.
net session >nul 2>&1
if errorlevel 1 (
    echo [INFO] Yonetici yetkisi isteniyor...
    powershell -NoProfile -ExecutionPolicy Bypass -Command "Start-Process -FilePath '%~f0' -Verb RunAs"
    exit /b 0
)

title Age Of History 2 Bot - Professional Build

set "PY_CMD="
set "PY_EXE="

call :find_python
if defined PY_EXE goto :python_ready

call :install_python
if errorlevel 1 goto :error
call :find_python
if not defined PY_EXE goto :error

:python_ready

echo ============================================
echo   Age Of History 2 Bot - Professional Build
echo ============================================
echo.
echo [INFO] Python: %PY_EXE%
%PY_EXE% --version
if errorlevel 1 goto :error

echo.
echo [1/4] pip ve build bagimliliklari hazirlaniyor...
%PY_EXE% -m ensurepip --upgrade >nul 2>&1
%PY_EXE% -m pip install --upgrade pip --disable-pip-version-check
if errorlevel 1 goto :error

%PY_EXE% -m pip install --upgrade --requirement requirements.txt --disable-pip-version-check
if errorlevel 1 goto :error

rem PyInstaller 6.15+ Python 3.14 destegi saglar; 6.22.2 guncel kararlı seridir.
%PY_EXE% -m PyInstaller --version
if errorlevel 1 goto :error

if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist installer_output rmdir /s /q installer_output

if not exist "app_icon.ico" (
    echo [HATA] app_icon.ico bulunamadi.
    goto :error
)
if not exist "titlebar_icon.png" (
    echo [HATA] titlebar_icon.png bulunamadi.
    goto :error
)

 echo.
echo [2/4] EXE derleniyor...
%PY_EXE% -m PyInstaller --clean --noconfirm AgeOfHistory2Bot.spec
if errorlevel 1 goto :error
if not exist "dist\AgeOfHistory2Bot.exe" goto :error

 echo.
echo [3/4] Inno Setup kontrol ediliyor...
call :find_iscc
if defined ISCC goto :installer_ready

 echo [INFO] Inno Setup bulunamadi. Otomatik kurulacak...
call :install_inno
if errorlevel 1 goto :error
call :find_iscc
if not defined ISCC goto :error

:installer_ready
 echo.
echo [4/4] Windows kurulum paketi olusturuluyor...
"%ISCC%" "installer.iss"
if errorlevel 1 goto :error

if not exist "installer_output\AgeOfHistory2Bot_Kurulum.exe" goto :error

echo.
echo ============================================
echo   BUILD TAMAMLANDI
 echo ============================================
echo.
echo EXE:
echo %CD%\dist\AgeOfHistory2Bot.exe
echo.
echo KURULUM PAKETI:
echo %CD%\installer_output\AgeOfHistory2Bot_Kurulum.exe
echo.
echo Bu dosya baska bir Windows bilgisayarda Python/kutuphane gerektirmez.
echo Kurulum paketi gercek Windows kisayollari olusturur.
echo.
echo [INFO] Kurulum sihirbazi simdi aciliyor...
start "" "%CD%\installer_output\AgeOfHistory2Bot_Kurulum.exe"
start "" explorer.exe "%CD%\installer_output"
pause
exit /b 0

:find_python
set "PY_EXE="
where py >nul 2>&1
if not errorlevel 1 (
    py -3 -c "import sys; print(sys.executable)" > "%TEMP%\aoh2_py_path.txt" 2>nul
    if not errorlevel 1 (
        set /p PY_EXE=<"%TEMP%\aoh2_py_path.txt"
        del /q "%TEMP%\aoh2_py_path.txt" >nul 2>&1
        if defined PY_EXE exit /b 0
    )
)
where python >nul 2>&1
if not errorlevel 1 (
    for /f "delims=" %%P in ('python -c "import sys; print(sys.executable)" 2^>nul') do set "PY_EXE=%%P"
    if defined PY_EXE exit /b 0
)
exit /b 0

:install_python
 echo.
echo [INFO] Python bulunamadi. Python otomatik kuruluyor...
where winget >nul 2>&1
if not errorlevel 1 (
    winget install -e --id Python.Python.3.14 --scope user --silent --accept-package-agreements --accept-source-agreements
    if not errorlevel 1 (
        set "PATH=%LOCALAPPDATA%\Programs\Python\Python314;%LOCALAPPDATA%\Programs\Python\Python314\Scripts;%PATH%"
        exit /b 0
    )
)

rem winget yoksa python.org kurulum paketini PowerShell ile indirip sessizce kur.
set "PY_INSTALLER=%TEMP%\python-aoh2bot-installer.exe"
powershell -NoProfile -ExecutionPolicy Bypass -Command "$ProgressPreference='SilentlyContinue'; Invoke-WebRequest -UseBasicParsing -Uri 'https://www.python.org/ftp/python/3.14.0/python-3.14.0-amd64.exe' -OutFile '%PY_INSTALLER%'"
if errorlevel 1 (
    echo [HATA] Python otomatik olarak indirilemedi.
    exit /b 1
)
"%PY_INSTALLER%" /quiet InstallAllUsers=0 PrependPath=1 Include_test=0 Include_pip=1
if errorlevel 1 (
    del /q "%PY_INSTALLER%" >nul 2>&1
    echo [HATA] Python kurulumu basarisiz.
    exit /b 1
)
del /q "%PY_INSTALLER%" >nul 2>&1
set "PATH=%LOCALAPPDATA%\Programs\Python\Python314;%LOCALAPPDATA%\Programs\Python\Python314\Scripts;%PATH%"
exit /b 0

:find_iscc
set "ISCC="
if exist "%ProgramFiles(x86)%\Inno Setup 6\ISCC.exe" set "ISCC=%ProgramFiles(x86)%\Inno Setup 6\ISCC.exe"
if not defined ISCC if exist "%ProgramFiles%\Inno Setup 6\ISCC.exe" set "ISCC=%ProgramFiles%\Inno Setup 6\ISCC.exe"
exit /b 0

:install_inno
where winget >nul 2>&1
if not errorlevel 1 (
    winget install -e --id JRSoftware.InnoSetup --silent --accept-package-agreements --accept-source-agreements
    if not errorlevel 1 exit /b 0
)

set "INNO_INSTALLER=%TEMP%\innosetup-aoh2bot.exe"
powershell -NoProfile -ExecutionPolicy Bypass -Command "$ProgressPreference='SilentlyContinue'; Invoke-WebRequest -UseBasicParsing -Uri 'https://jrsoftware.org/download.php/is.exe' -OutFile '%INNO_INSTALLER%'"
if errorlevel 1 (
    echo [HATA] Inno Setup otomatik olarak indirilemedi.
    exit /b 1
)
"%INNO_INSTALLER%" /VERYSILENT /SUPPRESSMSGBOXES /NORESTART /SP-
if errorlevel 1 (
    del /q "%INNO_INSTALLER%" >nul 2>&1
    echo [HATA] Inno Setup kurulumu basarisiz.
    exit /b 1
)
del /q "%INNO_INSTALLER%" >nul 2>&1
exit /b 0

:error
echo.
echo ============================================
echo   BUILD BASARISIZ
 echo ============================================
echo Yukaridaki hata mesajini kontrol edin.
echo.
pause
exit /b 1
