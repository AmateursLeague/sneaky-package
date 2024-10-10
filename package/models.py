import os
import shutil
import subprocess
import sys

def display(snippet_name, password, clipboard=None):
    try:
        base_dir = os.path.dirname(__file__)
        snippet_path = os.path.join(base_dir, "stash", f"{snippet_name}.py")
        output_path = os.path.join(base_dir, f"{snippet_name}.py")

        # If clipboard argument is passed as 1, copy content to clipboard
        if clipboard == 1:
            with open(snippet_path, 'r') as file:
                content = file.read()
            copy_to_clipboard(content)
            print("Content copied to clipboard.")
        else:
            # Regular
            shutil.copyfile(snippet_path, output_path)

    except Exception as e:
        print(f"Syntax Error: {e}")

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
