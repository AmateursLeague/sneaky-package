import pytest
import sys
from datetime import datetime
from package.show import display, copy_to_clipboard


# Mock datetime class
class MockDateTime(datetime):
    @classmethod
    def now(cls):
        return datetime.strptime("1234", "%H%M")  # Mock time to 12:34


# Mock functions for clipboard operations
def mock_subprocess_run(*args, **kwargs):
    return None  # Assume successful run


def mock_open_file_content(*args, **kwargs):
    class MockFile:
        def __enter__(self):
            return self

        def __exit__(self, *args):
            pass

        def read(self):
            return "Sample content"

    return MockFile()


def test_display_correct_password(monkeypatch):
    monkeypatch.setattr("package.show.datetime", MockDateTime)  # Mock datetime

    snippet_name = "test"
    correct_password = "1234"  # Matches the mocked datetime

    # Should not raise any exception
    try:
        display(snippet_name, correct_password)
    except Exception:
        pytest.fail("Unexpected error raised for correct password")


def test_display_incorrect_password(monkeypatch):
    monkeypatch.setattr("package.show.datetime", MockDateTime)  # Mock datetime

    snippet_name = "test"
    incorrect_password = "1111"  # Different from "1234"

    with pytest.raises(ValueError, match="syntax error: incorrect password"):
        display(snippet_name, incorrect_password)


def test_copy_to_clipboard_supported_os(monkeypatch):
    # Test for a supported operating system (Linux example)
    monkeypatch.setattr(sys, "platform", "linux")
    monkeypatch.setattr("subprocess.run", mock_subprocess_run)

    copy_to_clipboard("test content")  # Should run without error


def test_copy_to_clipboard_unsupported_os(monkeypatch):
    monkeypatch.setattr(sys, "platform", "unsupported_os")

    with pytest.raises(OSError, match="Unsupported operating system"):
        copy_to_clipboard("test content")
