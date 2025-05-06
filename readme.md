# 🖱️🔑 WhatWriting — Keyboard & Mouse Activity Logger

## 💻 Clone the repository
```bash
git clone https://github.com/KasparTheAhv/WhatDoingLogger.git
cd WhatDoingLogger
```

**WhatWriting** is a lightweight Python utility that logs every key press and mouse click along with the active window title. Logs are stored in a `logs/` folder, one file per day, and each entry records only the time (no date or milliseconds). On Windows it can optionally register itself to start automatically at user logon via a Scheduled Task.

## ⚙️ Project Structure

```
.
├── track.py             # Main logger script (also registers scheduled task on Windows)
├── RUNLOGGING.bat       # Starts logger in background (headless mode)
├── ENDMYSAFETY.bat      # Stops all Python background processes (safety shutdown)
└── logs/                # Automatically created on first run
    └── YYYY-MM-DD.txt   # Today’s log file (e.g. 2025-05-06.txt)
```

## 🚀 How It Works

- **Automatic logs folder**  
  On launch, the script creates a `logs/` directory in the same folder.
- **Daily files**  
  Creates (or appends to) `logs/YYYY-MM-DD.txt` based on the current date.
- **Time-only entries**  
  Logs each event with `HH:MM:SS : <message>`—hours/minutes/seconds of the day.
- **Silent background mode**  
  Designed to run via `pythonw.exe` so no console window appears.
- **Windows Scheduled Task**  
  If running on Windows (`os.name == 'nt'`), on startup the script will automatically create or update a Scheduled Task named **WhatWritingLogger** that launches itself at user logon (using `schtasks /Create … /F`). This ensures one and only one task exists, and it will be overwritten on subsequent runs to keep the path up to date.

### Example Log Entries

```
11:08:22 : Key 'a' pressed in 'Notepad'
11:08:24 : Mouse clicked at (300, 400) in 'Google Chrome'
```

## 🔧 Requirements

- **Python**: 3.7 or higher  
- **Packages**:
  ```bash
  pip install pynput pygetwindow
  ```
  **Optional**:
  If you ever see an error about win32gui or similar when importing pygetwindow, just install the PyWin32 extensions:
  ```bash
  pip install pywin32
  ```

## ▶️ Running the Logger

1. **Start logging**  
   Double-click or run:
   ```bash
   RUNLOGGING.bat
   ```
   This launches `track.py` in the background with `pythonw.exe`. On Windows, it will also set up the Scheduled Task the first time.

2. **Stop logging**  
   To safely terminate all background Python (`pythonw.exe`) instances:
   ```bash
   ENDMYSAFETY.bat
   ```
   > ⚠️ *Warning:* This kills _all_ `pythonw.exe` processes—use with caution.

## 📁 Output

All events are appended to:
```
<project-root>/logs/YYYY-MM-DD.txt
```
(e.g. `WhatDoingLogger/logs/2025-05-06.txt`)

You don’t need to create the `logs/` folder manually—`track.py` will do it for you. The Windows task will also manage auto-start.

## 🛡️ Disclaimer

For **personal** or **authorized** use only. Ensure you have permission before logging keystrokes or mouse activity on any machine.

## 📄 License

[MIT](https://choosealicense.com/licenses/mit/) — free for personal and educational use.
