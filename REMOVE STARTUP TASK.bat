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

:: === DELETE SCHEDULED TASK ===
schtasks /Delete /TN "WhatWritingLogger" /F

echo.
echo ❌ Scheduled Task "WhatWritingLogger" has been removed!
exit