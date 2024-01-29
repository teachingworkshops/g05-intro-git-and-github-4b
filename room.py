class Room:
    _connected_rooms = {}  # Assume (String name: Room room) pair
    _name = ""
    _description = ""
    _has_key = False
    _is_exit = False
    _is_cleared = False

    def __init__(self, name, description):
        """
        Initializes a new room object

        Args:
            name (String): Name of the current room
            description (String): Some words telling the player about the current room
        """
        self._description = description
        self._name = name
        self._connected_rooms = {}
        self._has_key = False
        self._is_exit = False

    @property
    def connected_rooms(self):
        """
        Returns the dictionary of rooms connected to the current room

        Returns:
            dict: connected rooms dictionary
        """
        return self._connected_rooms

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
    def description(self):
        """
        Returns the description of the current room

        Returns:
            String: _description
        """
        return self._description

    @property
    def connected_names(self):
        """
        Returns the names of all rooms connected to the current room

        Returns:
            list: All connected room names
        """
        return list(self._connected_rooms.keys())

    def set_has_key(self, new_value):
        """
        Sets the boolean value for whether a room will have a key
        """
        self._has_key = new_value

    @property
    def has_key(self):
        """
        Returns whether the current room has a key or not

        Returns:
            Boolean: _has_key
        """
        return self._has_key
    
    def set_exit(self, new_value):
        """
        Sets the boolean value for whether the room is an exit
        """
        self._is_exit = new_value
    
    @property
    def is_exit(self):
        """
        Returns whether the room is an exit

        Return:
            Boolean: _is_exit
        """
        return self._is_exit
    
    def set_cleared(self, new_value):
        """
        Sets the _is_cleared flag
        """
        self._is_cleared = new_value

    @property
    def is_cleared(self):
        """
        Gets whether a room is cleared of enemies

        Returns:
            Boolean: _is_cleared
        """
        return self._is_cleared
    
    def set_name(self, new_value):
        """
        Sets the name of the current room
        """
        self._name = new_value

    @property
    def name(self):
        """
        Gets the name of the current room

        Returns:
            String: Name of current room
        """
        return self._name
