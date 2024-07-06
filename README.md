# sneaky-package 🥸
This is my side project, that exploits the permissions and vulnerabilities of **pip** packages, which is capable of sneaking in *sensitive information, source code or any malware* inside a local machine.

## How it works?
- Well, this basically **functions like a Python package** and we use certain methods that triggers the respective operations.
- It has few features that's especially for **integrating source into secured environment** without getting caught.
- This repository holds the codebase that has already incorporated few features, but **feel free to fork and change the codebase** as you see fit.

## Getting started!

### **Install:**
```bash
pip install matplotlib-visual
```
> **Note:** This `matplotlib-visual` has already been implemented by me, you can officially install it in your PC. However this package holds information that were relevant to me and it won't be useful for new user, so I recommend you to fork and change the repository and upload your own package.

### **Executing Package:**
1. Create a `python` file and enter any one of the codes below
2. Or you can open a terminal and work on python without creating a `python` this command:
```bash
python
```

So far, I have incorporated features that can let you get source code into machine. But sneaking in such source code can be made in some ways, they are:
- **Displaying source code** in console output.
```python
    from matplotlib_visual.models import display
    display("<filename-without-extension>")
```
>*models method displays source code*
- **Stealth Copy to Clipboard**, which is more secure.

```python
    from matplotlib_visual.graph import display
    display("<filename-without-extension>")
```
> *graph* copies the source code into system's clipboard

- **Writing the source code** into the program's root directory.
```python
    from matplotlib_visual.piechart import display
    display("<filename-without-extension>")
```


# Contributing

Anyone can contribute to this project, or they can fork and work on their own project. If you have any ideas to enhance this project to it's stealthy development, feel free to submit a pull request.

**Remember the key is to keep it discreet!** 

# License

This package operates under the [GPL 3.0](https://www.gnu.org/licenses/gpl-3.0.en.html) , allowing you to sneakily use and modify it as needed.

Happy sneaking! 🕵️‍♂️🤫

