# Contribution Guidelines for Sneaky Package

## Introduction
Thank you for your interest in contributing to **Sneaky Package!** This project is nothing more than a lightweight & faster Python package that aims to highlight and improve security by demonstrating potential vulnerabilities in the system when connected with pip. Your contributions—whether they be code, documentation, or feedback—help foster a collaborative environment and drive innovation in our project.


Please follow the guidelines below to ensure a smooth contribution process.

## Getting Started
To contribute to the Sneaky Package, follow these steps to set up your development environment:

1. Fork this repository to your GitHub account by clicking the "Fork" button in the top right.

2. **Clone the Repository**:
   Open your terminal and run:
   ```bash
   git clone https://github.com/YOUR-USERNAME/sneaky-package
   cd sneaky-package
   ```

3. **Install Prerequisites**:
   Ensure you have the following installed:
   - Python 3.x
   - pip (Python package installer)
     

4. **Install the package:**
   Open your terminal and run:
   ```bash
   pip install matplotlib_visual
   ```  

   Create a file or open Python in the terminal and enter the following code:
   ```bash
   from matplotlib_visual.display import featureName  
   featureName("fileName", 1234) # password integer
   ```  

      - `display` - A method that contains features  
      - `featureName` - Check out `display.py` in the repo and use the required method name (feature).

## Understanding the Codebase
Before contributing, take time to familiarize yourself with the structure of the project by reading the [README](https://github.com/AmateursLeague/sneaky-package/blob/main/README.md) file. 
   - This project is **beginner-friendly** with most features implemented in **minimal lines of code**.
   - Codebase is compact, lightweight and faster.  
   - Research thoroughly to understand how to implement stealthy features.
   - Review comments and docstrings within the code to grasp how each component works.

## How to Contribute
Follow these steps to make your contributions:

### Step 1: Identify an Issue
First, check for any [existing issues](https://github.com/AmateursLeague/sneaky-package/issues) in the repository. If you want to report a new issue, please make sure to follow the **Issue Template** provided below:

   - **Issue Template:**
      - **Issue Title:** A concise and descriptive title.
      - **Description:** Clear and detailed description of the issue or feature request.
      - **Steps to Reproduce (if applicable):** Detailed steps to reproduce the issue.
      - **Expected Behavior:** What you expected to happen.
      - **Actual Behavior:** What actually happened.

If the issue already exists or you're interested in fixing something, feel free to pick it up.

### Step 2: Fork the Repository
   Click on the "_Fork_" button at the top right of the repository page to create your copy.

### Step 3: Create a Branch
   After cloning your forked repository, create a new branch for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```

### Step 4: Make Changes
   Implement your changes adhering to coding standards and best practices outlined in this project.

### Step 5: Testing
   Write tests for any new features or bug fixes you implement. Ensure all tests pass before submitting your contribution.

## Submitting Contributions
To submit your changes:

1. Commit your changes with a clear message:
   ```bash
   git commit -m "Description of changes made"
   ```

2. Push your branch to your forked repository:
   ```bash
   git push origin feature/your-feature-name
   ```

3. Go to the original repository and click "_Compare & Pull Request_". When submitting the PR, please follow this **PR Format:**

   - **Pull Request Template:**
      - **Title:** Short and descriptive title for your pull request.
      - **Description:** Detailed description of what changes you made and why.
      - **Issue Reference:** Mention the issue number this PR addresses (if applicable).

**4. Code Review & Feedback:**
The project maintainers will review your pull request. You may be asked to make some changes before your PR can be merged. Please respond to the feedback and make the necessary adjustments.

If you have any questions or doubts during the review process, feel free to ask.


## Reporting Issues
If you encounter bugs or have feature suggestions:

- Report them by creating a new issue in the GitHub repository.
- Provide clear and concise descriptions, including steps to reproduce bugs or use cases for feature requests.


## Acknowledgments
We appreciate all contributions! If you have any doubts or need clarification at any point, please feel free to reach out by creating an issue or asking a question in the PR comments.

Happy coding!
---
