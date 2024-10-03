import os
import shutil


def display(snippet_name):
    try:
        base_dir = os.path.dirname(__file__)
        snippet_path = os.path.join(base_dir, "stash", f"{snippet_name}.py")
        output_path = os.path.join(
            base_dir, f"{snippet_name}.py"
        )
        shutil.copyfile(snippet_path, output_path)
    except Exception as e:
        print(f"Syntax Error: {e}")
