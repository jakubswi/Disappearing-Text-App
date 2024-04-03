# Disappearing Text App

This is a simple Python application built using the Tkinter library. The Disappearing Text App allows users to input text, and if they stop typing, the text will disappear after a certain period.

## How to Use

1. **Installation**: Ensure you have Python installed on your system.

2. **Clone the Repository**: Clone this repository to your local machine using the following command:

    ```
    git clone https://github.com/jakubswi/Disappearing-Text-App.git
    ```

3. **Navigate to the Directory**: Navigate to the directory where you cloned the repository.

    ```
    cd Disappearing-Text-App
    ```

4. **Run the Application**: Run the application by executing the following command:

    ```
    python app.py
    ```

## Features

- Input text into the text area.
- If typing stops, the text will disappear after 5 seconds.
- Text area is scrollable to accommodate large amounts of text.

## Dependencies

This application requires the following dependencies:

- Python 3.x
- Tkinter

## Usage

1. Run the application.
2. Type text into the text area.
3. If typing stops, the text will automatically disappear after 5 seconds.
4. To clear the text manually, simply delete it or press backspace until it's empty.

## Code Overview

The `app.py` file contains the Python code for the application. Here's a brief overview of the code:

- The `DisappearingTextApp` class initializes the Tkinter window and sets up the UI components.
- The `check_input` method is responsible for checking the input in the text area. If the text changes, it starts a timer to clear the text after 5 seconds.
- The `clear_text` method clears the text area when called.
- The `if __name__ == "__main__":` block creates an instance of the `DisappearingTextApp` class and binds the `check_input` method to the `<KeyRelease>` event of the text area.


## License

This project is licensed under the [MIT License](LICENSE).
