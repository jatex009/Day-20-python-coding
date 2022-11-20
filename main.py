from question_model import Question
from File.data import question_data
from quiz_brain import Quizbrain

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

quiz = Quizbrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the Quiz")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")