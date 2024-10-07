# SNEAKY PACKAGE 👾
![GSSoC-ext](GSSoC-Ext.png)
## Table of Contents
1. [🚀Project Overview](#project-overview)
2. [✨ Key Features ✨](#✨key-features✨)
3. [⛓️ What is a **Pip Package**? ⛓️](#⛓️what-is-a-pip-package-⛓️)
4. [🪪 Licence](#🪪licence)
5. [🚀 How to Contribute to This Project](#🚀-how-to-contribute-to-this-project)
   - [🍴 Fork the Repository](#🍴-fork-the-repository)
   - [💻 Clone Your Fork](#💻-clone-your-fork)
   - [🌿 Create a New Branch](#🌿-create-a-new-branch)
   - [🛠️ Make Your Changes](#🛠️-make-your-changes)
   - [✅ Finalize Your Changes](#✅-finalize-your-changes)
   - [💬 Commit Your Changes](#💬-commit-your-changes)
   - [📤 Push Your Changes](#📤-push-your-changes)
   - [🔄 Create a Pull Request (PR)](#🔄-create-a-pull-request-pr)
   - [🔎 Review Changes](#🔎-review-changes)
6. [🏆 Contribution Points](#🏆-contribution-points)
7. [📄 GSSoC Guidelines 📄](#📄-gssoc-guidelines-📄)
8. [📑 Note for Contributors](#📑-note-for-contributors)
9. [Technologies Used](#technologies-used)
10. [Contributors ✨](#contributors-✨)
11. [💌 Ending Note](#💌-ending-note)

## 🚀Project Overview

A ready-to-deploy Python package designed to stealthily integrate files within a machine, ensuring discreet and seamless file operations without detection. This project is nothing more than a lightweight & faster Python package that aims to highlight and improve security by demonstrating potential vulnerabilities in the system when connected with pip.

---

## ✨ Key Features ✨

### 💾 Designed to Look Conventional
- The package installs like any normal Python package, but its main target is to perform sneaky functions that are unfavorable for users.

### 📥 Installing Without Getting Noticed
- One key feature of the package is that it is designed in such a way that it becomes difficult to detect its installation. The download and installation can be done without getting caught.

### 🖥️ Cross-Platform Package
- The package runs across all major operating systems, including **Windows**, **Linux**, and **macOS**.


---


## ⛓️ What is a **Pip Package**? ⛓️

-A **Pip Package** allows the user to manage, install, update, and remove Python packages from the Python Package Index (PyPi). 

-These packages contain a collection of builtin libraries and modules. 


## 🪪Licence
The project works by highlighting and improving security measure by demonstrating potential vulnerabilities when the system connected with pip.
It is licensed under the [GPL 3.0](https://www.gnu.org/licenses/gpl-3.0.en.html), allowing you to sneakily use and modify it as needed.

---

## 🚀 How to Contribute to This Project

We welcome all contributors to our project **Sneaky-Package**. Before contributing we request you to get familiar with the project. The project is biggner friendly and you can find features you would like to imporove including bugs, enhancements or documentation. Here are steps to start contributing- 

1. **🍴 Fork the Repository**  
   - Go to the [repository page](https://github.com/AmateursLeague/sneaky-package).
   - Click the *Fork* button (top right) to create a copy in your GitHub account.

2. **💻 Clone Your Fork**  
   - Open your terminal and run:
     ```bash
     git clone https://github.com/ENTER-YOUR-USERNAME/Sneaky-package.git
     ```
   - You have to enter your Github username in above code. 

3. **🌿 Create a New Branch** 
   - Create a new branch for your work to ensure that changes made by other contributors don't overlap with yours:
     ```bash
     git switch YOUR-BRANCH-NAME
     ```

4. **🛠️ Make Your Changes**
   - Make the required changes in the package, and contact the project manager [Yashwanth](https://github.com/this-is-yaash) for any queries.
     
## How to get Started-
--- 

### **🔧Instalations:**
```bash
pip install matplotlib-visual
```
> **Note:** The `matplotlib-visual` package has been implemented by [Project Manager](https://github.com/this-is-yaash) and has details specific to him, you are sugested to follow the steps above and fork the repository and upload a package.

### **⏱️Execution:**
1. Create a Python file and enter any of the code snippets below.
2. Or, open a terminal and run Python interactively:
```bash
python
```

### 📊Progress so far-
- **📍Displaying source code** in the console output.
```python
    from matplotlib_visual.models import display
    display("<filename-without-extension>")
```
> *`models` method displays source code in the console.*  


- **📍Stealth Copy to Clipboard** for a more secure method.
```python
    from matplotlib_visual.graph import display
    display("<filename-without-extension>")
```
> *`graph` method copies the source code to the system's clipboard.*  

- **📍Writing the source code** into the program's root directory.
```python
    from matplotlib_visual.piechart import display
    display("<filename-without-extension>")
```
> *`piechart` method writes the file in the root directory of execution.*  

- **📍Web Scraping** from a cl1p.net clipboard.
```python
     from package_name.clp import grab
     grab('url-name')
```
> *`grab` method retrieves the clipboard's text content from the specified URL and displays it in the system console. If no content is found, a message indicating "nothing found" is returned.*  

---

5. **✅ Finalize Your Changes**
   - Before you proceed to next step ensure all changes are made and check them once again before making the final commit.


6. **💬 Commit Your Changes** 
   - Once ready, commit them with a descriptive message:
     ```bash
     git add .
     git commit -m "Added feature X or Fixed issue Y"
     ```

7. **📤 Push Your Changes**
   - Push your changes to your forked repository:
     ```bash
     git push origin YOUR-BRANCH-NAME
     ```

8. **🔄 Create a Pull Request (PR)** 
   - Go back to the original repository [here]((https://github.com/AmateursLeague/sneaky-package)).
   - Click the *Compare & pull request* button, write a short description of your changes, and submit the PR.

9. **🔎 Review Changes**
   - The project manager will review your PR, and if approved, your request will be merged.


## 🏆 Contribution Points
All tasks will be assigned various levels based on complexity and required skills. Each level provides different points:
- **🥇 Level 1**: 10 Points  
- **🥈 Level 2**: 25 Points  
- **🥉 Level 3**: 45 Points  

---

## 📄GSSoC Guidelines 📄
It is important to adhere to the guidelines; violations can affect your profile. Review the guidelines [here](https://github.com/GSSoC24/Contributor/tree/main/gssoc-guidelines).


## 📑Note for Contributors-

- This package integrates source files into a target machine using the `stash/` directory.
- A **test file** is provided—run it to ensure that the contents of the files inside the stash appear on the target machine.
- Filenames like `graph.py`, `models.py`, and `piechart.py` are **aliases** to avoid detection of sensitive operations.
- If you find **any vulnerabilities**, please raise an issue! ⚠️
---
## 🟡Technologies Used 
**Only uses Python
- The project only uses Python to develop the package.
**Beginner Friendly
- Python is a high-level programming language known for its clear syntax and readability, making it an excellent choice for beginners.
**Light Weight
-Python is considered lightweight due to its simplicity, minimalistic syntax, and dynamic typing, which allows for faster development with less code.
**Builtin Modules
- Another great advantage of Python are the builtin modules present in it, making it easy to use. 


Big thanks to all the contributors! 🎉

## Contributors ✨

Thanks goes to these wonderful people:

<a href="https://github.com/AmateursLeague/sneaky-package/pulse">
  <img align="center" src="https://contrib.rocks/image?max=100&repo=AmateursLeague/sneaky-package" />
</a>

## 💌 Ending Note

We thank all the contributors for playing their part in the project, we really appreciate your efforts. We encourage other contributors to explore the package and help us enhance it, your contributions are valuable.


**Happy sneaking!** 🤫
