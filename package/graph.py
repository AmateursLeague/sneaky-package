import os
import subprocess
import sys
from datetime import datetime


def copy_to_clipboard(text):
    """
    Copies the provided text to the clipboard.
    
    Args:
        text (str): The text to copy to the clipboard.

    Raises:
        OSError: If the operating system is unsupported.
    """
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
    else:
        raise OSError("Unsupported operating system")


def display(snippet_name, password):
    """
    Displays the source code and copies it to the clipboard if the password is correct.

    Args:
        snippet_name (str): Name of the snippet file to copy.
        password (int): Password based on the current time.

    Raises:
        ValueError: If the password is incorrect.
        FileNotFoundError: If the snippet file is not found.
    """
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

