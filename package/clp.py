import urllib.request
import re
import html
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def grab(url_name: str) -> str:
    """
    Retrieve the clipboard content from a specified cl1p.net URL.

    Parameters:
    url_name (str): The identifier for the clipboard URL.

    Returns:
    str: The content retrieved from the clipboard, or an error message.
    """
    url = f"https://cl1p.net/{url_name}"
    try:
        with urllib.request.urlopen(url) as response:
            html_content = response.read().decode('utf-8')
        match = re.search(r'<textarea[^>]*id="cl1pTextArea"[^>]*>(.*?)</textarea>', html_content, re.DOTALL)
        if match:
            content = html.unescape(match.group(1)).strip()
            return content if content else "Nothing found."
    except urllib.error.HTTPError as e:
        logging.error(f"HTTP error: {e.code} - {e.reason}")
        return "Invalid URL."
    except urllib.error.URLError as e:
        logging.error(f"URL error: {e.reason}")
        return "Network error."

    return "Nothing found. The clipboard might be empty."
