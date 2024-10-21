from setuptools import setup, find_packages
from pathlib import Path

# Read the long description from README.md
long_description = (Path(__file__).parent / "README.md").read_text()

setup(
    name='custom_package_name',
    version='0.1',
    packages=find_packages(),
    description='Your custom description',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='custom_author_name',
    author_email='youremail@gmail.com',
    url='https://github.com/yourusername/custom_package_name',  # Add project URL
    license='GPL 3.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.8',
    install_requires=[
        # Add dependencies here, e.g. 'requests', 'numpy'
    ],
    entry_points={
        'console_scripts': [
            'custom_command=package.module:function',  # Add CLI tool if needed
        ],
    },
    include_package_data=True,  # Include non-code files specified in MANIFEST.in
)
