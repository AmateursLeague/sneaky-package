import pytest
from unittest.mock import patch, Mock
import urllib.request
import urllib.error
from package.scrap import grab

# Sample HTML responses
VALID_HTML_WITH_CONTENT = '''
<html>
<body>
    <textarea id="cl1pTextArea">Sample clipboard content</textarea>
</body>
</html>
'''

VALID_HTML_EMPTY_CONTENT = '''
<html>
<body>
    <textarea id="cl1pTextArea"></textarea>
</body>
</html>
'''

INVALID_HTML_NO_TEXTAREA = '''
<html>
<body>
    <div>Some content but no textarea</div>
</body>
</html>
'''

# Mock response class
class MockResponse:
    def __init__(self, content, status=200):
        self.content = content
        self.status = status

    def read(self):
        return self.content.encode('utf-8')

    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass

def test_grab_successful_content(capsys):
    """Test successful content retrieval"""
    with patch('urllib.request.urlopen') as mock_urlopen:
        mock_urlopen.return_value = MockResponse(VALID_HTML_WITH_CONTENT)
        
        grab("test-url")
        
        # Check if correct URL was called
        mock_urlopen.assert_called_once_with("https://cl1p.net/test-url")
        
        # Check if content was printed
        captured = capsys.readouterr()
        assert "Sample clipboard content" in captured.out

def test_grab_empty_content(capsys):
    """Test empty clipboard content"""
    with patch('urllib.request.urlopen') as mock_urlopen:
        mock_urlopen.return_value = MockResponse(VALID_HTML_EMPTY_CONTENT)
        
        grab("test-url")
        
        captured = capsys.readouterr()
        assert "Nothing found" in captured.out

def test_grab_no_textarea(capsys):
    """Test HTML without textarea"""
    with patch('urllib.request.urlopen') as mock_urlopen:
        mock_urlopen.return_value = MockResponse(INVALID_HTML_NO_TEXTAREA)
        
        grab("test-url")
        
        captured = capsys.readouterr()
        assert "Nothing found" in captured.out

def test_grab_http_error(capsys):
    """Test HTTP error handling"""
    with patch('urllib.request.urlopen') as mock_urlopen:
        mock_urlopen.side_effect = urllib.error.HTTPError(
            url="https://cl1p.net/test-url",
            code=404,
            msg="Not Found",
            hdrs={},
            fp=None
        )
        
        grab("test-url")
        
        captured = capsys.readouterr()
        assert "Nothing found" in captured.out

def test_grab_url_error(capsys):
    """Test URL error handling"""
    with patch('urllib.request.urlopen') as mock_urlopen:
        mock_urlopen.side_effect = urllib.error.URLError("Connection failed")
        
        grab("test-url")
        
        captured = capsys.readouterr()
        assert "Nothing found" in captured.out

def test_grab_encoded_content(capsys):
    """Test HTML with encoded characters"""
    html_with_encoded_content = '''
    <html>
    <body>
        <textarea id="cl1pTextArea">Hello &amp; World</textarea>
    </body>
    </html>
    '''
    
    with patch('urllib.request.urlopen') as mock_urlopen:
        mock_urlopen.return_value = MockResponse(html_with_encoded_content)
        
        grab("test-url")
        
        captured = capsys.readouterr()
        assert "Hello & World" in captured.out

def test_grab_multiple_textareas(capsys):
    """Test HTML with multiple textareas"""
    html_multiple_textareas = '''
    <html>
    <body>
        <textarea>Wrong content</textarea>
        <textarea id="cl1pTextArea">Correct content</textarea>
        <textarea>More wrong content</textarea>
    </body>
    </html>
    '''
    
    with patch('urllib.request.urlopen') as mock_urlopen:
        mock_urlopen.return_value = MockResponse(html_multiple_textareas)
        
        grab("test-url")
        
        captured = capsys.readouterr()
        assert "Correct content" in captured.out
