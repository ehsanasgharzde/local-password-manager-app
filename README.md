# Simple Local Password Manager with Python and Tkinter

This is a basic password manager application created with Python and Tkinter. It allows you to generate strong passwords and store website login information locally in a text file.

## Features

- Generate strong passwords with random characters.
- Save website, username/email, and password information.
- Store data locally in a text file for easy access.

## Files

- `main.py`: The Python script containing the password manager application.
- `PasswordLog.txt`: A text file where the saved website login information is stored.

## How to Use

1. Run `main.py` using Python.
2. Enter the website, username/email, and password.
3. Click the "Generate Password" button to create a strong password.
4. Click the "Add" button to save the website login information to `PasswordLog.txt`.

## Requirements

- Python 3.x
- tkinter library (usually included with Python)
- pyperclip library (to copy generated passwords to the clipboard)

## Usage Notes

- Make sure to keep the `PasswordLog.txt` file secure as it contains your login information.
- You can customize the character sets and password length in the `passwordgenerator` function in `main.py`.

## Disclaimer

This is a basic password manager for personal use. It is recommended to use more secure and dedicated password management tools for sensitive or critical data.
