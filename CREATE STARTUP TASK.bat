@echo off
:: Check for admin rights
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\_elevate.vbs"
    echo UAC.ShellExecute "cmd.exe", "/c ""%~f0""", "", "runas", 1 >> "%temp%\_elevate.vbs"
    cscript //nologo "%temp%\_elevate.vbs"
    del "%temp%\_elevate.vbs"
    exit /b
)

:: === SETUP VARIABLES ===
set "TASK_NAME=WhatWritingLogger"
set "PYTHONW=%LocalAppData%\Programs\Python\Python312\pythonw.exe"
set "SCRIPT=%~dp0program\track.py"

:: === CREATE SCHEDULED TASK ===
schtasks /Create ^
 /TN "%TASK_NAME%" ^
 /TR "\"%PYTHONW%\" \"%SCRIPT%\"" ^
 /SC ONLOGON ^
 /RL HIGHEST ^
 /F

echo.
echo ✅ Scheduled Task "%TASK_NAME%" created successfully!
exit
