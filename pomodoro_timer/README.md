# Pomodoro Timer

This is a simple **Pomodoro Timer** application built using Python and Tkinter. The Pomodoro technique is a time management method where you work for a set period of time (usually 25 minutes), followed by a short break (5 minutes), and after a few cycles, you take a longer break. In this timer, you can customize the work and break durations, and it will automatically alternate between work and break intervals.

## Features

- **Work Sessions**: Set for 50 minutes by default.
- **Short Breaks**: After each work session, you get a 10-minute break.
- **Long Breaks**: After four work sessions, you get a longer 20-minute break.
- **Visual Timer**: Displays the countdown of work/break sessions.
- **Check Marks**: For every completed work session, a checkmark appears as progress.

## Getting Started

### Prerequisites

You need Python installed on your machine. You can download Python from [here](https://www.python.org/downloads/).

This application uses the `tkinter` library which is bundled with Python, so no additional libraries are needed.

### Installation

1. Clone the repository or download the code.
2. Ensure you have an image named `tomato.png` in the same directory as the script. The image will be displayed as the background of the timer.

### Running the Application

To start the Pomodoro Timer:

1. Open a terminal or command prompt.
2. Navigate to the directory where the code is located.
3. Run the following command:
    ```bash
    python pomodoro.py
    ```
4. The Pomodoro Timer window will open.

### Customization

You can easily customize the durations for the work session, short break, and long break by modifying the following constants at the top of the script:

```python
WORK_MIN = 50  # Work session in minutes
SHORT_BREAK_MIN = 10  # Short break in minutes
LONG_BREAK_MIN = 20  # Long break in minutes
```

### Usage
- **Start Timer**: Press the "Start" button to begin the timer.
- **Reset Timer**: Press the "Reset" button to reset the timer and the progress.
- **Visual Feedback**: Checkmarks will be displayed for each completed work session.

### Files
- **tomato.png**: The image displayed in the UI to represent the Pomodoro method.

## License
This project is part of the "100 Days of Code: The Complete Python Pro Bootcamp" from Dr. Angela Yu
