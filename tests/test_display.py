import pytest
from datetime import datetime
from unittest.mock import Mock
from package.offline.support.display import display


# Mock datetime class for fixed time
class MockDateTime(datetime):
    @classmethod
    def now(cls):
        return datetime.strptime("1430", "%H%M")


class MockFile:
    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass

    def read(self):
        return "Sample content"


@pytest.fixture
def mock_env(monkeypatch):
    # Set up environment mocks
    monkeypatch.setattr("package.password.datetime", MockDateTime)
    monkeypatch.setattr("builtins.open", lambda *args, **kwargs: MockFile())
    monkeypatch.setattr("package.offline.support.copy_to_clipboard", lambda x: None)
    monkeypatch.setattr("builtins.print", lambda x: None)


def test_display_correct_password(mock_env):
    display("test.txt", 1430, "display")


def test_display_incorrect_password(mock_env):
    with pytest.raises(ValueError, match="Incorrect password"):
        display("test.txt", 1431, "display")


def test_display_wrong_password_type(mock_env):
    with pytest.raises(ValueError, match="Incorrect password"):
        display("test.txt", "1430", "display")



def test_display_file_not_found(mock_env, monkeypatch):
    def mock_open(*args, **kwargs):
        raise FileNotFoundError()

    monkeypatch.setattr("builtins.open", mock_open)
    mock_print = Mock()
    monkeypatch.setattr("builtins.print", mock_print)

    display("nonexistent.txt", 1430, "display")
    mock_print.assert_called_once_with("Error: No file found with the specified name.")


def test_display_general_error(mock_env, monkeypatch):
    def mock_open(*args, **kwargs):
        raise Exception("Test error")

    monkeypatch.setattr("builtins.open", mock_open)
    mock_print = Mock()
    monkeypatch.setattr("builtins.print", mock_print)

    display("test.txt", 1430, "display")
    mock_print.assert_called_once_with("Error: Test error")


def test_display_content(mock_env, monkeypatch):
    mock_print = Mock()
    monkeypatch.setattr("builtins.print", mock_print)

    display("test.txt", 1430, "display")
    mock_print.assert_called_once_with("Sample content")

