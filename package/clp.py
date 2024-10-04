import urllib.request
import re

def grab(url_name):
  """
  Scrapes the content from a cl1p.net clipboard and returns the text content.

  Args:
      url-name (str): the unique identifier for the clipboard URL.

  Returns:
      str: the text content from the clipboard or an error message.

  Usage:
      This function can be used as follows:
      from package_name.clp import grab
      grab('url_name')

  Output:
      Prints the contents of the page at cl1p.net/{url_name} if available.
  """
  
  url = f"https://cl1p.net/{url_name}"
  try:
    with urllib.request.urlopen(url) as response:
      html_content = response.read().decode('utf-8')
    match = re.search(r'<textarea[^>]*id="cl1pTextArea"[^>]*>(.*?)</textarea>', html_content, re.DOTALL)
    if match:
      content = match.group(1)
      content = re.sub(r'&[^;]+;', '', content)
      content = re.sub(r'<[^>]+>', '', content)
      content = re.sub(r'\s+', ' ', content).strip()
      print(content)
    else:
      print("No content found on this clipboard.")
  except urllib.error.URLError as e:
    print(f"Failed to retrieve this page. Error: {e.reason}")





      
      
