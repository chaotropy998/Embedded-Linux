import pyperclip as pc
import keyboard
import os

file_path = "notes.txt"

def export_clipboard_data():
    clipboard_data = pc.paste()

    # Create the notes.txt file if it doesn't exist
    if not os.path.exists(file_path):
        with open(file_path, "w"):
            pass

    # Append clipboard_data to the notes.txt file
    with open(file_path, "a+") as file:
        file.write(clipboard_data + "\n")
    
# Register the hotkey
keyboard.add_hotkey("alt+shift+s", export_clipboard_data)

# Keep the script running
keyboard.wait()