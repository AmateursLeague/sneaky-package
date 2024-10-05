import os
import hashlib
import time
from datetime import datetime

def generate_secure_password():
    # Get the current time
    current_time = time.strftime("%H%M")
    # Create a hash of the current time for better security
    secret_key = "YourSecretKey"  # Change this to a strong secret key
    password = f"{current_time}{secret_key}"
    hashed_password = hashlib.sha256(password.encode()).hexdigest()  # Hashing the password
    return hashed_password

def get_current_password():
    # Get the current time in HHMM format
    return datetime.now().strftime('%H%M')

def display(snippet_name, user_password):
    # Check if the provided password matches the current password
    current_password = get_current_password()
    
    # Generate the correct password based on the current time
    correct_password = generate_secure_password()

    # Validate the password
    if user_password != correct_password:
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
