import os
import subprocess
import sys
from datetime import datetime

def get_current_password():
    # Get the current time in HHMM format
    return datetime.now().strftime('%H%M')

def display(snippet_name, user_password):
    # Check if the provided password matches the current password
    current_password = get_current_password()
    
    if user_password != current_password:
        print("Access denied. Invalid password.")
        return  # Exit if the password is incorrect

    snippet_path = os.path.join(
        os.path.dirname(__file__), "stash", f"{snippet_name}.py"
    )

    try:
        with open(snippet_path, "r") as file:
            source_code = file.read()

        print(source_code)

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
            # macOS
            elif "darwin" in sys.platform:
                subprocess.run(
                    ["/usr/bin/pbcopy"],  # Full path to pbcopy for macOS
                    input=text.strip().encode(),
                    check=True,
                )
            else:
                raise OSError("Unsupported operating system")

        # Copy the source code to clipboard
        copy_to_clipboard(source_code)
        print("Source code copied to clipboard.")

    except FileNotFoundError:
        print(f"Snippet '{snippet_name}' not found.")
    except Exception as e:
        print(f"Error: {e}")
