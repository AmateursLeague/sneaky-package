import os
import subprocess
import sys
from datetime import datetime


def copy_to_clipboard(text):
    # Linux
    if "linux" in sys.platform:
        subprocess.run(
            ["/usr/bin/xclip", "-selection", "clipboard"],
            input=text.strip().encode(),
            check=True,
        )
    # Windows
    elif "win32" in sys.platform:
        subprocess.run(
            ["C:\\Windows\\System32\\clip.exe"],
            input=text.strip().encode(),
            check=True,
        )
    #macOS
    elif "darwin" in sys.platform:
        subprocess.run(
            ["/usr/bin/pbcopy"],  # Full path to pbcopy for macOS
            input=text.strip().encode(),
            check=True,
        )
    else:
        raise OSError("Unsupported operating system")


def display(snippet_name, password):
    # Retrieve the current time in HHMM format
    current_time = datetime.now().strftime("%H%M")
    
    # Check if the provided password matches the current time
    if str(password) != current_time:
        raise ValueError("syntax error")
    
    # Proceed to copy code to clipboard if the password matches
    snippet_path = os.path.join(
        os.path.dirname(__file__), "stash", f"{snippet_name}.py"
    )

    try:
        with open(snippet_path, "r") as file:
            source_code = file.read()

        # Copy the source code to clipboard
        copy_to_clipboard(source_code)

    except FileNotFoundError:
        print("syntax error")
        raise

