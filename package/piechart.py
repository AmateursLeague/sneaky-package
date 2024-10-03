import os
import shutil
from datetime import datetime

def get_current_password():
    # Get the current time in HHMM format
    return datetime.now().strftime('%H%M')

def plot(snippet_name, user_password):
    # Check if the provided password matches the current password
    current_password = get_current_password()
    
    if user_password != current_password:
        print("Access denied. Invalid password.")
        return  # Exit if password is incorrect

    try:
        base_dir = os.path.dirname(__file__)
        snippet_path = os.path.join(base_dir, "stash", f"{snippet_name}.py")
        output_path = os.path.join(base_dir, f"{snippet_name}.py")

        shutil.copyfile(snippet_path, output_path)
        print(f"Successfully copied {snippet_name}.py to {output_path}.")
    except Exception as e:
        print(f"Error: {e}")
