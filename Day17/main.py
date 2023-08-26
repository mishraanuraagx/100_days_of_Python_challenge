from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    question_bank.append(Question(i["text"], i["answer"]))

quiz = QuizBrain(question_bank)
while not quiz.end_of_quiz():
    quiz.ask_question()

print(f"Quiz is over. Your final score: {quiz.score}/{quiz.question_number}")