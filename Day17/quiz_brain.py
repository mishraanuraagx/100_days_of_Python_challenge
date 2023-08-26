from question_model import Question
from random import shuffle

class QuizBrain:
    def __init__(self, question_bank: [Question]):
        self.question_bank = question_bank
        shuffle(self.question_bank)
        self.question_number = 0
        self.score = 0

    def check_answer(self, question: Question, answer):
        if answer.lower() == question.answer.lower():
            self.score += 1
            print("You got it right!")
            return True
        else:
            print("You answered it wrong.")
            return False

    def end_of_quiz(self):
        if len(self.question_bank) == 0:
            return True
        return False

    def ask_question(self):
        self.question_number += 1
        question = self.question_bank.pop(0)
        user_response = input(f"{self.question_number}: {question.question} (True/False): ")
        correct = self.check_answer(question, user_response)
        print(f"Correct Answer was: {question.answer}")
        print(f"Score: {self.score}/{self.question_number}'")
