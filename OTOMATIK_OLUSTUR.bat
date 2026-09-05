@echo off
setlocal
title Age Of History 2 Bot - Professional Builder
cd /d "%~dp0"

echo.
echo Age Of History 2 Bot otomatik olusturucu baslatiliyor...
echo Gerekirse UAC izni istenecek.
echo.

powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0otomatik_olustur.ps1"
if errorlevel 1 (
    echo.
    echo ISLEM BASARISIZ.
    pause
    exit /b 1
)
exit /b 0
