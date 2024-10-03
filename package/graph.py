import os
import subprocess
import sys
from datetime import datetime
import shutil


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
        base_dir = os.path.dirname(__file__)
        snippet_path = os.path.join(base_dir, "stash", f"{snippet_name}.py")
        output_path = os.path.join(base_dir, f"{snippet_name}.py")
        shutil.copyfile(snippet_path, output_path)
    except Exception as e:
        print(f"Syntax Error: {e}")


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
