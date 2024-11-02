#!/bin/bash

# Check python version
python_version=$(python --version 2>&1 | awk '{print $2}')

if [[ ! $(python3 --version 2>&1) ]]; then
  echo "Error: Python 3 is not installed. Please install Python 3.6 or above."
  exit 1
fi

if [[ $(echo "${python_version}" | grep -Eo '[0-9]+\.[0-9]+') > "3.6" ]]; then
  echo "Error: Python version detected: ${python_version}. Please upgrade to Python 3.6 or above."
  exit 1
fi

# Check pip
if ! command -v pip >/dev/null 2>&1; then
  echo "Error: pip is not installed. Please install pip for Python 3."
  exit 1
fi

# Upgrade pip, setuptools, and wheel
echo "Upgrading pip, setuptools, and wheel..."
python -m pip install --upgrade pip setuptools wheel --user || {
  echo "Error: Upgrading pip, setuptools, and wheel failed."
  exit 1
}

# Install tqdm
echo "Installing tqdm..."
python -m pip install tqdm || {
  echo "Error: Installation of tqdm failed. Please check network connectivity."
  exit 1
}

# Install twine with user flag
echo "Installing twine..."
python -m pip install --user --upgrade twine || {
  echo "Error: Installation of twine failed."
  exit 1
}

echo "Installation complete!"