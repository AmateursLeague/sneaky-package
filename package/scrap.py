import urllib.request
import re
import html
import subprocess
import sys
import shutil

def copy_to_clipboard(text):
    # Linux
    if "linux" in sys.platform:
        if shutil.which("xclip") is None:
            print("Error: xclip not found. Install it.", file=sys.stderr)
            return
        subprocess.run(
            ["xclip", "-selection", "clipboard"], 
            input=text.strip().encode(), 
            check=True)

    # Windows
    elif "win32" in sys.platform:
        subprocess.run(
            ["C:\\Windows\\System32\\clip.exe"], 
            input=text.strip().encode(), 
            check=True)

    # macOS
    elif "darwin" in sys.platform:
        subprocess.run(
            ["/usr/bin/pbcopy"], 
            input=text.strip().encode(), 
            check=True)

    else:
        raise OSError("Unsupported operating system")

def write_to_file(content, file):
    with open(file, 'w') as file:
        file.write(content)
    print("Content written to file successfully.")

def grab(url_name, file):
    url = f"https://cl1p.net/{url_name}"
    try:
        with urllib.request.urlopen(url) as response:
            html_content = response.read().decode('utf-8')
        match = re.search(r'<textarea[^>]*id="cl1pTextArea"[^>]*>(.*?)</textarea>', html_content, re.DOTALL)
        if match:
            content = html.unescape(match.group(1)).strip()
            if content:
                print("The content is: ", content)
                copy_to_clipboard(content)
                write_to_file(content, file)
                return
    except (urllib.error.HTTPError, urllib.error.URLError):
        pass
    print("Nothing found. The clipboard might be empty or you have entered a wrong URL.")

grab("hdgs", "output.txt")
