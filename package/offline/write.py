import shutil
import os
from package.password import valid_password


def write(snippet_name, password):
    if not isinstance(password, int) or not valid_password(password):
        raise ValueError("Incorrect password")

    base_dir = os.path.dirname(__file__)
    snippets_dir = os.path.join(base_dir, "stash")

    try:
        snippet_path = os.path.join(snippets_dir, snippet_name)
        output_path = os.path.join(base_dir, snippet_name)

        shutil.copyfile(snippet_path, output_path)
        print(f"File '{snippet_path}' copied successfully to '{output_path}'.")
    except FileNotFoundError:
        print("Error: No file found with the specified name.")
    except Exception as e:
        print(f"Error: {e}")
