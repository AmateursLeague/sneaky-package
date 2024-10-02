import os
import inspect


def display(snippet_name):
    snippet_path = os.path.join(
        os.path.dirname(__file__), "stash", f"{snippet_name}.py"
    )

    if os.path.isfile(snippet_path):
        with open(snippet_path, "r") as file:
            source_code = file.read()

    print(source_code)
