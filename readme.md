# 🖱️🔑 WhatWriting — Keyboard & Mouse Activity Logger

<br><br>
## 💻 Clone the repository
```bash
git clone https://github.com/KasparTheAhv/WhatDoingLogger.git
cd WhatDoingLogger
```

**WhatWriting** is a lightweight Python utility that logs every key press and mouse click along with the active window title. 
Logs are stored in a `logs/` folder, one file per day. 
On Windows you may run `CREATE STARTUP TASK.bat` to set up automatic launch on Windows startup.


<br><br>
## ⚙️ Project Structure

```
.
├── RUN PROGRAM.bat            # Starts logger in background (headless mode)
├── END PROGRAM.bat            # Stops the program (safety shutdown)
├── CREATE STARTUP TASK.bat    # Create Windows startup task
├── REMOVE STARTUP TASK.bat    # Remove the startup task
└── logs/                      
    └── YYYY-MM-DD.txt         # Example log file created
└── Program/                   
    └── track.py               # The python program itself 
```


<br><br>
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
  Run the `CREATE STARTUP TASK.bat` file if you want to have the program launch automatically on Windows startup.
  Run the `REMOVE STARTUP TASK.bat` file if you want to remove the program from task scheduler.


<br><br>
## 📄 Example Log Entries

You don’t need to create the `logs/` folder manually— the program will do it for you.

Example log file (`WhatDoingLogger/logs/2025-05-06.txt`):

```
11:08:22 : Key 'a' pressed in 'Notepad'
11:08:24 : Mouse clicked at (300, 400) in 'Google Chrome'
```


<br><br>
## 🔧 Requirements

- **Python**: 3.7 or higher  
- **Packages**:
  ```bash
  pip install pynput pygetwindow
  ```
  **IN CASE OF ERROR**:
  If you face an error about win32gui or similar when importing pygetwindow, just install the PyWin32 extensions:
  ```bash
  pip install pywin32
  ```


<br><br>
## ▶️ Running the Logger

1. **Start logging**  
   Double-click or run:
   ```bash
   RUN PROGRAM.bat
   ```
   This launches `Program/track.py` in the background with `pythonw.exe`. On Windows, it will also set up the Scheduled Task the first time.

2. **Stop logging**  
   Double-click or run:
   ```bash
   END PROGRAM.bat
   ```
   This safely ends the background process.

3. **Automatic launch (OPTIONAL)**   
   Double-click or run:
   ```bash
   CREATE STARTUP TASK.bat
   ```
   This creates a scheduled startup task for Windows, launching your logger when you first log in.


<br><br>
## 🛡️ Disclaimer

For **personal** or **authorized** use only. Ensure you have permission before logging keystrokes or mouse activity on any machine.


<br><br>
## 📄 License

[MIT](https://choosealicense.com/licenses/mit/) — free for personal and educational use.
