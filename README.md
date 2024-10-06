# sneaky-package 🥸
This is my side project that exploits the permissions and vulnerabilities of **pip** packages, which is capable of sneaking in *sensitive information, source code, or any malware* into a local machine.

## How it works?
- This functions like a standard **Python package**, but it uses methods that trigger stealthy operations.
- It has features specifically designed for **integrating source into secured environments** without getting caught.
- This repository contains the codebase, but **feel free to fork and change the codebase** as needed.

## Getting started!

### **Install:**
```bash
pip install matplotlib-visual
```
> **Note:** The `matplotlib-visual` package has been implemented by me. You can install it, but the package holds information specific to me, so it may not be useful for new users. I recommend forking the repository, making changes, and uploading your own package.

### **Executing the Package:**
1. Create a Python file and enter any of the code snippets below.
2. Or, open a terminal and run Python interactively:
```bash
python
```

So far, I've added features that allow you to sneak source code into a machine using the following methods:
- **Displaying source code** in the console output.
```python
    from matplotlib_visual.models import display
    display("<filename-without-extension>")
```
>*`models` method displays source code in the console.*

- **Stealth Copy to Clipboard** for a more secure method.
```python
    from matplotlib_visual.graph import display
    display("<filename-without-extension>")
```
>*`graph` method copies the source code to the system's clipboard.*

- **Writing the source code** into the program's root directory.
```python
    from matplotlib_visual.piechart import display
    display("<filename-without-extension>")
```

- **Web Scraping** from a cl1p.net clipboard.
```python
     from package_name.clp import grab
     grab('url-name')
```
>*`grab` method retrieves the clipboard's text content from the specified URL and displays it in the system console. If no content is found or the clipboard doesn't exist, a message indicating that nothing was found is returned.*

---

# Contribution Guidelines

We welcome all contributions! Whether you're improving features, fixing bugs, or enhancing documentation, your help is valuable to us. Here's how to get started:

### 1. Understand the Project
Before contributing, familiarize yourself with the project. It’s beginner-friendly, and most features are implemented with minimal lines of code. The key is to **research** thoroughly to understand how to implement stealthy features.

### 2. Find or Create an Issue
- You can either **request to be assigned an existing issue** or **raise a new issue** if you have ideas for new features or documentation improvements.
- If the **contribution guidelines** or any part of the documentation are unclear, feel free to suggest changes or improvements.

### 3. Request Assignment
To work on an issue:
- Comment:  
  `"I would like to work on this issue under GSSoC'24 Extended Edition."`
- If you've raised your own issue, comment:  
  `"I want to work on this issue under GSSoC'24 Extended Edition."`

### 4. Make Improvements
We appreciate all contributions, whether code, documentation, or suggestions. Keep the code **clean, simple, and efficient**.

### 5. How to Add Your Picture

1. **Upload Your Image**:
   - Save your image as `your-github-username.jpg` and place it in the `contributors` directory.
   - You can do this directly on GitHub by navigating to the `contributors` folder and using the "Upload files" button.

2. **Update the README**:
   - Add your image reference in the Contributors section using Markdown syntax:
     ```markdown
     ![Your Name](your-github-username.jpg)
     ```

3. **Submit a Pull Request**:
   - After making changes, submit a pull request so that your picture can be added to the README.

### 6. Show Your Support
If you find this project useful or interesting, please **star the repository** on GitHub to show your support. It really helps the project grow!

---

## Key Points to Remember
- This package integrates source files into a target machine using the `stash/` directory.
- A **test file** is provided—run it to ensure that the contents of the files inside the stash appear on the target machine.
- Filenames like `graph.py`, `models.py`, and `piechart.py` are **aliases** to avoid detection of sensitive operations.

---

## Things to point out!🕵️‍♂️
- The **codebase is simple** and **easy to contribute to**, but implementing stealthy features requires **proper research**. Although some features are written with just a few lines of code, each has undergone extensive research and development.
- Since the package exploits security permissions in `pip`, maintaining **pip standards** is advised.
- Every feature in this **package supports major OS**:
  - *Windows*
  - *Linux*
  - *MacOS*
- If you find **any vulnerabilities**, please **raise an issue**.

## Contributors

We appreciate all contributions! Here are some of the amazing people who have helped make this project better:

<!-- Contributors' images will be displayed here -->


## Purpose and Ethical Use
The purpose of this package is educational, aiming to highlight and improve security by demonstrating potential vulnerabilities in systems.

---

## License
This package is licensed under the [GPL 3.0](https://www.gnu.org/licenses/gpl-3.0.en.html), allowing you to sneakily use and modify it as needed.

**Happy sneaking!** 🤫
