import os
import subprocess
import sys
import getpass

PASSWORD = "<password_of_your_choice>"  # Replace with your password


def check_password():
    entered_password = getpass.getpass("Enter the password: ")
    if entered_password != PASSWORD:
        print("Incorrect password. Access denied.")
        sys.exit(1)
        

def display(snippet_name):
    check_password()  # Check password before proceeding
    
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

        # macOS
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
