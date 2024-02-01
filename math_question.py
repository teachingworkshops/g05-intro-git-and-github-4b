import random
from assets import Assets

class MathQuestion:
    """
        Gives out a math question
    """
    # Dictionary keeping track of the used questions for each difficulty
    used_questions = {0: set(), 1: set(), 2: set()}

    @staticmethod
    def generate_question(difficulty):
        """
        Generates a question based on the alloted difficulty.
        Difficulty values with correspondence:
        0 = boss
        1-6 = easy
        7-12 = medium
        13+ = hard

        Args: 
            difficulty (int): Incremented in order to change the difficulty of the questions.

        Returns:
            string array containing question, correct_answer
            
        """
        
        # Checks for difficulty and chooses set accordingly
        if difficulty >= 1 and difficulty <= 6:
            available_questions = set(Assets.easy_questions)
        elif difficulty >= 7 and difficulty <= 12:
            available_questions = set(Assets.medium_questions)
        elif difficulty >= 13:
            available_questions = set(Assets.hard_questions)
        elif difficulty == 0:
            available_questions = set(Assets.boss_questions)

        # Makes set with only unused questions
        unused_questions = available_questions - MathQuestion.used_questions[difficulty]

        # Chooses random question from unused questions list
        question, correct_answer = random.choice(list(unused_questions))

        # Marks questions as answered
        MathQuestion.used_questions[difficulty].add((question, correct_answer))

        return question, correct_answer

