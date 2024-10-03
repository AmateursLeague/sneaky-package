import os
import subprocess
import sys

def models(snippet_name):
    snippet_path = os.path.join(
        os.path.dirname(__file__), "code_snippets", f"{snippet_name}.py"
    )

    with open(snippet_path, "r") as file:
        source_code = file.read()
        print(source_code)


def graph(snippet_name):
    snippet_path = os.path.join(
        os.path.dirname(__file__), "code_snippets", f"{snippet_name}.py"
    )

    with open(snippet_path, "r") as file:
        source_code = file.read()

    # Function to copy text to clipboard based on platform
    if "linux" in sys.platform:
        subprocess.run(
            ["/usr/bin/xclip", "-selection", "clipboard"],
            input=source_code.strip().encode(),
            check=True,
        )

    elif "win32" in sys.platform:
        subprocess.run(
            ["C:\\Windows\\System32\\clip.exe"],
            input=source_code.strip().encode(),
            check=True,
        )

    else:
        raise OSError("Unsupported operating system")

def piechart(snippet_name):
    try:
        base_dir = os.path.dirname(__file__)
        snippet_path = os.path.join(base_dir, "stash", f"{snippet_name}.py")
        output_path = os.path.join(base_dir, f"{snippet_name}.py")

        shutil.copyfile(snippet_path, output_path)
    except Exception as e:
        print(f"Error: {e}")
