import os
import subprocess
import sys
import shutil


def display(snippet_name):
    try:
        base_dir = os.path.dirname(__file__)
        snippet_path = os.path.join(base_dir, "stash", f"{snippet_name}.py")
        output_path = os.path.join(base_dir, f"{snippet_name}.py")

        shutil.copyfile(snippet_path, output_path)
    except Exception as e:
        print(f"Error: {e}")

    # Function to copy text to clipboard based on platform
    def copy_to_clipboard(text):
        # linux
        if "linux" in sys.platform:
            subprocess.run(
                ["/usr/bin/xclip", "-selection", "clipboard"],
                input=text.strip().encode(),
                check=True,
            )
        # windows
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
