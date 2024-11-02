# **Development Environment Setup**

## Cloning the Repository

To create a local copy of the **Sneaky Package**, follow these simple steps:

1. **Open your terminal** (or command prompt).
2. **Navigate to the directory** where you want to store the project. You can use the `cd` command to change directories.
3. **Run the following command** to clone the repository:

   ```bash
   git clone https://github.com/AmateursLeague/sneaky-package.git
   cd sneaky-package
   ```

   This command will download the repository into a folder named `sneaky-package`. You can now navigate into this folder to start working on the project.

## Setting Up Your Development Environment

Now that you have the repository, follow these steps to set up your development environment:

1. **Run the install script**: This script installs all the necessary software dependencies for the project. In your terminal, enter:

   ```bash
   ./install.sh
   ```

2. **Explore the project**: After the dependencies are installed, feel free to propose changes, fix any bugs, or add new features!

3. **Store files**: If you have any files you want to integrate into another machine, place them in the `package/stash` directory.

4. **Register on PyPI**: Go to the [PyPI website](https://pypi.org/) to create an account. After registering, generate an API token and make sure to store it securely.

5. **Run the build script**: Finally, run the build script to package your project for deployment. Use this command:

   ```bash
   ./build.sh
   ```

   This script will ask you for some information, including the package name, version, description, author name, email, and your API token. Enter this information, and your package will be deployed to PyPI!

By following these steps, you'll have a fully set up development environment, allowing you to easily enhance the **Sneaky Package**. If you have any questions along the way, don't hesitate to ask for help!