from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

game = True
question_bank = []

for questions in question_data:
    question_text = questions["text"]
    question_answer = questions["answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)


while quiz.still_has_questions():
    quiz.next_question()
    quiz.check_score()

print("Thank you for playing!")
print(f"Your final score was {quiz.score}/{quiz.question_number}")