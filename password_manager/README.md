# Password Manager

This is a simple **Password Manager** application created using Python's `tkinter` library. It allows users to generate strong, random passwords and save their website credentials (website, email/username, and password) locally in a file.

### This project is for learning purpose only. Do not save your passwords locally in a non-encrypted file!

## Features

- **Password Generator**: Generate a random 15-character password using a combination of letters, numbers, and special characters.
- **Save Passwords**: After entering details, users can save their website credentials to a `data.txt` file.
- **Graphical User Interface (GUI)**: Built using `tkinter`, providing a simple and user-friendly interface.
- **Error Handling**: Alerts the user if any required fields are left empty before saving.

## How to Run

1. Clone this repository or download the code files.
2. Make sure you have Python installed on your system. This app uses Python's built-in libraries, so no external dependencies are required.
3. Run the script:

    ```bash
    python password_manager.py
    ```

4. A GUI window will open where you can:
   - Enter the website, email/username, and password.
   - Use the **Generate Password** button to create a random password.
   - Save the information by clicking **Add**.

5. The saved credentials will be stored in a file named `data.txt` in the same directory as the script.

## File Structure

- `password_manager.py`: Main script containing the code for the password manager.
- `logo.png`: Image file used as the logo in the GUI.
- `data.txt`: This file is created automatically when you save a password. It contains the saved credentials.

## GUI Layout

- The window has fields for:
  - **Website**
  - **Email/Username**
  - **Password**
- Buttons include:
  - **Generate Password**: Generates a 15-character random password.
  - **Add**: Saves the entered website, email, and password to `data.txt`.

## Requirements

- Python 3.x
- `tkinter` (comes pre-installed with Python)
- A PNG logo file (`logo.png`) for the application

## License

This project is part of the "100 Days of Code: The Complete Python Pro Bootcamp" from Dr. Angela Yu
