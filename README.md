# Simple Keylogger

## PRODIGY_CS_04

A basic keylogger script developed as part of the Prodigy Internship program. This tool captures and logs keystrokes to a file with timestamps, demonstrating event-driven programming in Python.

### Features
- Logs all key presses with timestamps
- Handles special keys (e.g., space, enter, shift)
- Stops logging when the ESC key is pressed
- Saves logs to `log.txt` in the same directory
- Includes error handling for file operations
- Type-annotated code for better maintainability

### Requirements
- Python 3.6 or higher
- `pynput` library

### Installation
1. Ensure Python is installed on your system.
2. Install the required library:
   ```
   pip install pynput
   ```

### Usage
1. Run the script:
   ```
   python keylogger.py
   ```
2. The keylogger will start listening for keystrokes.
3. Press the ESC key to stop and save the session.
4. Check `log.txt` for the logged keystrokes.

### How it Works
- Uses the `pynput` library to monitor keyboard events.
- `on_press` callback handles key press events, distinguishing between character keys and special keys.
- `on_release` callback checks for the ESC key to terminate the listener.
- Logs are written to `log.txt` with timestamps in the format `[DD-MM-YYYY, HH:MM:SS]`.

### Knowledge Gained
- Event-driven programming with callbacks
- Handling keyboard input in Python
- File I/O operations with error handling
- Type annotations for code clarity
- Basic security considerations for input monitoring tools

### Disclaimer
This tool is for educational purposes only. Keyloggers can be misused and may violate privacy laws. Use responsibly and ensure compliance with local regulations. Do not use for unauthorized monitoring.
