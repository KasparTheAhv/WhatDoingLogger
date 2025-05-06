# 🖱️🔑 WhatWriting — Keyboard & Mouse Activity Logger

## 💻 Clone the repository with:
> ```bash
> git clone https://github.com/KasparTheAhv/WhatDoingLogger.git
> ```

**WhatWriting** is a simple Python-based utility that logs keyboard and mouse activity, along with the active window title at the time of interaction. It is useful for personal productivity tracking, usability testing, or development of attention-focused tools.

## ⚙️ Project Structure

```
.
├── track.py             # Main logger script
├── RUNLOGGING.bat       # Starts logger in background (headless mode)
├── ENDMYSAFETY.bat      # Stops all Python background processes (safety shutdown)
└── mistekst.txt         # Output log file (created automatically in C:/Drivers/WhatWriting/)
```

## 🚀 How It Works

- Logs every key press and mouse click.
- Captures the name of the currently active window.
- Saves the log to `C:/Drivers/WhatWriting/mistekst.txt`.
- Designed to run silently in the background using `pythonw.exe`.

### Example Log Entry
```
2025-05-04 12:23:45,123: Key 'a' pressed in 'Notepad'
2025-05-04 12:23:46,456: Mouse clicked at (300, 400) in 'Google Chrome'
```

## 🔧 Requirements

- Python 3.7+
- Required packages:
  ```
  pip install pynput pygetwindow
  ```

## ▶️ Running the Logger

1. **Start logging:**  
   Run `RUNLOGGING.bat` to start `track.py` in the background.
   ```
   RUNLOGGING.bat
   ```

2. **Stop logging:**  
   Use `ENDMYSAFETY.bat` to terminate all background Python (`pythonw.exe`) processes.
   ```
   ENDMYSAFETY.bat
   ```

> **⚠️ Warning:** `ENDMYSAFETY.bat` force-kills all `pythonw.exe` processes. Be cautious if you have other background Python apps running.

## 📁 Output

Logs are saved in:
```
C:/Drivers/WhatWriting/mistekst.txt
```

Make sure the folder exists before running the logger, or modify `track.py` to create it if needed.

## 🛡️ Disclaimer

This tool is for personal or authorized testing use only. Do not deploy or run it on systems without the knowledge and consent of the user. Unauthorized logging of input devices may be illegal in many jurisdictions.

## 📄 License

[MIT](https://choosealicense.com/licenses/mit/) — free for personal and educational use. 