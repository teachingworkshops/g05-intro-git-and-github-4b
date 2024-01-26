from Room import Room

class Main:

    def main():
        dead_end = Room("Dead end sucker", {})
        x = Room("This is a cool room", {"North": dead_end})
        x.get_directions()
        y = x.get_room("North")
        print(y.get_description())

    if __name__ == '__main__':
        main()