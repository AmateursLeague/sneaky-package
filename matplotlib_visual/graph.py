import os
import subprocess
import sys


def display(snippet_name):
    """
    Displays the contents of a Python code snippet file and copies the source code
    to the clipboard based on the operating system.

    Parameters:
    snippet_name (str): The name of the code snippet file (without .py extension)
                        to display and copy.

    Raises:
    OSError: If the operating system is unsupported for copying to the clipboard.
    """
    snippet_path = os.path.join(
        os.path.dirname(__file__), "code_snippets", f"{snippet_name}.py"
    )

    with open(snippet_path, "r") as file:
        source_code = file.read()

    def copy_to_clipboard(text):
        """
        Copies the provided text to the clipboard based on the operating system.

        Parameters:
        text (str): The text to copy to the clipboard.

        Raises:
        OSError: If the operating system is unsupported for copying to the clipboard.
        """
        if "linux" in sys.platform:
            subprocess.run(
                ["/usr/bin/xclip", "-selection", "clipboard"],
                input=text.strip().encode(),
                check=True,
            )
        elif "win32" in sys.platform:
            subprocess.run(
                ["C:\\Windows\\System32\\clip.exe"],
                input=text.strip().encode(),
                check=True,
            )
        elif "darwin" in sys.platform:
            subprocess.run(
                ["/usr/bin/pbcopy"],  # Full path to pbcopy
                input=text.strip().encode(),
                check=True,
            )
        else:
            raise OSError("Unsupported operating system")

    print(source_code)
    copy_to_clipboard(source_code)
