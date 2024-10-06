# PyPi setup 

## 1. Introduction

In this guide, We will provide you with a comprehensive overview of how to set up and deploy a Python package to the Python Package Index (PyPI). This package is designed to facilitate the sharing of Python projects, enabling you to install it easily using pip.

### Purpose

The objectives of this guide is to help you to:

- Understand the necessary setup for your package
- Deploy your package to PyPI
- Install your package easily on any system

## 2. Pre-requisites

Before you begin, ensure that you have the following tools installed:

### Required Tools

- **Python** (version 3.6 or above)
- **pip** (Python package manager)
- **setuptools**, **wheel**, **twine** (for building and uploading packages)

## 3. Installations

To prepare your environment, upgrade pip, setuptools, and wheel:

```bash
sudo python -m pip install --upgrade pip setuptools wheel
```

Next, install `tqdm` and `Twine`:

```bash
sudo python -m pip install tqdm
sudo python -m pip install --user --upgrade twine
```

These tools are essential for building and uploading your package.

## 4. Project Structure

```
sneaky_package/
│
├── .github/                              # GitHub-specific files
│   ├── BUG_report_issue_template.md      # Template for bug reports
│   ├── Feature_request_issue_template.md # Template for feature requests
│   ├── changes_in_code_issue_template.md # Template for code change issues
│   └── pull_request_template.md          # Template for pull requests
│
├── package/                              # Main package directory
│   ├── __init__.py                       # Required for package initialization
│   ├── clp.py                            # Module for CLP functionality
│   ├── display.py                        # Module for display-related functions
│   ├── graph.py                          # Module for graph-related functions
│   ├── models.py                         # Module containing data models
│   ├── piechart.py                       # Module for pie chart functionalities
│   └── test.py                           # Test script for testing package modules
│
├── .gitignore                            # Specifies files to ignore in Git
├── CHANGELOG.md                          # Log of changes made to the project
├── CODE_OF_CONDUCT.md                    # Code of conduct for contributors
├── LICENSE                               # License information for the project
├── README.md                             # Documentation about the project
└── setup.py                              # Setup script for packaging the project

```
### Note
Feel free to change any filenames or directory names to better suit your needs. 

The filenames in the stash/ directory are aliases, you can modify them as necessary!

### Explanation of Key Files

- **.github/**: Contains templates for issues and pull requests to streamline contributions.
- **.gitignore**: Lists files and directories that should not be tracked by Git.
- **changelog.md**: Documents significant changes and updates made to the project over time.
- **code_of_conduct.md**: Outlines expected behavior and guidelines for contributors.
- **setup.py**: Contains package information and dependencies.
- **license**: Specifies the licensing terms under which the project is distributed.
- **readme.md**: Provides an overview of the project, installation instructions, usage
guidelines, and other relevant information.
- **setup.py**: Contains metadata about the package and instructions on how to install it.

## 5. Building the Package

### Step-by-Step Instructions

1. Create or update the `setup.py` file in the root directory using the following structure:

```python
from setuptools import setup, find_packages

setup(
    name='custom_package_name',            # Replace with your actual package name
    version='0.1',                         # Update version as needed
    packages=find_packages(),              # Automatically find package directories
    description='Your custom description', # Provide a brief description of your package
    author='custom_author_name',           # Add your name or organization
    author_email='youremail@gmail.com',    # Add your email address
    license='GPL 3.0',                     # Specify the license type
    install_requires=[                     # List any package dependencies here
        # e.g., 'numpy>=1.18.0',
    ],
)

```

**Note:** 
Ensure that your package's structure is correct and that the `setup.py` file is properly configured.

2. Build the Package by running:

```bash
python setup.py sdist bdist_wheel
```

This command will create a `dist/` directory containing `.tar.gz` and `.whl` files.

## 6. Uploading to PyPI

### Detailed Steps for Deployment

1. **Create a PyPI Account**:

   - Go to [PyPI](https://pypi.org/) and click on "Register" to create an account if you don’t have one.

      ![image](https://github.com/user-attachments/assets/cfbaadf6-3edc-4416-9481-72626b63a96c)

   - Fill in the required information (username, password, email) and click on Create Account.
   - After logging in, verify your email address by clicking on the link sent to your email.
   - Once verified, go to your account settings and navigate to the API tokens section.

      ![image](https://github.com/user-attachments/assets/cda0d120-5659-4a86-b265-885f70221bd7)

   ### NOTE: To create an API token, you must enable Two-factor Authentication

   - Click on "Add API token" to generate a new token. This token will be used for authentication when uploading packages.

      ![image](https://github.com/user-attachments/assets/fd3eff02-94b4-461e-bb11-ee2cd580773b)

      under "select scope", select your project.


1. **Upload the Package Using Twine**:

    - First, ensure you have Twine installed. If not, you can install it using pip:
     ```bash
     pip install twine
     ```
   - Next, navigate to the directory containing your package files in the terminal.
   - Create a source distribution of your package by running:
     ```bash
     python setup.py sdist
     ```
   - Use your API token for authentication when uploading:
     ```bash
     twine upload dist/* --username __token__ --password <YOUR_API_TOKEN>
     ```
   - Replace `<YOUR_API_TOKEN>` with the actual token you generated earlier.
   - You should see a confirmation message once the upload is successful.


3. Make sure Twine is installed and run:

```bash
twine upload dist/*
```

This command will prompt you for your PyPI credentials. If you haven't logged in yet, you'll need to enter them.

### Optional: Upload Using PyPI API Token

1. Create an API Token on PyPI:
   - Log into your PyPI account.
   - Go to Account Settings and generate an API token.
   - Store the token securely.

2. Upload Package with API Token:

```bash
twine upload dist/* --username __token__ --password <YOUR_API_TOKEN>
```

Replace `<YOUR_API_TOKEN>` with your generated token.

## 7. Installation Instructions

Once your package is deployed, users can install it via pip:

```bash
pip install your_package_name
```

This command will download and install the latest version of your package from PyPI.

## 8. Troubleshooting

### Common Issues and Solutions

- **Issue**: Build fails due to missing setuptools or wheel  
  **Solution**: Ensure you have the latest versions installed:
  
  ```bash
  python -m pip install --upgrade setuptools wheel
  ```

- **Issue**: Twine upload failed with authentication error  
  **Solution**: Verify that you are using the correct PyPI token; regenerate it if necessary.

- **Issue**: Unable to find package after uploading  
  **Solution**: Double-check that the package name in your `setup.py` matches what was uploaded on PyPI.

- **Issue**: Invalid version error  
  **Solution**: Ensure your version number follows the correct format (e.g., `0.1`, `1.0.0`).
