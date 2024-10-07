# sneaky-package 🥸  
A ready-to-deploy Python package designed to **stealthily integrate files** within a machine, ensuring discreet and seamless file operations without detection. This project is nothing more than a *lightweight & faster* Python package that aims to highlight and improve security by demonstrating potential vulnerabilities in the system when connected with **`pip`**.

---

## Getting Started! 🚀

### How does it work? 🤔  
- Install the package using **`pip`**.
- Either create a `.py` file or run Python in the terminal and execute the program.
- You can execute the existing three features, but feel free to add or update features of your own and deploy your own package globally. 🌍

---

### Example:  

> **Note**: I already have a package of my own deployed globally in PyPI.  

1. **Install the package** 📦:  
```bash  
pip install matplotlib_visual  
```

2. **Create a file or open Python in the terminal and enter the following code**:  
```python  
from matplotlib_visual.display import featureName  
featureName("fileName", 1234) # password integer  
```  

- `display` - A method that contains features  
- `featureName` - Check out `display.py` in the repo and use the required method name (feature).

---

## How to Setup and Deploy the Package 🛠️

1. [**Documentation on How to Build?**](https://gist.github.com/this-is-yaash/c6d1dceee10d17851b79d3781a078c51) 📄  
2. [**Documentation on Register PyPI and Deploy Package**](https://gist.github.com/this-is-yaash/12c00a4c9cff94bf12a0e753b4eed075)  

> Contributors & Users are advised to use this *gist* until the official documentation is ready. 📝

---

## Features ✨

These features allow you to discreetly integrate source code into a private machine using the following methods:

- **Displaying source code** in the console output. 🖥️  
```python  
from package.display import models  
display("<filename-without-extension>")  
```
> *`models` method displays source code in the console.*  

- **Stealth Copy to Clipboard** for a more secure method. 📋  
```python  
from package.display import graph  
display("<filename-without-extension>")  
```
> *`graph` method copies the source code to the system's clipboard.*  

- **Writing the source code** into the program's root directory. 📝  
```python  
from package.display import piechart  
display("<filename-without-extension>")  
```
> *`piechart` method writes the file in the root directory of execution.*  

- **Web Scraping** from a cl1p.net clipboard. 🌐  
```python  
from package.display import grab  
grab('url-name')  
```
> *`grab` method retrieves the clipboard's text content from the specified URL and displays it in the system console. If no content is found, a message indicating "nothing found" is returned.*  

---

## Contribution Guidelines 🙌

We welcome all contributions! Whether you're improving features, fixing bugs, or enhancing documentation, your help is valuable to us. Here's how to get started:

### 1. Understand the Project 🔍
- It’s **beginner-friendly** with most features implemented in **minimal lines of code**.  
- Research thoroughly to understand how to implement stealthy features. 🕵️‍♀️

### 2. Find or Create an Issue 🛠️
- Visit the [**Issues section**](https://github.com/AmateursLeague/sneaky-package/issues) in this repository.  
- Look for existing issues that are available to work on or past their time limit! ⏳  
- Or raise your own issue with a proposal or idea and start contributing! 🗣️

### 3. Make Improvements ✨
- Keep the code **clean, simple, and efficient**. 🧹

### 4. Show Your Support 🌟
- If you find this project useful or interesting, please **star the repository** on GitHub! ⭐ It helps the project grow!

---

## Key Points to Remember 📌
- This package integrates source files into a target machine using the `stash/` directory. 📁  
- A **test file** is provided—run it to ensure that the files inside the stash appear on the target machine. 💡  
- Filenames like `graph.py`, `models.py`, and `piechart.py` are **aliases** to avoid detection. 🔒  

---

## Things to Point Out! 🕵️‍♂️
- The **codebase is simple** and **easy to contribute to**, but implementing stealthy features requires **proper research**. 🔍  
- This package **exploits security permissions** in `pip`, so maintaining **pip standards** is advised. ✅  
- Every feature in this package supports major operating systems:  
  - *Windows* 🪟  
  - *Linux* 🐧  
  - *MacOS* 🍏  

If you find **any vulnerabilities**, please raise an issue! ⚠️

---

## Purpose and Ethical Use ⚖️

The purpose of this package is **educational**, aiming to highlight and improve security by demonstrating potential vulnerabilities in systems. 🛡️

---

## License 📜

This package is licensed under the [**GPL 3.0**](https://www.gnu.org/licenses/gpl-3.0.en.html), allowing you to sneakily use and modify it as needed.

**Happy sneaking!** 🤫
