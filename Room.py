class Room:
    _connected_rooms = {}  # Assume (String direction: Room room) pair
    _description = ""
    _has_key = False
    _is_exit = False

    def __init__(self, description):
        """
        Initializes a new room object

        Args:
            description (String): Some words telling the player about the current room
        """
        self._description = description
        self._connected_rooms = {}
        self._has_key = False
        self._is_exit = False

    def add_room(self, name):
        """
        Adds a room to the current room

        Args:
            name (String): Name of the new room
        """
        self._connected_rooms[name] = Room("")

    @property
    def get_room(self, name):
        """
        Returns the room tied to given name

        Args:
            name (String): Name of the room

        Returns:
            Room: Room object
        """
        return self._connected_rooms[name]

    @property
    def get_description(self):
        """
        Returns the description of the current room

        Returns:
            String: Room description
        """
        return self._description

    def get_directions(self):
        """
        Prints the all room names connected to the current room
        """
        for key in self._connected_rooms:
            print(key)

    def set_has_key(self, new_value):
        """
        Sets the boolean value for whether a room will have a key
        """
        self._has_key = new_value

    @property
    def get_has_key(self):
        """
        Returns whether the current room has a key or not

        Returns:
            Boolean: Key
        """
        return self._has_key
    
    def set_exit(self, new_value):
        """
        Sets the boolean value for whether the room is an exit
        """
        self._is_exit = new_value
    
    @property
    def get_exit(self):
        """
        Returns whether the room is an exit

        Return:
            Boolean: Exit
        """
        return self._is_exit