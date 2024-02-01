import random
from assets import Assets

class MathQuestion:
    """
        Gives out a math question
    """

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
        if 1 <= difficulty <= 6:
            question, correct_answer = random.choice(Assets.easy_questions)
        elif 7 <= difficulty <= 12:
            question, correct_answer = random.choice(Assets.medium_questions)
        elif difficulty >= 13:
            question, correct_answer = random.choice(Assets.hard_questions)
        elif difficulty == 0:
            question, correct_answer = random.choice(Assets.boss_questions)

        return question, correct_answer
