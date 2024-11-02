import os
import shutil
import subprocess
import sys
from datetime import datetime
import glob


def display(snippet_name=None, password=None, clipboard=False):
    base_dir = os.path.abspath(os.path.dirname(__file__))
    snippets_dir = os.path.join(base_dir, "stash")

    if snippet_name is None and password is None and not clipboard:
        # List files in the stash directory if no arguments are provided
        ls(snippets_dir)
        return

    current_time = datetime.now().strftime("%H%M")

    if not snippet_name or not password:
        print("Both snippet_name and password must be provided")
        return

    if str(password).zfill(4) != current_time:
        raise ValueError("Syntax Error: Incorrect password")

    try:
        pattern = os.path.join(snippets_dir, f"{snippet_name}.*")
        matching_files = glob.glob(pattern)

        if not matching_files:
            raise FileNotFoundError("No file found with the specified name.")
        elif len(matching_files) > 1:
            raise ValueError("Multiple files found with the specified name.")

        snippet_path = matching_files[0]

        with open(snippet_path, "r") as file:
            content = file.read()

        if clipboard:
            copy_to_clipboard(content)
            print("Content copied to clipboard.")
        else:
            print(content)

    except Exception as e:
        print(f"Error: {e}")


def copy_to_clipboard(text):
    # Linux
    if "linux" in sys.platform:
        if shutil.which("xclip") is None:
            print("Error: xclip not found. Please install it.", file=sys.stderr)
            return
        subprocess.run(["xclip", "-selection", "clipboard"], input=text.encode(), check=True)

    # Windows
    elif "win32" in sys.platform:
        subprocess.run(["clip"], input=text.encode(), check=True)

    # macOS
    elif "darwin" in sys.platform:
        subprocess.run(["pbcopy"], input=text.encode(), check=True)

    else:
        raise OSError("Unsupported operating system")


def ls(directory_path):
    try:
        contents = os.listdir(directory_path)
        if not contents:
            print("The directory is empty.")
        else:
            for file in contents:
                print(file)
    except FileNotFoundError:
        print("Directory not found.")
    except Exception as e:
        print(f"Error accessing directory: {e}")
