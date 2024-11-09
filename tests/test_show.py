import pytest
import os
from unittest.mock import Mock, mock_open, patch
from package.offline.show import show
from package.offline.support.display import display

@pytest.fixture
def setup_test_env(monkeypatch):
    base_dir = os.path.dirname(__file__)
    snippets_dir = os.path.join(base_dir, "stash")
    test_snippet = "test_content"
    
    mock_list = Mock()
    mock_clipboard = Mock()
    monkeypatch.setattr("package.offline.support.list_snippets", mock_list)
    monkeypatch.setattr("package.offline.support.copy_to_clipboard", mock_clipboard)
    
    mock_dt = Mock()
    mock_dt.now.return_value.strftime.return_value = "1430"
    monkeypatch.setattr("package.password.datetime", mock_dt)
    
    return {
        "base_dir": base_dir,
        "snippets_dir": snippets_dir,
        "mock_list": mock_list,
        "mock_clipboard": mock_clipboard,
        "test_snippet": test_snippet
    }

def test_display_invalid_password_type(setup_test_env):
    with pytest.raises(ValueError):
        display("test.txt", "1430", "display")

def test_display_invalid_password_value(setup_test_env):
    with pytest.raises(ValueError):
        display("test.txt", 1431, "display")

def test_display_file_not_found(setup_test_env):
    with patch("builtins.open", mock_open()) as mock_file:
        mock_file.side_effect = FileNotFoundError()
        display("nonexistent.txt", 1430, "display")

def test_display_action_display(setup_test_env):
    env = setup_test_env
    mock_file = mock_open(read_data=env["test_snippet"])
    
    with patch("builtins.open", mock_file), \
         patch("builtins.print") as mock_print:
        display("test.txt", 1430, "display")
        
        mock_print.assert_called_once_with(env["test_snippet"])


def test_display_general_error(setup_test_env):
    with patch("builtins.open", mock_open()) as mock_file, \
         patch("builtins.print") as mock_print:
        mock_file.side_effect = Exception("Test error")
        display("test.txt", 1430, "display")
        
        mock_print.assert_called_once_with("Error: Test error")