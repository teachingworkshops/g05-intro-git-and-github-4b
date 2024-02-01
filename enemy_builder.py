from enemy import Enemy
from assets import Assets
from math_question import MathQuestion
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
        math_question = MathQuestion.generate_question(difficulty)

        return Enemy(e_type, art, action, math_question)
    
    
    def build_boss(self):
        """
        Builds the map boss.

        Returns 
        Enemy: enemy object
        """
        e_type = Assets.BOSS_NAME
        art = Assets.BOSS_ART
        action =  Assets.BOSS_ACTION
        boss_question = random.choice(Assets.boss_questions)

        return Enemy(e_type, art, action, boss_question)    




     