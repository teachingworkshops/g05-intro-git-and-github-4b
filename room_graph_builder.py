class RoomGraphBuilder:
    """
    Builder used to build graphs based on rooms
    """

    @staticmethod
    def attach_rooms(room1, room2):
        """
        Attaches two rooms to each other
        Checks if rooms not attached to that rooms yet

        Args:
            room1 (Room): First room
            room2 (Room): Second room
        """            
        if room2.name not in room1.connected_rooms:
            room1.connected_rooms[room2.name] = room2

        if room1.name not in room2.connected_rooms:            
            room2.connected_rooms[room1.name] = room1

    @staticmethod
    def cycle(room_list):
        """
        creates a cycle graph out of the rooms list

        Args:
            room_list (list): list of rooms

        """
        RoomGraphBuilder.path(room_list)
        RoomGraphBuilder.attach_rooms(room_list[0], room_list[-1])

    @staticmethod
    def path(rooms_list):
        """
        creates a path graph out of rooms list in order

        Args:
            rooms_list (list): list of rooms

        """
        list_len = len(rooms_list)  
        for idx in range(list_len-1):
            RoomGraphBuilder.attach_rooms(rooms_list[idx], rooms_list[idx+1])

    @staticmethod
    def star(central_room, room_list):
        """
        creates a star graph using the central room 
        and a list of rooms to attach it to

        Args:
            central_room (Room): room that all other rooms will be attached to
            room_list (list): list of rooms to attach to central room
        """
        for current_room in room_list:
            RoomGraphBuilder.attach_rooms(central_room, current_room)    