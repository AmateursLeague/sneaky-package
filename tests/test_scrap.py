import unittest
from unittest.mock import patch, mock_open
import os
from package.scrap import copy_to_clipboard, save_snippet


class TestScrapFunctions(unittest.TestCase):

    @patch('subprocess.run')
    @patch('shutil.which', return_value='xclip')  # Mocking xclip for Linux
    @patch('sys.platform', 'linux')  # Mocking Linux platform
    def test_copy_to_clipboard_linux(self, mock_which, mock_run):
        text = "Hello, World!"
        copy_to_clipboard(text)
        mock_run.assert_called_once_with(
            ["xclip", "-selection", "clipboard"],
            input=text.strip().encode(),
            check=True
        )

    @patch('subprocess.run')
    @patch('sys.platform', 'win32')  # Mocking Windows platform
    def test_copy_to_clipboard_windows(self, mock_run):
        text = "Hello, World!"
        copy_to_clipboard(text)
        mock_run.assert_called_once_with(
            ["C:\\Windows\\System32\\clip.exe"],
            input=text.strip().encode(),
            check=True
        )

    @patch('subprocess.run')
    @patch('sys.platform', 'darwin')  # Mocking macOS platform
    def test_copy_to_clipboard_macos(self, mock_run):
        text = "Hello, World!"
        copy_to_clipboard(text)
        mock_run.assert_called_once_with(
            ["/usr/bin/pbcopy"],
            input=text.strip().encode(),
            check=True
        )

    @patch('os.makedirs')
    @patch('builtins.open', new_callable=mock_open)
    def test_save_snippet(self, mock_file, mock_makedirs):
        snippet_name = "test_snippet"
        content = "This is a test snippet."
        
        save_snippet(snippet_name, content)
        
        # Check if the directory was created
        mock_makedirs.assert_called_once_with(os.path.join(os.path.dirname(__file__), "stash"), exist_ok=True)
        
        # Check if the file was opened with the correct path
        mock_file.assert_called_once_with(os.path.join(os.path.dirname(__file__), "stash", f"{snippet_name}.txt"), "w")
        
        # Check if the content was written to the file
        mock_file().write.assert_called_once_with(content)

if __name__ == '__main__':
    unittest.main()
