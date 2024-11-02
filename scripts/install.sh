#!/bin/bash

# Adding colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print an error and exit
error_exit() {
    echo -e "${RED}Error: $1${NC}"
    exit 1
}

# Check if Python 3 is installed
if ! command -v python3 >/dev/null 2>&1; then
    error_exit "Python 3 is not installed. Please install Python 3.6 or above."
fi

# Get the Python version
python_version=$(python3 --version 2>&1 | awk '{print $2}')

# Check if the Python version is less than 3.6
if [[ $(echo "${python_version}" | awk -F. '{printf "%d%02d", $1, $2}') -lt 306 ]]; then
    error_exit "Python version detected: ${python_version}. Please upgrade to Python 3.6 or above."
fi

# Check if pip for Python 3 is installed
if ! command -v pip3 >/dev/null 2>&1; then
    error_exit "pip for Python 3 is not installed. Please install pip."
fi

# Upgrade pip, setuptools, and wheel
echo -e "${YELLOW}Upgrading pip, setuptools, and wheel...${NC}"
if ! python3 -m pip install --upgrade pip setuptools wheel --user; then
    error_exit "Upgrading pip, setuptools, and wheel failed."
fi

# Install tqdm
echo -e "${YELLOW}Installing tqdm...${NC}"
if ! python3 -m pip install tqdm --user; then
    error_exit "Installation of tqdm failed. Please check your network connection."
fi

# Install twine
echo -e "${YELLOW}Installing twine...${NC}"
if ! python3 -m pip install --user --upgrade twine; then
    error_exit "Installation of twine failed."
fi

echo -e "${GREEN}Installation complete!${NC}"
