import os
import hashlib
import time

def generate_secure_password():
    # Get the current time
    current_time = time.strftime("%H%M")
    # Create a hash of the current time for better security
    secret_key = "YourSecretKey"  # Change this to a strong secret key
    password = f"{current_time}{secret_key}"
    hashed_password = hashlib.sha256(password.encode()).hexdigest()  # Hashing the password
    return hashed_password

def display(snippet_name, password):
    snippet_path = os.path.join(
        os.path.dirname(__file__), "stash", f"{snippet_name}.py"
    )

    # Generate the correct password based on the current time
    correct_password = generate_secure_password()

    # Validate the password
    if password != correct_password:
        print("Invalid password!")
        return

    with open(snippet_path, "r") as file:
        source_code = file.read()

    print(source_code)
