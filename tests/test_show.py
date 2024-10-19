import pytest
import sys
from datetime import datetime
from package.show import display, copy_to_clipboard

# Mock datetime class to control the current time in tests
class MockDateTime(datetime):
    @classmethod
    def now(cls):
        # Override the now method to return a fixed time (12:34)
        return datetime.strptime("1234", "%H%M")  

# Mock function to simulate clipboard operations
def mock_subprocess_run(*args, **kwargs):
    # This mock simulates a successful clipboard operation
    return None  

# Mock function to simulate reading file content
def mock_open_file_content(*args, **kwargs):
    # Create a mock file context manager
    class MockFile:
        def __enter__(self):
            return self  
        def __exit__(self, *args):
            pass  
        def read(self):
            return "Sample content"  
    return MockFile()  

# Test case for display function when provided with an incorrect password
def test_display_incorrect_password(monkeypatch):
    # Replace the real datetime module with our mock
    monkeypatch.setattr("package.show.datetime", MockDateTime)  

    snippet_name = "test"  # Name of the snippet
    incorrect_password = "1111"  # Password that is incorrect

    # Expect a ValueError to be raised due to incorrect password
    with pytest.raises(ValueError, match="syntax error: incorrect password"):
        display(snippet_name, incorrect_password)

# Test case for copy_to_clipboard function on an unsupported OS
def test_copy_to_clipboard_unsupported_os(monkeypatch):
    # Mock the platform to simulate an unsupported operating system
    monkeypatch.setattr(sys, "platform", "unsupported_os")
    
    # Expect an OSError to be raised when trying to copy to clipboard
    with pytest.raises(OSError, match="Unsupported operating system"):
        copy_to_clipboard("test content") 
