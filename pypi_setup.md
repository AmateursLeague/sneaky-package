# PyPi setup 

## 1. Introduction

This documentation provides a comprehensive guide on how to set up and deploy a Python package to the Python Package Index (PyPI). The package is designed to facilitate the sharing of Python projects, enabling users to install it easily using pip.

### Purpose

The objectives of this guide are to help users:

- Understand the necessary setup for the package
- Deploy the package to PyPI
- Install the package effortlessly on any system

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

Here’s an example of a basic project structure for a Python package:

```
my_package/
│
├── setup.py              # Setup script for packaging
├── README.md             # Package documentation
├── LICENSE               # License for the package
├── my_package/           # Main package directory
│   ├── __init__.py       # Required for the package
│   └── module.py         # Your module code
└── tests/                # Unit tests for the package
    └── test_module.py    # Example test file
```

### Explanation of Key Files

- **setup.py**: Contains package information and dependencies.
- **README.md**: Provides information about the package.
- **my_package/**: Directory containing the actual Python code.
- **tests/**: Directory for unit testing your package.

## 5. Building the Package

### Step-by-Step Instructions

1. Create a `setup.py` file in the root directory with the following content:

```python
from setuptools import setup, find_packages

setup(
    name='your_package_name',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Add any package dependencies here
    ],
    # You can also add metadata like author, license, etc.
)
```

**Note:** Ensure that your package's structure is correct and that the `setup.py` file is properly configured.

2. Build the Package by running:

```bash
python setup.py sdist bdist_wheel
```

This command will create a `dist/` directory containing `.tar.gz` and `.whl` files.

## 6. Uploading to PyPI

### Detailed Steps for Deployment

1. **Create a PyPI Account**:
   - Go to PyPI and create an account if you don’t have one.
   - After logging in, generate an API token via your account settings.

2. **Upload the Package Using Twine**:
   - Use your API token for authentication:

```bash
twine upload dist/* --username __token__ --password <YOUR_API_TOKEN>
```

Replace `<YOUR_API_TOKEN>` with the actual token copied from your PyPI account.

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

After adding all these sections to your `pypi_setup.md` file, save it. Then commit the file to your repository:

```bash
git add pypi_setup.md
git commit -m "Add documentation for PyPI package setup and deployment"
git push
```

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

Citations:

[1] https://packaging.python.org/en/latest/tutorials/packaging-projects/

[2] https://dev.to/mmphego/how-i-published-deployed-my-python-package-to-pypi-easily-3hio

[3] https://www.freecodecamp.org/news/how-to-create-and-upload-your-first-python-package-to-pypi/

[4] https://stackoverflow.com/questions/3658084/how-to-create-upload-and-install-a-package-for-pypi

[5] https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/

[6] https://www.youtube.com/watch?v=h6oa_FwzFwU

[7] https://realpython.com/pypi-publish-python-package/

[8] https://pypi.org/project/python-deploy/
