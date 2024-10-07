import urllib.request
import re
import html
def grab(url_name: str) -> str:
    url = f"https://cl1p.net/{url_name}"
    try:
        with urllib.request.urlopen(url) as response:
            html_content = response.read().decode('utf-8')
        match = re.search(r'<textarea[^>]*id="cl1pTextArea"[^>]*>(.*?)</textarea>', html_content, re.DOTALL)
        if match:
            content = html.unescape(match.group(1)).strip()
            if content:
                print(content)
                return
    except (urllib.error.HTTPError, urllib.error.URLError):
        pass
    print("Nothing found. The clipboard might be empty or you have entered a wrong URL.")
 
