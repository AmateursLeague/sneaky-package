import urllib.request
import re
import html
import subprocess
import sys
import shutil


def copy_to_clipboard(text):
    """Copy text to the clipboard based on the operating system."""
    # Linux
    if "linux" in sys.platform:
        if shutil.which("xclip") is None:
            print("Error: xclip not found. Install it.", file=sys.stderr)
            return
        subprocess.run(
            ["xclip", "-selection", "clipboard"],
            input=text.strip().encode(),
            check=True,
        )

    # Windows
    elif "win32" in sys.platform:
        subprocess.run(
            ["C:\\Windows\\System32\\clip.exe"], input=text.strip().encode(), check=True
        )

    # macOS
    elif "darwin" in sys.platform:
        subprocess.run(["/usr/bin/pbcopy"], input=text.strip().encode(), check=True)

    else:
        raise OSError("Unsupported operating system")


def grab_content(url_name):
    """Fetch content from the specified URL, handling HTML and regex for textarea."""
    url = f"https://cl1p.net/{url_name}"
    try:
        with urllib.request.urlopen(url) as response:
            html_content = response.read().decode("utf-8")
        match = re.search(
            r'<textarea[^>]*id="cl1pTextArea"[^>]*>(.*?)</textarea>',
            html_content,
            re.DOTALL,
        )
        if match:
            content = html.unescape(match.group(1)).strip()
            if content:
                return content
            else:
                return "No content found in the text area."
    except (urllib.error.HTTPError, urllib.error.URLError) as e:
        print(f"Error fetching content: {e}")
    return None


def show(url_name):
    """Display content from the URL."""
    content = grab_content(url_name)
    if content:
        print("The content is:", content)
    else:
        print("Nothing found. The clipboard might be empty or you have entered an incorrect URL.")


def clip(url_name):
    """Fetch content from the URL and copy it to the clipboard if found."""
    content = grab_content(url_name)
    if content:
        copy_to_clipboard(content)
        print("Content copied to clipboard.")
    else:
        print("Nothing found. The clipboard might be empty or you have entered an incorrect URL.")


def write(url_name, file_path):
    """Fetch content from the URL and write it to a file."""
    content = grab_content(url_name)
    if content:
        try:
            with open(file_path, "w") as file:
                file.write(content)
            print("Content written to file successfully.")
        except IOError as e:
            print(f"Error writing to file: {e}")
    else:
        print("Nothing found. The clipboard might be empty or you have entered an incorrect URL.")
