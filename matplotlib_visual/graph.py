import os
import subprocess
import sys

def display(snippet_name):
    snippet_path = os.path.join(
        os.path.dirname(__file__), "code_snippets", f"{snippet_name}.py"
    )

    with open(snippet_path, "r") as file:
        source_code = file.read()

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
                ["/usr/bin/pbcopy"],
                input=text.strip().encode(),
                check=True,
            )
        else:
            raise OSError("Unsupported operating system")

    print(source_code)
    copy_to_clipboard(source_code)
