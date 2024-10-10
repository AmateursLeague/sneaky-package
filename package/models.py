import os
import shutil


def display(snippet_name=None):
    try:
        if snippet_name:
            base_dir = os.path.dirname(__file__)
            snippet_path = os.path.join(base_dir, "stash", f"{snippet_name}.py")
            output_path = os.path.join(
                base_dir, f"{snippet_name}.py"
            )
            shutil.copyfile(snippet_path, output_path)
        else:
            ls() #Call ls() if snippet_name is not provided
    except Exception as e:
        print(f"Syntax Error: {e}")

def ls():
    stash_dir = os.path.join(os.path.dirname(__file__), 'stash')
    
    # Get the list of files in the stash directory
    try:
        files = os.listdir(stash_dir)
        if not files:
            print("No files found in stash directory.")
        else:
            # Format the output as numbered list
            for i, file in enumerate(files, 1):
                print(f"{i}. {file}")
    except FileNotFoundError:
        print("Stash directory not found.")
