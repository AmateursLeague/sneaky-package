import os


def list_snippets(snippets_dir):
    try:
        contents = os.listdir(snippets_dir)
        for file in contents:
            print(file)
    except FileNotFoundError:
        print("Error: Stash directory not found.")
    except Exception as e:
        print(f"Error: {e}")
