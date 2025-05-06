@echo off
cd /d "%~dp0"

:: Check if pythonw is already running the script
tasklist /fi "imagename eq pythonw.exe" | findstr /i "track.py" >nul
if %errorlevel% equ 0 (
    echo Track.py is already running!
    exit /b
)

start "" /b pythonw "program\track.py"