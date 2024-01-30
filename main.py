from enemy import Enemy
from assets import Assets
from map_builder import build_level


class Main:
    def __init__(self):
        self.current_level = build_level()
        self.has_key = False
        self.game_over = False
        self.difficulty_counter = 0

    def intro(self):
        print(Assets.GAME_NAME)
        print(Assets.INTRO_MSG)

    def prompt_user(self):
        print(
            f"What room would you like to move to?\nYou are currently in {self.current_level.name}. You can travel to..."
        )
        for connected_name in self.current_level.connected_names:
            print("\t" + connected_name)
        response = input("Choose wisely: ")
        self.check_response(response)

    def check_response(self, response):

        while response not in self.current_level.connected_rooms:
            print("\nNot quite. Please enter a valid connected room name.")
            print(f"Remember, you can only travel to...")
            for connected_name in self.current_level.connected_names:
                print("\t" + connected_name)
            response = input("Choose wisely: ")
        self.move_user(response)

    def move_user(self, response):
        self.current_level = self.current_level.connected_rooms[response]
        print(f"You have successfully moved to {self.current_level._name}!")
        print(self.current_level.description)
        print()
        if not self.current_level.is_cleared:
            print("g")

    def math_prompt(self, difficulty_counter):
        print(
            f"You have approach a {Enemy.enemy_type}. The {Enemy.enemy_type} has {Enemy.action}"
        )
        # Get math problem
        # placeholders:
        math_prob = "3 + 3"
        ans = 6
        print(
            f"The {Enemy.enemy_type} has a question for you... What is the answer for this problem? \t{math_prob}"
        )
        if not input() == ans:
            self.death()

    def check_has_key(self):
        if self.current_level.has_key:
            print("Congrats you got the key\n")
            self.has_key = True

    def check_game_over(self):
        if self.has_key and self.current_level.is_exit:  # fix this (check boss first)
            response = input(
                "Would you like to restart? Enter Y or N: "
            ).lower()  # add check for invalid response later
            while not response == "y" or "n":
                response = input("Enter either Y or N... I thought you were smart: ")
            if response.lower() == "y":
                self.restart_game()
            else:
                self.game_over = True

    def death(self):
        print(
            "That was wrong. You are NOT as smart as you thought you were. And for that, you will pay the price. You have been smited. Would you like to try again? Enter Y or N: "
        )
        if input() == "y":
            self.restart_game()
        else:
            self.game_over = True

    def credits():
        print(Assets.CREDITS)

    def restart_game(self):
        game = Main()
        game.play_game()

    def play_game(self):
        self.intro()
        while not self.game_over:
            self.prompt_user()
            self.check_has_key()
            self.check_game_over()
            # boss and math problems

    def create_test_enemy(self):
        # Instantiate a test enemy
        test_enemy = Enemy(
            enemy_type="Test Enemy",
            art="ASCII art goes here",
            action="Action message goes here",
            math_problem="Math problem goes here",
        )
        return test_enemy


if __name__ == "__main__":

    game = Main()
    game.play_game()
