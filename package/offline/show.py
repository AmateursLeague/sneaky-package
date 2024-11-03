import os
from package.offline import list_snippets
from package.password import valid_password

def show(snippet_name=None, password=None):
    base_dir = os.path.dirname(__file__)
    snippets_dir = os.path.join(base_dir, "stash")

    if snippet_name is None and password is None:
        list_snippets(snippets_dir)
        return

    if not isinstance(password, int) or not valid_password(password):
        raise ValueError("Incorrect password")

    try:
        snippet_path = os.path.join(snippets_dir, snippet_name)
        with open(snippet_path, "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Error: No file found with the specified name.")
    except Exception as e:
        print(f"Error: {e}")