import random
from assets import Assets

class math_question:
    
    @staticmethod
    def generate_question(difficulty):
        if difficulty == 0:
            question, correct_answer = random.choice(Assets.easy_questions)
        elif difficulty == 1:
            question, correct_answer = random.choice(Assets.medium_questions)
        elif difficulty == 2:
            question, correct_answer = random.choice(Assets.hard_questions)
        
        return question, correct_answer

"""
TESTING

difficulty = 1
problem = math_question.generate_question(difficulty)

print("Question:", problem[0])
user_answer = input("Your answer: ")

if user_answer == problem[1]:
    print("Correct")
else:
    print("Incorrect. Correct answer:", problem[1])

"""
