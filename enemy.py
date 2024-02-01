class Enemy:
    """
    Represents an Enemy.
    """    
    def __init__(self, enemy_type, art, action, math_question):
        """
        Initializes a new instance of the Enemy class.

        Args:
            enemy_type (String): Enemy type.
            art (String): ASCII art corresponding with the enemy.
            action (String): Action message the enemy will be doing.
            math_question (Tuple): Holds question and answer
        """
        self._art = art
        self._action = action
        self._math_question = math_question
        self._enemy_type = enemy_type

    @property
    def enemy_type(self):
        """
        returns the enemy's type.

        Returns:
            String: enemy type
        """        
        return self._enemy_type

    @property
    def art(self):
        """
        returns the enemy's ASCII art.

        Returns:
            String: ASCII art.
        """        
        return self._art

    @property
    def action(self):
        """
         returns the enemy's action.

        Returns:
            String: the enemy's action message.
        """        
        return self._action 
    
    def get_question(self):
        """
         returns the enemy's math problem.

        Returns:
            String: enemy's math problem.
        """        
        return self._math_question[0]
    
    def get_answer(self):
        """
         returns the enemy's math problem.

        Returns:
            String: enemy's math problem.
        """        
        return self._math_question[1]       