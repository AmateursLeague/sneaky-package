import os
import subprocess
import sys
import shutil
from datetime import datetime
import glob


def display(snippet_name, password):
    # Check if the current time matches the provided password
    current_time = datetime.now().strftime("%H%M")
    if str(password).zfill(4) != current_time:
        raise ValueError("Invalid password")

    # Base directory adjustment for when __file__ is unavailable
    try:
        base_dir = os.path.abspath(os.path.dirname(__file__))
    except NameError:
        base_dir = os.getcwd()
        
    snippets_dir = os.path.join(base_dir, "stash")
    pattern = os.path.join(snippets_dir, f"{snippet_name}.*")
    matching_files = glob.glob(pattern)

    if not matching_files:
        raise FileNotFoundError("No file found with the name.")
    elif len(matching_files) > 1:
        raise ValueError("Multiple files found with the given name.")

    snippet_path = matching_files[0]

    try:
        with open(snippet_path, "r") as file:
            source_code = file.read()

        # Call the function to copy the text to clipboard
        copy_to_clipboard(source_code)
        print("Snippet copied to clipboard successfully.")

    except FileNotFoundError:
        print("File not found.")
        raise


def copy_to_clipboard(text):
    """Copies text to the clipboard depending on the operating system."""
    text = text.strip()

    # Linux
    if "linux" in sys.platform:
        # Check if xclip is installed
        if shutil.which("xclip") is None:
            print("Error: xclip not found. Install it.", file=sys.stderr)
            return
        subprocess.run(
            ["xclip", "-selection", "clipboard"],
            input=text.encode(),
            check=True,
        )

    # Windows
    elif "win32" in sys.platform:
        subprocess.run(
            ["clip"], input=text.encode(), check=True
        )

    # macOS
    elif "darwin" in sys.platform:
        subprocess.run(["pbcopy"], input=text.encode(), check=True)

    else:
        raise OSError("Unsupported operating system")
