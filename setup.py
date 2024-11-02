from setuptools import setup, find_packages

setup(
    name="custom_package_name",  # Replace with your actual package name
    version="0.1",
    packages=find_packages(),  # Automatically find and include all packages in the project
    description="Your custom description",  # Replace with a meaningful description of your package
    author="custom_author_name",  # Replace with your actual name
    author_email="youremail@gmail.com",  # Replace with your actual email address
    license="GPL-3.0",  # Use a hyphen instead of a space for the license
    classifiers=[  # Optional: add classifiers to specify the package's audience
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPL-3.0)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Specify the minimum Python version required
    install_requires=[  # List your package dependencies here
        # Example: "numpy>=1.18.0",
    ],
    include_package_data=True,  # Include non-code files specified in MANIFEST.in
    zip_safe=False,  # If the package can be reliably used if installed as a .egg file
)
