from models import display  # Adjust the import path as necessary
from datetime import datetime

def test_display_function():
    snippet_name = 'test'  # This should match the name of your snippet file
    
    # Test with correct password
    correct_password = datetime.now().strftime('%H%M')
    print("Testing with correct password:")
    display(snippet_name, correct_password)

    # Test with incorrect password
    incorrect_password = "0000"  # Any password that is unlikely to be the current time
    print("\nTesting with incorrect password:")
    display(snippet_name, incorrect_password)

if __name__ == "__main__":
    test_display_function()
