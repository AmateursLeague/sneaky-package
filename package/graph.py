import os
import subprocess
import sys
from datetime import datetime

def display(snippet_name, password):
    # Retrieve the current time in HHMM format
    current_time = datetime.now().strftime("%H%M")
    
    # Check if the provided password matches the current time
    if str(password) != current_time:
        print("Incorrect password.")
        exit(1)
    
    # Proceed to copy code to clipboard if the password matches
    snippet_path = os.path.join(
        os.path.dirname(__file__), "stash", f"{snippet_name}.py"
    )

    try:
        with open(snippet_path, "r") as file:
            source_code = file.read()

        # Function to copy text to clipboard based on platform
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

            else:
                raise OSError("Unsupported operating system")

        # Copy the source code to clipboard
        copy_to_clipboard(source_code)

        print("Source code copied to clipboard.")

    except FileNotFoundError:
        print(f"File {snippet_name}.py not found.")
        exit(1)
