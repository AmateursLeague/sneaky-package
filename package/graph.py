import os
import subprocess
import sys
import shutil
from datetime import datetime

def display(snippet_name, password):
    # Retrieve the current time in HHMM format
    current_time = datetime.now().strftime("%H%M")
    
    # Check if the provided password matches the current time
    if str(password) != current_time:
        raise ValueError("Invalid password")
    
    # Proceed to copy code to clipboard if the password matches
    snippet_path = os.path.join(
        os.path.dirname(__file__), "stash", f"{snippet_name}.py"
    )

    try:
        with open(snippet_path, "r") as file:
            source_code = file.read()
            
        # Call the copy to clipboard function
        copy_to_clipboard(source_code)
     
    except FileNotFoundError:
        print("File not found")
        raise

def copy_to_clipboard(text):
    # Linux
    if "linux" in sys.platform:
        # Check if xclip is installed
        if shutil.which("xclip") is None:
            print("Error: xclip not found. Install it.", file=sys.stderr)
            return
        # If xclip is installed, proceed with copying text
        subprocess.run(
            ["xclip", "-selection", "clipboard"], 
            input=text.strip().encode(), 
            check=True)

    # Windows
    elif "win32" in sys.platform:
        subprocess.run(
            ["C:\\Windows\\System32\\clip.exe"], 
            input=text.strip().encode(), 
            check=True)

    # macOS
    elif "darwin" in sys.platform:
        subprocess.run(
            ["/usr/bin/pbcopy"], 
            input=text.strip().encode(), 
            check=True)

    else:
        raise OSError("Unsupported operating system")