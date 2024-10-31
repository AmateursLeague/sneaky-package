import os
import subprocess
import sys
from dotenv import load_dotenv

load_dotenv()

# Getting package details from environment variables
package_name = os.getenv("PACKAGE_NAME")
version = os.getenv("VERSION")
author_name = os.getenv("AUTHOR_NAME")
author_email = os.getenv("AUTHOR_EMAIL")
description = os.getenv("DESCRIPTION", "")  # this is optional
url = os.getenv("URL")
    
if not url:
    url = input("Enter your Forked GitHub URL: ")

# Checking if all fields are provided
if not all([package_name, version, author_name, author_email, url]):
    print("Error: Please ensure PACKAGE_NAME, VERSION, AUTHOR_NAME, AUTHOR_EMAIL, and URL are set.")
    sys.exit(1)

# Create setup.py content dynamically
setup_content = f"""
from setuptools import setup, find_packages

setup(
    name="{package_name}",
    version="{version}",
    packages=find_packages(),
    description="{description}",
    author="{author_name}",
    author_email="{author_email}",
    license="GPL 3.0",
    install_requires=[],
    url="{url}"
)
"""

# Add the credentials to setup.py to the current directory
with open("setup.py", "w") as f:
    f.write(setup_content)

# Building the package
print("Building the package...")
subprocess.run(["python", "setup.py", "sdist", "bdist_wheel"], check=True)

print("Package build complete!") 