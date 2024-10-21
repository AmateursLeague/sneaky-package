import os
import subprocess
import sys
import shutil
from datetime import datetime
import glob

def display(snippet_name, password):
    """
    This function displays the content of a snippet file and copies it to the clipboard.
    It first checks if the provided password matches the current time in HHMM format.
    If the password is valid, it searches for a file with the given snippet_name in the "stash" directory.
    If a single file is found, it reads the file content and calls the copy_to_clipboard function to copy the content.
    """
    current_time = datetime.now().strftime("%H%M")
    
    if int(password) != int(current_time):
        raise ValueError("Invalid password")
    
    base_dir = os.path.dirname(__file__)
    snippets_dir = os.path.join(base_dir, "stash")
    pattern = os.path.join(snippets_dir, f"{snippet_name}.*")

    matching_files = glob.glob(pattern)
    
    if not matching_files:
        raise FileNotFoundError(f"No file found with the name.")
    elif len(matching_files) > 1:
        raise ValueError("Multiple files found with the given name.")
    
    snippet_path = os.path.join(snippets_dir, matching_files[0])

    try:
        with open(snippet_path, "r") as file:
            source_code = file.read()
            
        # Call the copy to clipboard function
        copy_to_clipboard(source_code)
     
    except FileNotFoundError:
        print("File not found")
        raise

def copy_to_clipboard(text):
    """
    This function copies the given text to the clipboard based on the operating system.
    It supports Linux, Windows, and macOS.
    """
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

