from enemy import Enemy
from assets import Assets
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
        # TODO: Difficulty handling
        return Enemy(e_type, art, action, "math_problem")
 
if __name__ == "__main__":
    e = EnemyBuilder()
    enemy_instance = e.build_random_enemy(1)      
    print(enemy_instance.enemy_type)
    print(enemy_instance.art)
    print(enemy_instance.action)
    print(enemy_instance.math_problem )




     