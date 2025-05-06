import os
import logging
from datetime import datetime
from pynput import keyboard, mouse
import pygetwindow as gw

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
    try:
        active_window = gw.getActiveWindow()
        return active_window.title if active_window else "No active window"
    except Exception as e:
        return f"Error getting active window: {e}"

def on_click(x, y, button, pressed):
    if pressed:
        active_window = log_active_window()
        logging.info(f"Mouse clicked at ({x}, {y}) in '{active_window}'")

def on_press(key):
    active_window = log_active_window()
    logging.info(f"Key {key!r} pressed in '{active_window}'")

if __name__ == "__main__":
    # Start listening to mouse and keyboard events
    with mouse.Listener(on_click=on_click) as mouse_listener, \
         keyboard.Listener(on_press=on_press) as keyboard_listener:
        mouse_listener.join()
        keyboard_listener.join()