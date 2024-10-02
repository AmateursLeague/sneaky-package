import os
import inspect


def display(snippet_name):
    snippet_path = os.path.join(
        os.path.dirname(__file__), "stash", f"{snippet_name}.py"
    )

    if not os.path.isfile(snippet_path):
        print(f"Error: The file '{snippet_name}.py' does not exist.")
        return

    try:
        with open(snippet_path, "r") as file:
            source_code = file.read()
        print(source_code)
    except Exception as e:
        print(f"Error reading file: {e}")
