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

:: === CREATE SCHEDULED TASK ===
schtasks /Create ^
 /TN "WhatWritingLogger" ^
 /TR "cmd /c \"\"%~dp0RUN PROGRAM.bat\"\"" ^
 /SC ONLOGON ^
 /F

echo.
echo ✅ Scheduled Task "WhatWritingLogger" created successfully!
exit