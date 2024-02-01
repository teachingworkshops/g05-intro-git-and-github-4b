import random
from assets import Assets

class MathQuestion:

    # Dictionary keeping track of the used questions for each difficulty
    used_questions = {0: set(), 1: set(), 2: set()}

    @staticmethod
    def generate_question(difficulty):

        # Checks for difficulty and chooses set accordingly
        if difficulty == 0:
            available_questions = set(Assets.easy_questions)
        elif difficulty == 1:
            available_questions = set(Assets.medium_questions)
        elif difficulty == 2:
            available_questions = set(Assets.hard_questions)

        # Makes set with only unused questions
        unused_questions = available_questions - MathQuestion.used_questions[difficulty]

        # Chooses random question from unused questions list
        question, correct_answer = random.choice(list(unused_questions))

        # Marks questions as answered
        MathQuestion.used_questions[difficulty].add((question, correct_answer))

        return question, correct_answer

