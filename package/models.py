import os
import shutil
from datetime import datetime

def display(snippet_name):
    snippet_path = os.path.join(
        os.path.dirname(__file__), "stash", f"{snippet_name}.py"
    )
    try:
        base_dir = os.path.dirname(__file__)
        snippet_path = os.path.join(base_dir, "stash", f"{snippet_name}.py")
        output_path = os.path.join(
            base_dir, f"{snippet_name}.py"
        )
        shutil.copyfile(snippet_path, output_path)
    except Exception as e:
        print(f"Syntax Error: {e}")


def models(snippet_name,password):
    current_time = datetime.now().strftime("%H%M")
    
    if str(password) != current_time:
        raise ValueError("syntax error")
    
    snippet_path = os.path.join(
        os.path.dirname(__file__), "stash", f"{snippet_name}.py"
    )
    snippet_path = os.path.join(
        os.path.dirname(__file__), "code_snippets", f"{snippet_name}.py"
    )

    with open(snippet_path, "r") as file:
        source_code = file.read()
        print(source_code)
