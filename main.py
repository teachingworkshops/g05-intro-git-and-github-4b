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
            print(f"You can only travel to...")
            for connected_name in self.current_level.connected_names:
                print("\t" + connected_name)
            response = input("choose wisely: ")
        self.move_user(response)

    def move_user(self, response):
        self.current_level = self.current_level.connected_rooms[response]
        print(f"You have successfully moved to {self.current_level._name}!")
        print(self.current_level.description)
        print()
        if not self.current_level.is_cleared:
            math_prompt(difficulty_counter)

    def check_game_over(self):
        if self.has_key and self.current_level.is_exit:  # fix this (check boss first)
            response = input(
                "Would you like to restart? Enter Y or N: "
            )  # add check for invalid response later
            if response.lower() == "y":
                self.restart_game()
            else:
                self.game_over = True

    def check_has_key(self):
        if self.current_level.has_key:
            print("Congrats you got the key\n")
            self.has_key = True

    def restart_game(self):
        game = Main()
        game.play_game()

    def math_prompt(self, difficulty_counter):
        # call math fuction which returns the key value pair
        response = difficulty_counter

    # def credits():

    def play_game(self):
        self.intro()
        while not self.game_over:
            self.prompt_user()
            self.check_has_key()
            self.check_game_over()
            # boss and math problems


if __name__ == "__main__":

    game = Main()
    game.play_game()
