# Quiz Game README

This Python script is a simple quiz game that utilizes a question bank containing various questions and their respective answers. Players are presented with questions one by one and must provide answers. After completing the quiz, the player's final score is displayed.

## Getting Started

To use this quiz game, follow these steps:

1. Ensure you have Python installed on your computer. You can download it from [Python's official website](https://www.python.org/).

2. Clone or download this repository to your local machine.

3. Navigate to the directory where the script is located using the command line or terminal.

4. Run the script by executing the following command:

```bash
python quiz_game.py
```

## How to Play

1. Upon running the script, the quiz game will start automatically.

2. You will be presented with questions one by one.

3. Input your answer for each question.

4. After answering all the questions, your final score will be displayed.

5. Enjoy the game and challenge yourself to improve your score!

## Modifying the Quiz

If you wish to customize the quiz by adding your own questions or modifying the existing ones, you can do so by editing the `question_data.py` file. Follow the format of the existing questions:

```python
question_data = [
    {"text": "Question text goes here.", "answer": "Correct answer goes here"},
    {"text": "Another question text.", "answer": "Correct answer goes here"},
    # Add more questions as needed
]
```

Ensure that each question is a dictionary with keys `"text"` and `"answer"`, representing the question text and its corresponding answer, respectively.

## Files

- `quiz_game.py`: The main Python script that runs the quiz game.
- `question_data.py`: Contains the data for the quiz questions.
- `question_model.py`: Defines the Question class used to create question objects.
- `quiz_brain.py`: Implements the QuizBrain class responsible for managing the quiz flow and checking answers.
