#!/bin/bash

# Check if Python 3 is installed
if ! command -v python3 >/dev/null 2>&1; then
  echo "Error: Python 3 is not installed. Please install Python 3.6 or above."
  exit 1
fi

# Get the Python version
python_version=$(python3 --version 2>&1 | awk '{print $2}')

# Check if the Python version is less than 3.6
if [[ $(echo "${python_version}" | awk -F. '{printf "%d%02d", $1, $2}') -lt 306 ]]; then
  echo "Error: Python version detected: ${python_version}. Please upgrade to Python 3.6 or above."
  exit 1
fi

# Check pip
if ! command -v pip3 >/dev/null 2>&1; then
  echo "Error: pip is not installed. Please install pip for Python 3."
  exit 1
fi

# Upgrade pip, setuptools, and wheel
echo "Upgrading pip, setuptools, and wheel..."
python3 -m pip install --upgrade pip setuptools wheel --user || {
  echo "Error: Upgrading pip, setuptools, and wheel failed."
  exit 1
}

# Install tqdm
echo "Installing tqdm..."
python3 -m pip install tqdm --user || {
  echo "Error: Installation of tqdm failed. Please check network connectivity."
  exit 1
}

# Install twine with user flag
echo "Installing twine..."
python3 -m pip install --user --upgrade twine || {
  echo "Error: Installation of twine failed."
  exit 1
}

echo "Installation complete!"
