import os
import subprocess
import sys

def display(snippet_name):
    snippet_path = os.path.join(os.path.dirname(__file__), 'code_snippets', f'{snippet_name}.py')

    with open(snippet_path, 'r') as file:
        source_code = file.read()

    # Function to copy text to clipboard based on platform
    def copy_to_clipboard(text):
        # Linux
        if 'linux' in sys.platform:
            subprocess.run(['xclip', '-selection', 'clipboard'], input=text.strip().encode(), check=True)
        # Windows
        elif 'win32' in sys.platform:
            subprocess.run('clip', input=text.strip().encode(), check=True)
        else:
            raise OSError("Unsupported operating system")

    # Copy source code to clipboard
    copy_to_clipboard(source_code)
