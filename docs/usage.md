## Getting Started

### Installation
To install the Sneaky Package, run the following command in your terminal:
```python
pip install matplotlib-visual
```

> **Note:** The `matplotlib-visual` package has been implemented by [Project Manager](https://github.com/this-is-yaash) and has details specific to him, you are suggested to follow the steps above and fork the repository and upload a package.

### Basic Usage
After installation, you can use the Sneaky Package in your Python scripts or interactively in a Python shell. Here's a simple example:
```python
from matplotlib_visual.show import display
display("<filename-without-extension>")
```
This will display the source code of the specified file in the console.

### Advanced Features
The Sneaky Package offers more advanced features, such as:
- **Stealth Copy to Clipboard**: Copies the source code to the system's clipboard for a more secure method.
```python
from matplotlib_visual.clip import display
display("<filename-without-extension>")
```
- **Writing the source code**: Writes the file in the root directory of execution.
```python
from matplotlib_visual.write import display
display("<filename-without-extension>")
```
- **Web Scraping**: Retrieves the clipboard's text content from a specified URL and displays it in the system console.
```python
from package_name.clp import grab
grab('url-name')
```

## Licence
The project works by highlighting and improving security measure by demonstrating potential vulnerabilities when the system connected with pip.
It is licensed under the [GPL 3.0](https://www.gnu.org/licenses/gpl-3.0.en.html), allowing you to sneakily use and modify it as needed.

---


**Happy sneaking!** 🤫
