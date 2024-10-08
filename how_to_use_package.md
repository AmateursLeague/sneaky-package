# 🚀 Quick Start Guide for matplotlib_visual
--- 

## **🔧Installations:**
```bash
pip install matplotlib_visual
```
> **Note:** The `matplotlib-visual` package has been implemented by [Project Manager](https://github.com/this-is-yaash) and has details specific to him, you are sugested to follow the steps above and fork the repository and upload a package.

## **⏱️Execution:**
1. Create a Python file with **.py** extension and enter any of the code snippets below.
2. Or, open a terminal and run Python interactively:
```bash
python
```

### 📊Features of this package:
- **📍Displaying source code** in the console output.
```python
    from package.models import display
    display("<filename-without-extension>")
```
 *`models` method displays source code in the console.*  


- **📍Stealth Copy to Clipboard** for a more secure method.
```python
    from package.graph import display
    display("<filename-without-extension>")
```
 *`graph` method copies the source code to the system's clipboard.*  

- **📍Writing the source code** into the program's root directory.
```python
    from package.piechart import display
    display("<filename-without-extension>")
```
 *`piechart` method writes the file in the root directory of execution.*  

- **📍Web Scraping** from a cl1p.net clipboard.
```python
     from package.clp import grab
     grab('url-name')
```
 *`grab` method retrieves the clipboard's text content from the specified URL and displays it in the system console. If no content is found, a message indicating "nothing found" is returned.*  

---
