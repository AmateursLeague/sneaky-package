import subprocess
import sys
import shutil


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