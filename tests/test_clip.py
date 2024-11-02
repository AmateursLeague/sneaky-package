import pytest
from package.clip import display, copy_to_clipboard
from datetime import datetime
import subprocess


def test_display_right_password():
    # Use the current time as password
    current_time = datetime.now().strftime("%H%M")
    
    # Check that display does not raise an exception with the correct password
    try:
        display("test", current_time, clipboard=None)
    except ValueError as e:
        pytest.fail(f"Unexpected ValueError raised with correct password: {e}")
    except FileNotFoundError as e:
        pytest.skip(f"File not found, skipping test: {e}")
    except Exception as e:
        pytest.fail(f"Unexpected error raised with correct password: {e}")


def test_display_wrong_password():
    # Use an incorrect password
    with pytest.raises(ValueError, match="Syntax Error: Incorrect password"):
        display("test", "1111", clipboard=None)


def test_copy_to_clipboard(monkeypatch):
    # Mock subprocess.run to avoid actual clipboard interaction
    def mock_run(*args, **kwargs):
        return subprocess.CompletedProcess(args, 0)

    monkeypatch.setattr(subprocess, "run", mock_run)

    # Ensure no exceptions are raised when running copy_to_clipboard
    try:
        copy_to_clipboard("Test clipboard content")
    except Exception as e:
        pytest.fail(f"Unexpected error raised during clipboard copying: {e}")
