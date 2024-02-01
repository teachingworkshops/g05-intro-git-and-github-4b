from enemy_builder import EnemyBuilder
from assets import Assets
from map_builder import build_level


class derivative_dungeon:
    def __init__(self):
        """
        Initializes a new instance of the Derivative Dungeon class

        Attributes:
            current_level (Room): The current level the player is in.
            has_key (bool): Indicates whether the player has obtained the key.
            game_over (bool): Indicates whether the game is over.
            difficulty_counter (int): The counter indicating the game difficulty.
            enemy_builder (EnemyBuilder): The builder used to create enemies.
        """
        self.current_level = build_level()
        self.current_level._is_cleared = True
        self.has_key = False
        self.game_over = False
        self.difficulty_counter = 1
        self.enemy_builder = EnemyBuilder()

    def intro(self):
        """
        Displays the game name and introduction messages.

        """
        print(Assets.GAME_NAME)
        print(Assets.INTRO_MSG)

    def prompt_user(self):
        """
        Prompts user where they would like to move to.

        """
        print(
            f"What room would you like to move to?\nYou are currently in {self.current_level.name}. You can travel to..."
        )
        for connected_name in self.current_level.connected_names:
            print("\t" + connected_name)
        response = input(
            "Choose wisely and enter exactly as you see it: "
        )  # eventually we can ignore cases
        print(Assets.DELIMIT)
        self.check_response(response)

    def check_response(self, response):
        """
        checks whether room user wants to travel to is a valid room

        Args:
            response (String): room user wants to travel to.
        """
        while response not in self.current_level.connected_rooms:
            print("\nNot quite. Please enter a connected room name.")
            print(f"Remember, you can only travel to...")
            for connected_name in self.current_level.connected_names:
                print("\t" + connected_name)
            response = input("Make sure you enter it exactly as you see: ")

        self.move_user(response)

    def move_user(self, response):
        """
        Moves user to the room they want. if room is not cleared already,
        prompt a math question

        Args:
            response (String): room user wants to travel to.
        """
        self.current_level = self.current_level.connected_rooms[response]
        if not self.current_level.is_cleared:
            self.math_enemy()
        print(
            f"\nYou have successfully moved to {self.current_level._name}!\n{self.current_level.description}\n"
        )

    def math_enemy(self):
        """
        spawns an math enemy and checks if the answer is correct. If not, game over buddy.

        """
        if self.current_level.is_exit:
            enemy = self.enemy_builder.build_boss()
            self.difficulty_counter = 10
        else:
            enemy = self.enemy_builder.build_random_enemy(self.difficulty_counter)

        question, answer = enemy._math_question
        print(
            f"{enemy.art}\nYou have approached a {enemy.enemy_type}. The {enemy.enemy_type} is {enemy.action}! "
            + f"The {enemy.enemy_type} has a question for you...\nWhat is the answer for this problem? \t{question}"
        )

        if not input().strip() == answer:
            self.death()
        self.difficulty_counter += 1
        print(Assets.DELIMIT)
        print("Nice job. Transporting now...")
        self.current_level._is_cleared = True

        if not self.has_key and self.current_level.is_exit:
            print("Nice try buddy, you forgot the key...")

    def check_has_key(self):
        """
        Gives user key if enters key room.

        """
        if self.current_level.has_key:
            print("Congrats you got the key\n")
            self.has_key = True

    def check_game_over(self):
        """
        Asks user if they want to stop playing after reaching exit with key.

        """
        if self.has_key and self.current_level.is_exit:
            print(Assets.win_message())
            self.game_over = True
            exit()

    def death(self):
        """
        Displays death message when user fails.

        """
        print(Assets.death_message())
        if input().lower() == "y":
            self.restart_game()
        else:
            self.game_over = True
            exit()

    def credits():
        """
        Displays end credits

        """
        print(Assets.CREDITS)

    def restart_game(self):
        """
        Restarts game state

        """
        game = derivative_dungeon()
        game.play_game()

    def play_game(self):
        """
        Game Controller

        """
        self.intro()
        while not self.game_over:
            self.prompt_user()
            self.check_has_key()
            self.check_game_over()


if __name__ == "__main__":
    game = derivative_dungeon()
    game.play_game()
