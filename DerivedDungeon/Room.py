class Room:
    description = ""
    connected_rooms = {}  # Assume (String direction: Room room) pair
    _has_key = False
    _is_exit = False

    def __init__(self, description, connected_rooms):
        self.description = description
        self.connected_rooms = connected_rooms

    def get_description(self):
        return self.description

    def get_directions(self):
        for key in self.connected_rooms:
            print(key)
            
    def get_room(self, direction):
        return self.connected_rooms[direction]

    def set_has_key(self, new_value):
        self._has_key = new_value

    def get_has_key(self):
        return self._has_key