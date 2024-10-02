
# Contributing Guidelines 🤝



[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
&nbsp;
[![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/)


# Contributing to sneaky-package

Thank you for considering contributing to sneaky-package! We welcome contributions from the community and are excited to see what you can bring to the project.

## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [How to Contribute](#how-to-contribute)
3. [Creating Issues](#creating-issues)
4. [Writing Better Comments for Issue Assignment](writing-better-comments-for-issue-assignment)
5. [Setting Up Your Development Environment](#setting-up-your-development-environment)
6. [Making Changes](#making-changes)
7. [Submitting Your Changes](#submitting-your-changes)
8. [How to Create Pull Requests](#how-to-create-pull-requests)
9. [Time Limit for Assigned Issue](#time-limit-for-assigned-issues)
10. [Gathering Contributor Information](#gathering-contributor-information)
11. [Style Guide](#style-guide)
12. [Testing](#testing)
13. [Documentation](#documentation)
14. [Contact](#contact)

## Code of Conduct

Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms.

## How to Contribute

**1. Fork the Repository**

Fork the repository to your own GitHub account by clicking the "Fork" button on the top right of the repository page.

**2. Clone the Repository**

Clone the forked repository to your local machine:

```bash
git clone https://github.com/your-username/sneaky-package.git
cd sneaky-package
```

**3. Create a Branch**

Create a new branch for your feature or bug fix:

```bash
git checkout -b feature/your-feature-name
``` 
## Creating Issues

If you've encountered a bug or have a feature request, you can create an issue in the repository:

**1. Clear and Concise Title:**  Use a descriptive title that summarizes the problem or feature request.

**2. Detailed Explanation:** Provide a clear description of the problem, steps to reproduce (if applicable), and expected behavior. For feature requests, explain the purpose and benefits.

**3. Attachments:** Whenever possible, include screenshots, logs, or code snippets that help explain the issue.

**4. Use Templates:** If issue templates are provided, please use them to ensure that all necessary information is included.

This information will help the maintainers understand the context and prioritize the issue appropriately.

## Writing Better Comments for Issue Assignment
When requesting an issue assignment:

**1. Clearly Describe Your Approach:** Briefly explain how you intend to solve the issue or add the feature. This helps maintainers assess whether your approach aligns with the project's needs.

**2. Be Thoughtful and Constructive:** Use professional language, be polite, and ensure that your comments contribute to a positive and collaborative environment.

**3. Explain Your Availability:** Let the maintainers know if you anticipate any delays in solving the issue, so the maintainers can manage the project timeline efficiently.


## Setting Up Your Development Environment

1. Ensure you have Node.js and npm installed. You can download them from [Node.js](https://nodejs.org/).
2. Install the project dependencies:

```bash
npm install
```

3. Start the development server:

```bash
npm start
```

This will start the development server and you can view the application in your browser at `http://localhost:3000`.

## Making Changes

1. Make your changes to the codebase. Ensure that your code follows the project's coding standards.
2. If you are adding a new feature, consider adding tests to cover your changes.
3. Ensure your code passes all existing tests.

## Submitting Your Changes

### 1. Commit Changes

Commit your changes with a descriptive commit message:

```bash
git add .
git commit -m "Add feature: your feature description"
```

### 2. Push Changes

Push your changes to your forked repository:

```bash
git push origin feature/your-feature-name
```
## How to Create Pull Requests
To submit your work:

**1. Fork the Repository:** Ensure your repository is forked and you have created a new branch for your work.

**2. Make Changes and Test:** Make your changes on the new branch, then ensure that everything is working as expected.

**3. Maintain Clean Commit History:** Organize your commits meaningfully and squash or rebase them if necessary. Ensure each commit has a clear and descriptive message explaining the changes.

**4. Link to the Issue:** In the PR description, link the issue you're addressing (if applicable) by referencing the issue number.

**5. Submit PR:** Go to the original repository and create a pull request from your forked repository. Provide a clear and descriptive title and description for your pull request.

**6. Complete any Requested Changes:** If maintainers request changes to your PR, complete them as soon as possible.

## Time Limit for Assigned Issues
Once an issue is assigned, contributors will have 1-2 days to work on the issue and submit a pull request.

- If you're unable to meet this deadline, please communicate with the maintainers as soon as possible to request an extension.
- If you fail to submit the PR or communicate delays within the specified timeframe, the issue may be reassigned to someone else.

## Gathering Contributor Information
To properly acknowledge the efforts of all contributors:

**1. Collect Information:** I will ensure each contributor’s name, GitHub profile link, and the details of their contributions (e.g., bug fixes, features, etc.) are accurately included.

**2. Markdown Syntax for Formatting:** Contributors will be listed using markdown to create a clean and consistent layout. If appropriate, sections will be created for profiles, images, and descriptions of their contributions.

**3. Sorting by Contribution:** Contributors may be sorted based on role or type of contribution (e.g., bug fix, feature implementation) for better readability.

The expected outcome is a well-organized `CONTRIBUTORS.md` file that acknowledges every contributor's effort while maintaining clarity for visitors of the repository.

## Style Guide

- **Code Formatting**: Ensure your code is properly formatted. We use Prettier for code formatting. You can format your code by running:

```bash
npm run format
```
## Testing
Ensure that your code passes all tests before submitting your changes. If you're adding new features, consider writing tests for them.

## Documentation

Update documentation as necessary for any changes you make. This includes updating the README.md file and any other relevant documentation files.

## Contact

If you have any questions or need further assistance, feel free to open an issue or contact the maintainers.

Thank you for your contributions!