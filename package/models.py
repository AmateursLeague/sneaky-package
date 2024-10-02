import os


def display(snippet_name):
    try:
        snippet_path = os.path.join(
            os.path.dirname(__file__), "stash", f"{snippet_name}.py"
        )

        with open(snippet_path, "r") as file:
            source_code = file.read()

        print(source_code)
    except FileNotFoundError as e:
        print(f"Error: {e} - File not found.")
    except PermissionError as e:
        print(f"Error: {e} - Permission denied.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
