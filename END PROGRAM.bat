@echo off
echo Attempting to kill all pythonw.exe processes...

powershell -NoProfile -Command "Get-CimInstance Win32_Process | Where-Object { $_.Name -eq 'pythonw.exe' } | ForEach-Object { try { Stop-Process -Id $_.ProcessId -Force -ErrorAction Stop } catch { Write-Host \"Failed to stop PID $($_.ProcessId): $_\" } }"

echo Done.
pause