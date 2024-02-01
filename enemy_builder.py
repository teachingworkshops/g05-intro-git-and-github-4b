from enemy import Enemy
from assets import Assets
from math_question import math_question
import random

class EnemyBuilder:
    """
    Represents a builder class for enemies
    """
    def build_random_enemy(self, difficulty):
        """
        Builds an enemy based a re a new instance of the Enemy class.

        Args:
            difficulty (int): Difficulty of the question the enemy will have

        Returns 
        Enemy: enemy object
        """
        enemy_id = random.choice(list(Assets.ENEMY_ID))
        e_type = Assets.ENEMY_TYPES[enemy_id]
        art = Assets.ENEMY_ART[enemy_id]
        action =  random.choice(Assets.ENEMY_ACTIONS)
        math_question = math_question.generate_question(difficulty)
        
        return Enemy(e_type, art, action, math_question)




     