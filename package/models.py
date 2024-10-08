import os
import shutil
from datetime import datetime

def display(snippet_name):
    snippet_path = os.path.join(
            os.path.dirname(__file__), "stash", f"{snippet_name}.py"
        )
    try:
        if not os.path.exists(snippet_path):
            raise FileNotFoundError(f"File '{snippet_name}.py' not found in stash.")
        

        output_path = os.path.join(os.path.dirname(__file__), f"{snippet_name}.py")
        shutil.copyfile(snippet_path, output_path)

        with open(output_path, "r") as file:
            print(file.read())
    
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except Exception as e:
        print(f"Error: {e}")
