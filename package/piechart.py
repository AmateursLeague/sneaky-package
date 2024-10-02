import os
import shutil


def plot(snippet_name):
    snippet_path = os.path.join(
        os.path.dirname(__file__), "stash", f"{snippet_name}.py"
    )
    output_path = os.path.join(os.path.dirname(__file__), f"{snippet_name}.py")

    if os.path.isfile(snippet_path):
        shutil.copyfile(snippet_path, output_path)
    else:
        print("Syntax Error!")
