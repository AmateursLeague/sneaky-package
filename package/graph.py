import os
import subprocess
import sys


def display(snippet_name):
    """
    Display the content of the snippet file and copy it to the clipboard.

    Args:
        snippet_name (str): Name of the code snippet (without extension).
    """
    snippet_path = os.path.join(
        os.path.dirname(__file__), "stash", f"{snippet_name}.py"
    )

    try:
        with open(snippet_path, "r") as file:
            source_code = file.read()
    except FileNotFoundError:
        print(f"Error: {snippet_name}.py not found in stash directory.")
        return

    # Function to copy text to clipboard based on platform
    def copy_to_clipboard(text):
        """
        Copy the given text to the system clipboard.

        Args:
            text (str): Text to be copied to the clipboard.
        """
        try:
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

            else:
                raise OSError("Unsupported operating system")

        except FileNotFoundError:
            print("Error: Clipboard utility not found. Cannot copy to clipboard.")
        except subprocess.CalledProcessError as e:
            print(f"Error during clipboard copying: {e}")

    # Copy the source code to clipboard
    copy_to_clipboard(source_code)

    # Display the snippet's content
    print(source_code)
