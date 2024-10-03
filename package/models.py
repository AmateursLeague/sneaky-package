import os
import inspect
from datetime import datetime

def get_current_password():
    # Get the current time in HHMM format
    return datetime.now().strftime('%H%M')

def display(snippet_name, user_password):
    # Check if the provided password matches the current password
    current_password = get_current_password()
    
    if user_password != current_password:
        print("Access denied. Invalid password.")
        return  # Exit the function if the password is incorrect

    snippet_path = os.path.join(
        os.path.dirname(__file__), "stash", f"{snippet_name}.py"
    )

    try:
        with open(snippet_path, "r") as file:
            source_code = file.read()

        print(source_code)
    except FileNotFoundError:
        print(f"Snippet '{snippet_name}' not found.")
