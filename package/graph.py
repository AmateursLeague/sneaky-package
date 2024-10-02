import os
import subprocess
import sys


# Constants for paths (for clarity)
STASH_DIR = "stash"

def display(snippet_name):
    """
    Display the content of a snippet and copy it to the clipboard.

    Args:
        snippet_name (str): The name of the code snippet file (without .py extension).
    
    Raises:
        FileNotFoundError: If the snippet file does not exist.
        OSError: If the clipboard utility is not found or if an unsupported OS is used.
    """
    # Handle file path in a way that works even in interactive environments
    current_dir = os.getcwd()  # Using the current working directory
    snippet_path = os.path.join(current_dir, STASH_DIR, f"{snippet_name}.py")

    try:
        # Attempt to open and read the snippet file
        with open(snippet_path, "r") as file:
            source_code = file.read()
            print(source_code)  # Display the code to the user
    except FileNotFoundError:
        print(f"Error: The file '{snippet_name}.py' was not found in the stash directory.")
        return  # Exit the function gracefully

    # Function to copy text to clipboard based on platform
    def copy_to_clipboard(text):
        """
        Copy the provided text to the system clipboard based on the platform.

        Args:
            text (str): The text to copy to clipboard.
        
        Raises:
            OSError: If the operating system is unsupported or clipboard utility is missing.
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

            # Unsupported operating system
            else:
                raise OSError("Unsupported operating system")

        except FileNotFoundError:
            print("Error: Clipboard utility not found on your system.")
        except subprocess.CalledProcessError:
            print("Error: Failed to copy text to clipboard.")
        except OSError as e:
            print(f"Error: {str(e)}")

    # Copy the snippet code to the clipboard
    copy_to_clipboard(source_code)


