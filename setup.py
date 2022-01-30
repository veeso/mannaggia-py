#!/usr/bin/python3

from setuptools import find_packages, setup
from pathlib import Path

# The directory containing this file
ROOT = Path(__file__).parent

README = (ROOT / "README.md").read_text(encoding="utf-8")

setup(
    name="mannaggia",
    version="0.1.4",
    description="mannaggia is a python application to praise or more likely to curse the saints.",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Christian veeso Visintin",
    author_email="christian.visintin1997@gmail.com",
    url="https://github.com/veeso/mannaggia-py",
    license="WTFPL",
    python_requires=">=3.5",
    include_package_data=True,
    install_requires=[
        "appdirs>=1.4.0",
        "click>=8.0.0",
        "pydub>=0.20.0",
        "requests>=2.20.0",
        "pathlib2>=2",
        "simpleaudio>=1.0.0",
    ],
    entry_points={"console_scripts": ["mannaggia = mannaggia.__main__:main"]},
    packages=find_packages(),
    keywords=["mannaggia", "debugging-tools", "italian-debugging-tool"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
    ],
)
