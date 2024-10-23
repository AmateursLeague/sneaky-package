#requirments:- 
pip install pyperclip requests


import pyperclip
import requests

def copy_to_clipboard(text):
    """Copy text to clipboard."""
    pyperclip.copy(text)
    print("Text copied to clipboard!")

def write_to_file(filename, text):
    """Write text to a specified file."""
    with open(filename, 'w') as file:
        file.write(text)
    print(f"Text written to {filename}")

def retrieve_text_from_cl1p(url):
    """Retrieve text from a cl1p.net URL."""
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print("Failed to retrieve the text. Status code:", response.status_code)
            return None
    except Exception as e:
        print("An error occurred:", e)
        return None

# Example usage
if __name__ == "__main__":
    # Copy text to clipboard
    copy_to_clipboard("Hello, this text is copied to clipboard.")

    # Write text to file
    write_to_file("example.txt", "This is an example text written to a file.")

    # Retrieve text from a cl1p.net URL
    url = "https://cl1p.net/your_cl1p_id"  # Replace with your cl1p ID
    text = retrieve_text_from_cl1p(url)
    if text:
        print("Retrieved text:", text)