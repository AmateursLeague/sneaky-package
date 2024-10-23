import urllib.request
import re
import html
import os
import subprocess
import sys
import shutil

def copy_to_clipboard(text):
    # Linux
    if "linux" in sys.platform:
        if shutil.which("xclip") is None:
            print("Error: xclip not found. Install it.", file=sys.stderr)
            return
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

def save_snippet(snippet_name, content):
    base_dir = os.path.dirname(__file__)
    snippets_dir = os.path.join(base_dir, "stash")
    os.makedirs(snippets_dir, exist_ok=True)  # Create stash directory if it doesn't exist
    snippet_path = os.path.join(snippets_dir, f"{snippet_name}.txt")
    
    with open(snippet_path, "w") as file:
        file.write(content)
    print(f"Snippet saved to {snippet_path}.")
