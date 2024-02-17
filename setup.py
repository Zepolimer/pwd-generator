from pathlib import Path

import setuptools
from pkg_resources import parse_requirements

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pwd_generator",
    version='0.0.1',
    author="Rémi Lopez",
    author_email="contact.remilopez@gmail.com",
    description="An open-source password generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pwd-generator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    include_package_data=True,
)
