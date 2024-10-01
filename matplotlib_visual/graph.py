import os
import subprocess
import sys

def display(snippet_name):
    snippet_path = os.path.join(
        os.path.dirname(__file__), "code_snippets", f"{snippet_name}.py"
    )

    with open(snippet_path, "r") as file:
        source_code = file.read()

    # Function to copy text to clipboard based on platform
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

        #macOS
        elif "darwin" in sys.platform:
            subprocess.run(
                ["pbcopy"],
                input=text.strip().encode(),
                check=True,
            )
        else:
            raise OSError("Unsupported operating system")


        else:
            raise OSError("Unsupported operating system")

    print(source_code)
    copy_to_clipboard(source_code)
