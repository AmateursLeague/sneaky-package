import os
import shutil
import subprocess
import sys
from package.password import valid_password

def display_or_copy_snippet(snippet_name, password, action):
    if not isinstance(password, int) or not valid_password(password):
        raise ValueError("Incorrect password")

    base_dir = os.path.dirname(__file__)
    snippets_dir = os.path.join(base_dir, "stash")
    
    try:
        snippet_path = os.path.join(snippets_dir, snippet_name)
        with open(snippet_path, "r") as file:
            content = file.read()
        
        if action == "display":
            print(content)
        elif action == "copy":
            copy_to_clipboard(content)
            print("Snippet copied to clipboard.")
    except FileNotFoundError:
        print("Error: No file found with the specified name.")
    except Exception as e:
        print(f"Error: {e}")


def show(snippet_name=None, password=None):
    if snippet_name is None and password is None:
        base_dir = os.path.dirname(__file__)
        snippets_dir = os.path.join(base_dir, "stash")
        list_snippets(snippets_dir)
        return

    display_or_copy_snippet(snippet_name, password, action="display")


def clip(snippet_name, password):
    display_or_copy_snippet(snippet_name, password, action="copy")

def write(snippet_name, password):
    if not isinstance(password, int) or not valid_password(password):
        raise ValueError("Incorrect password")

    base_dir = os.path.dirname(__file__)
    snippets_dir = os.path.join(base_dir, "stash")
    
    try:
        snippet_path = os.path.join(snippets_dir, snippet_name)
        output_path = os.path.join(base_dir, snippet_name)

        shutil.copyfile(snippet_path, output_path)
        print(f"File '{snippet_path}' copied successfully to '{output_path}'.")
    except FileNotFoundError:
        print("Error: No file found with the specified name.")
    except Exception as e:
        print(f"Error: {e}")


def copy_to_clipboard(text):
    try:
        if "linux" in sys.platform:
            if shutil.which("xclip") is None:
                raise RuntimeError("xclip not found. Install it.")
            subprocess.run(["xclip", "-selection", "clipboard"], input=text.strip().encode(), check=True)

        elif "win32" in sys.platform:
            subprocess.run(["C:\\Windows\\System32\\clip.exe"], input=text.strip().encode(), check=True)

        elif "darwin" in sys.platform:
            subprocess.run(["/usr/bin/pbcopy"], input=text.strip().encode(), check=True)

        else:
            raise OSError("Unsupported operating system")
    except subprocess.CalledProcessError:
        print("Error: Failed to copy to clipboard.")


def list_snippets(snippets_dir):
    try:
        contents = os.listdir(snippets_dir)
        for file in contents:
            print(file)
    except FileNotFoundError:
        print("Error: Stash directory not found.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    pass
