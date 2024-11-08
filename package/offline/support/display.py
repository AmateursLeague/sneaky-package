import os
from package.offline.support import copy_to_clipboard
from package.password import valid_password


def display(snippet_name, password, action):
    if not isinstance(password, int) or not valid_password(password):
        raise ValueError("Incorrect password")

    base_dir = os.path.dirname(__file__)
    snippets_dir = os.path.join(base_dir, "stash")

    try:
        snippet_path = os.path.join(snippets_dir, snippet_name)
        with open(snippet_path, "r") as file:
            content = file.read()

        if action == "display":
            print(content)
        elif action == "copy":
            copy_to_clipboard(content)
            print("Snippet copied to clipboard.")
    except FileNotFoundError:
        print("Error: No file found with the specified name.")
    except Exception as e:
        print(f"Error: {e}")
