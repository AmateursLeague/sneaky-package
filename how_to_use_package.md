# 🚀 Quick Start Guide for sneaky-package
--- 


## **🔧Installation:**
```bash
pip install matplotlib_visual
```
> **Note:** The `matplotlib_visual` package has been implemented by [this-is-yaash](https://github.com/this-is-yaash) and contains user-specific content. You are advised to follow the steps in the [`README.md`](https://github.com/AmateursLeague/sneaky-package?tab=readme-ov-file#-how-to-contribute-to-this-project) to deploy your own Python package and upload it accordingly.

## **⏱️Execution:**
1. Create a Python file with **.py** extension and enter any of the code snippets below.
2. Or, open a terminal and run Python interactively:
```bash
python
```

### 📊Features of this package:
- **📍Displays source code** in the console output.

 *`models` method displays source code of the file or python code snipped that has been copied from the file which was passed as an argument*  
```python
    from package.models import display
    display("<filename-without-extension>")
```



- **📍Stealth Copy to Clipboard** for a more secure method.

 *`graph` method copies the source code to the system's clipboard.*  
```python
    from package.graph import display
    display("<filename-without-extension>")
```


- **📍Writes the source code** into the program's root directory.

 *`piechart` method writes the file in the root directory of execution.*  
```python
    from package.piechart import display
    display("<filename-without-extension>")
```


- **📍Web Scraping** from cl1p.net clipboard.

 *`grab` method retrieves the clipboard's text content from the specified URL and displays it in the system console. If no content is found, a message indicating "nothing found" is returned.*  
```  python
     from package.clp import grab
     grab('url-name')
```


---
