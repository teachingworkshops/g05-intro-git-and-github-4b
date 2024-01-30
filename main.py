from enemy import Enemy
from assets import Assets
from map_builder import build_level


class Main:
    def __init__(self):
        self.current_level = build_level()
        self.current_level._is_cleared = True
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
        response = input(
            "Choose wisely and enter exactly as you see it: "
        )  # eventually we can ignore cases
        self.check_response(response)

    def check_response(self, response):
        while response not in self.current_level.connected_rooms:
            print("\nNot quite. Please enter a connected room name.")
            print(f"Remember, you can only travel to...")
            for connected_name in self.current_level.connected_names:
                print("\t" + connected_name)
            response = input("Make sure you enter it exactly as you see: ")
        self.move_user(response)

    def move_user(self, response):
        self.current_level = self.current_level.connected_rooms[response]
        if not self.current_level.is_cleared:
            self.math_prompt()
        print(
            f"\nYou have successfully moved to {self.current_level._name}!\n{self.current_level.description}\n"
        )

    def math_prompt(self):  # also pass difficulty_counter
       # ideally the enemy art will have a space before and a space after 
        print(
            f"\n{test_enemy.art}\n\nYou have approach a {test_enemy.enemy_type}. The {test_enemy.enemy_type} has {test_enemy.action}!"
        )
        # Get math problem
        # combine the print statements later or figure out something better
        print(
            f"The {test_enemy.enemy_type} has a question for you...\nWhat is the answer for this problem? \t{test_enemy.math_problem}"
        )

        # placeholder
        ans = 6

        # will all the answers be numbers? will some have variables? how can we handle that.. check diff counter, 0 should have answers all int. need the questions class to work on this.
        if not int(input()) == ans:
            self.death()

        # figure out the scaling for diff counter. how will we know when to increase the counter?
        self.current_level._is_cleared = True

    def check_has_key(self):
        if self.current_level.has_key:
            print("Congrats you got the key\n")
            self.has_key = True

    def check_game_over(self):
        if self.has_key and self.current_level.is_exit:  # fix this (check boss first)
            response = input("Would you like to restart? Enter Y or N: ").lower()
            while not response == "y" or "n":
                response = input(
                    "Enter either Y or N... I thought you were smart: "
                ).lower()
            if response == "y":
                self.restart_game()
            else:
                self.game_over = True

    def death(self):
        # replace print with print(death_message from assets class)
        print(
            "That was wrong. You are NOT as smart as you thought you were. And for that, you will pay the price. You have been smited. Would you like to try again? Enter Y or N: "
        )
        if input().lower() == "y":
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


if __name__ == "__main__":
    test_enemy = Enemy(
        enemy_type="Test Enemy",
        art=":)",
        action="spit in your food",
        math_problem="3 + 3",
    )
    game = Main()
    game.play_game()
