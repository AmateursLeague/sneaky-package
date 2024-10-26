import unittest
from unittest.mock import patch, Mock, mock_open
import urllib.error
import sys
import os
from package.scrap import grab, copy_to_clipboard, write_to_file
from io import StringIO

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
class TestClipboardUtility(unittest.TestCase):
    
    def setUp(self):
        self.sample_html = '''
        <html>
            <body>
                <textarea id="cl1pTextArea">Test content</textarea>
            </body>
        </html>
        '''
        
        self.sample_html_escaped = '''
        <html>
            <body>
                <textarea id="cl1pTextArea">Test &amp; content &lt;with&gt; HTML</textarea>
            </body>
        </html>
        '''

    @patch('urllib.request.urlopen')
    @patch('builtins.open', new_callable=mock_open)
    def test_successful_grab(self, mock_file, mock_urlopen):
        mock_response = Mock()
        mock_response.read.return_value = self.sample_html.encode('utf-8')
        mock_urlopen.return_value.__enter__.return_value = mock_response
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            grab("test-url", "output.txt")
            
        mock_file.assert_called_once_with("output.txt", 'w')
        mock_file().write.assert_called_once_with("Test content")
        self.assertIn("The content is:  Test content", fake_stdout.getvalue())

    @patch('urllib.request.urlopen')
    def test_failed_grab_http_error(self, mock_urlopen):
        mock_urlopen.side_effect = urllib.error.HTTPError(
            url='https://cl1p.net/test-url',
            code=404,
            msg='Not Found',
            hdrs={},
            fp=None
        )

        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            grab("test-url", "output.txt")
            
        self.assertIn("Nothing found", fake_stdout.getvalue())

    @patch('urllib.request.urlopen')
    def test_failed_grab_url_error(self, mock_urlopen):
        mock_urlopen.side_effect = urllib.error.URLError('Connection refused')
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            grab("test-url", "output.txt")
            
        self.assertIn("Nothing found", fake_stdout.getvalue())

    @patch('urllib.request.urlopen')
    @patch('builtins.open', new_callable=mock_open)
    def test_html_escaped_content(self, mock_file, mock_urlopen):
        mock_response = Mock()
        mock_response.read.return_value = self.sample_html_escaped.encode('utf-8')
        mock_urlopen.return_value.__enter__.return_value = mock_response

        with patch('sys.stdout', new=StringIO()):
            grab("test-url", "output.txt")
            
        mock_file().write.assert_called_once_with("Test & content <with> HTML")

    @patch('subprocess.run')
    def test_copy_to_clipboard_linux(self, mock_run):
        # Mock platform to test Linux clipboard
        with patch('sys.platform', 'linux'), \
             patch('shutil.which', return_value='/usr/bin/xclip'):
            copy_to_clipboard("test content")
            
        mock_run.assert_called_once_with(
            ['xclip', '-selection', 'clipboard'],
            input=b'test content',
            check=True
        )

    @patch('subprocess.run')
    def test_copy_to_clipboard_windows(self, mock_run):
        with patch('sys.platform', 'win32'):
            copy_to_clipboard("test content")
            
        mock_run.assert_called_once_with(
            ['C:\\Windows\\System32\\clip.exe'],
            input=b'test content',
            check=True
        )

    @patch('subprocess.run')
    def test_copy_to_clipboard_macos(self, mock_run):
        with patch('sys.platform', 'darwin'):
            copy_to_clipboard("test content")
            
        mock_run.assert_called_once_with(
            ['/usr/bin/pbcopy'],
            input=b'test content',
            check=True
        )

    def test_copy_to_clipboard_unsupported_os(self):
        with patch('sys.platform', 'unknown'):
            with self.assertRaises(OSError) as context:
                copy_to_clipboard("test content")
            
        self.assertEqual(str(context.exception), "Unsupported operating system")

    def test_write_to_file(self):
        test_content = "Test content"
        mock_file = mock_open()
        with patch('builtins.open', mock_file):
            write_to_file(test_content, "test.txt")
        mock_file.assert_called_once_with("test.txt", 'w')
        mock_file().write.assert_called_once_with(test_content)

if __name__ == '__main__':
    unittest.main()
