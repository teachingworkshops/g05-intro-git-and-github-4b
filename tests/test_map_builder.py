# -*- coding: utf-8 -*-
"""
@author: Brian Morillo
MapBuilder class test
"""
import pytest
from map_builder import MapBuilder
from Room import Room

# Fixture for creating an instance of the MapBuilder class
@pytest.fixture
def map_builder_instance():
    return MapBuilder()

# Test case for map builder attach rooms method
def test_map_builder_attach_rooms(map_builder_instance):
    room_name_1 = "Room Name 1"
    room_name_2 = "Room Name 2"
    room_desc = "Room Desc"

    room1 = Room(room_name_1, room_desc)
    room2 = Room(room_name_2, room_desc) 

    map_builder_instance.attach_rooms(room1, room2)   

    # Checks if room2 is correctly attached to room1
    assert room_name_1 not in room1.connected_names
    assert room_name_2 in room1.connected_names

    room_1_list = list(room1.connected_rooms.values())
    assert room1 not in room_1_list
    assert room2 in room_1_list

    # Checks if room1 is correctly attached to room2
    assert room_name_1 in room2.connected_names
    assert room_name_2 not in room2.connected_names

    room_2_list = list(room2.connected_rooms.values())
    assert room1 in room_2_list
    assert room2 not in room_2_list    


# Test case for checking a room path graph through the map builder
def test_map_builder_path_creation(map_builder_instance):
    room_name_1 = "Room Name 1"
    room_name_2 = "Room Name 2"
    room_name_3 = "Room Name 3"
    room_desc = "Room Desc"

    room1 = Room(room_name_1, room_desc)
    room2 = Room(room_name_2, room_desc)
    room3 = Room(room_name_3, room_desc)

    map_builder_instance.path([room1, room2, room3])

    # Checks if room1 is correctly attached to room2
    assert room_name_1 not in room1.connected_names
    assert room_name_2 in room1.connected_names
    assert room_name_3 not in room1.connected_names

    room_1_list = list(room1.connected_rooms.values())
    assert room1 not in room_1_list
    assert room2 in room_1_list
    assert room3 not in room_1_list

    # Checks if room2 is correctly attached to room1 and room3
    assert room_name_1 in room2.connected_names
    assert room_name_2 not in room2.connected_names
    assert room_name_3 in room2.connected_names

    room_2_list = list(room2.connected_rooms.values())
    assert room1 in room_2_list
    assert room2 not in room_2_list
    assert room3 in room_2_list    

    # Checks if room3 is correctly attached to room2
    assert room_name_1 not in room3.connected_names
    assert room_name_2 in room3.connected_names
    assert room_name_3 not in room3.connected_names

    room_3_list = list(room3.connected_rooms.values())
    assert room1 not in room_3_list
    assert room2 in room_3_list
    assert room3 not in room_3_list       

# Test case for checking a room cycle graph through the the map builder
def test_map_builder_cycle_creation(map_builder_instance):
    room_name_1 = "Room Name 1"
    room_name_2 = "Room Name 2"
    room_name_3 = "Room Name 3"
    room_desc = "Room Desc"

    room1 = Room(room_name_1, room_desc)
    room2 = Room(room_name_2, room_desc)
    room3 = Room(room_name_3, room_desc)

    map_builder_instance.cycle([room1, room2, room3])

    # Checks if rooms where correctly attached to room1
    assert room_name_1 not in room1.connected_names
    assert room_name_2 in room1.connected_names
    assert room_name_3 in room1.connected_names

    room_1_list = list(room1.connected_rooms.values())
    assert room2 in room_1_list
    assert room3 in room_1_list

    # Checks if rooms where correctly attached to room2
    assert room_name_1 in room2.connected_names
    assert room_name_2 not in room2.connected_names    
    assert room_name_3 in room2.connected_names

    room_2_list = list(room2.connected_rooms.values())
    assert room1 in room_2_list
    assert room3 in room_2_list    

    # Checks if rooms where correctly attached to room3
    assert room_name_1 in room3.connected_names
    assert room_name_2 in room3.connected_names    
    assert room_name_3 not in room3.connected_names

    room_3_list = list(room3.connected_rooms.values())
    assert room1 in room_3_list
    assert room2 in room_3_list      

# Test case for checking a room star graph through the the map builder
def test_map_builder_star_creation(map_builder_instance):
    room_name_1 = "Room Name 1"
    room_name_2 = "Room Name 2"
    room_name_3 = "Room Name 3"
    room_desc = "Room Desc"

    room1 = Room(room_name_1, room_desc)
    room2 = Room(room_name_2, room_desc)
    room3 = Room(room_name_3, room_desc)

    map_builder_instance.star(room2, [room1, room3])

    # Checks if room1 is correctly attached to room2
    assert room_name_1 not in room1.connected_names
    assert room_name_2 in room1.connected_names
    assert room_name_3 not in room1.connected_names

    room_1_list = list(room1.connected_rooms.values())
    assert room1 not in room_1_list
    assert room2 in room_1_list
    assert room3 not in room_1_list

    # Checks if room2 is correctly attached to room1 and room3
    assert room_name_1 in room2.connected_names
    assert room_name_2 not in room2.connected_names
    assert room_name_3 in room2.connected_names

    room_2_list = list(room2.connected_rooms.values())
    assert room1 in room_2_list
    assert room2 not in room_2_list
    assert room3 in room_2_list    

    # Checks if room3 is correctly attached to room2
    assert room_name_1 not in room3.connected_names
    assert room_name_2 in room3.connected_names
    assert room_name_3 not in room3.connected_names

    room_3_list = list(room3.connected_rooms.values())
    assert room1 not in room_3_list
    assert room2 in room_3_list
    assert room3 not in room_3_list       