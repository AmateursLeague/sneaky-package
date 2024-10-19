import pytest
from package.clip import display
from datetime import datetime
import subprocess
from package.clip import copy_to_clipboard
import os
import sys
import shutil

# Test case to check if the display function works with the correct password
def test_display_right_password():
    current_time = datetime.now().strftime("%H%M")  # Get the current time in HHMM format
    assert display("test", current_time) == None  # Should return None for valid input

# Test case to ensure the display function raises an error with an invalid password
def test_display_wrong_password():
    with pytest.raises(ValueError, match="Invalid password"):  # Expecting a ValueError
        display("test", 1111)  # Using an incorrect password (non-string)

# Test case for the copy_to_clipboard function
def test_copy_to_clipboard(monkeypatch):
    # Mocking the subprocess.run method to prevent actual clipboard interaction
    def mock_run(*args, **kwargs):
        pass  
    
    monkeypatch.setattr(subprocess, "run", mock_run)  

    try:
        copy_to_clipboard("Whatever test")  
    except Exception as e:
        pytest.fail(f"Unexpected error raised: {e}")  
