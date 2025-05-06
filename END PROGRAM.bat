@echo off
echo Searching for track.py process...
powershell -Command "Get-CimInstance Win32_Process | Where-Object { $_.CommandLine -match 'track.py' } | ForEach-Object { Stop-Process -Id $_.ProcessId -Force }"
exit