# Python Basics

## What is Python?

Python is a high-level, interpreted, and general-purpose programming language.
It was created to be simple, readable, and easy to learn.

Python is widely used in:

- Web Development
- Automation and Scripting
- Data Science and Machine Learning
- Artificial Intelligence
- DevOps and Cloud Computing
- Desktop and Game Development

---

## Why Python?

- Easy to learn and beginner-friendly
- Simple and readable syntax
- Large standard library
- Huge community support
- Cross-platform (Linux, Windows, macOS)
- Used by beginners and professionals

---

## How Python Works

- Python code is written in files with `.py` extension
- The Python interpreter reads and executes the code line by line
- No manual compilation step is required

---

## Checking Python Installation

To check if Python is installed, open a terminal and run:

    python3 --version

or

    python --version

If Python is installed, the version number will be displayed.

---

## Installing Python on Linux (Ubuntu / Debian)

Update the package list:

    sudo apt update

Install Python:

    sudo apt install python3

Install pip (Python package manager):

    sudo apt install python3-pip

Verify installation:

    python3 --version
    pip3 --version

---

## Running Your First Python Program

Create a Python file:

    nano hello.py

Write the following code in the file:

    print("Hello, Python!")

Save the file and run:

    python3 hello.py

---

## Python Virtual Environment (venv)

A virtual environment is an isolated Python environment used to manage dependencies
for a specific project.

---

## Why Use a Virtual Environment?

- Avoid dependency conflicts
- Keep system Python clean
- Different projects can use different packages

---

## Creating a Virtual Environment

    python3 -m venv venv

---

## Activating the Virtual Environment

    source venv/bin/activate

After activation, `(venv)` will appear in the terminal.

---

## Deactivating the Virtual Environment

    deactivate

---

## Installing Python Packages

With the virtual environment activated, install packages using pip:

    pip install package_name

Example:

    pip install requests

---

## Listing Installed Packages

    pip list

---

## Conclusion

Python is a powerful, flexible, and beginner-friendly programming language.
Using virtual environments and proper package management is a best practice.
