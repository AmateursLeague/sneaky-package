import os
import shutil


def display(snippet_name):
    try:
        snippet_path = os.path.join(
            os.path.dirname(__file__), "stash", f"{snippet_name}.py"
        )

        if os.path.isfile(snippet_path):
            backup_path = os.path.join(os.path.dirname(__file__), "stash", f"{snippet_name}_backup.py")
            shutil.copy(snippet_path, backup_path)

            with open(snippet_path, "r") as file:
                source_code = file.read()

            print(source_code)
        else:
            print(f"File '{snippet_name}.py' does not exist.")
    except FileNotFoundError as e:
        print(f"Error: {e} - File not found.")
    except PermissionError as e:
        print(f"Error: {e} - Permission denied.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
