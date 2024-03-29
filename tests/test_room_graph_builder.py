# -*- coding: utf-8 -*-
"""
@author: Brian Morillo
RoomGraphBuilder class test
"""
import pytest
from room_graph_builder import RoomGraphBuilder
from room import Room

# Fixture for sample rooms
@pytest.fixture
def sample_rooms():
    room_names = ["Room Name 1", "Room Name 2", "Room Name 3"]
    room_desc = "Room Desc"
    return [Room(name, room_desc) for name in room_names]

# Test case for room graph builder attach rooms method
def test_room_graph_builder_attach_rooms(sample_rooms):
    room1, room2 = sample_rooms[:2]

    RoomGraphBuilder.attach_rooms(room1, room2)   

    # Checks if room2 is correctly attached to room1
    assert room1.name not in room1.connected_names
    assert room2.name in room1.connected_names

    room_1_list = list(room1.connected_rooms.values())
    assert room1 not in room_1_list
    assert room2 in room_1_list

    # Checks if room1 is correctly attached to room2
    assert room1.name in room2.connected_names
    assert room2.name not in room2.connected_names

    room_2_list = list(room2.connected_rooms.values())
    assert room1 in room_2_list
    assert room2 not in room_2_list    


# Test case for checking a room path graph through the RoomGraphBuilder
def test_room_graph_builder_path_creation(sample_rooms):
    room1, room2, room3 = sample_rooms[:3]

    RoomGraphBuilder.path([room1, room2, room3])

    # Checks if room1 is correctly attached to room2
    assert room1.name not in room1.connected_names
    assert room2.name in room1.connected_names
    assert room3.name not in room1.connected_names

    room_1_list = list(room1.connected_rooms.values())
    assert room1 not in room_1_list
    assert room2 in room_1_list
    assert room3 not in room_1_list

    # Checks if room2 is correctly attached to room1 and room3
    assert room1.name in room2.connected_names
    assert room2.name not in room2.connected_names
    assert room3.name in room2.connected_names

    room_2_list = list(room2.connected_rooms.values())
    assert room1 in room_2_list
    assert room2 not in room_2_list
    assert room3 in room_2_list    

    # Checks if room3 is correctly attached to room2
    assert room1.name not in room3.connected_names
    assert room2.name in room3.connected_names
    assert room3.name not in room3.connected_names

    room_3_list = list(room3.connected_rooms.values())
    assert room1 not in room_3_list
    assert room2 in room_3_list
    assert room3 not in room_3_list       

# Test case for checking a room cycle graph through the RoomGraphBuilder
def test_room_graph_builder_cycle_creation(sample_rooms):
    room1, room2, room3 = sample_rooms[:3]

    RoomGraphBuilder.cycle([room1, room2, room3])

    # Checks if rooms where correctly attached to room1
    assert room1.name not in room1.connected_names
    assert room2.name in room1.connected_names
    assert room3.name in room1.connected_names

    room_1_list = list(room1.connected_rooms.values())
    assert room2 in room_1_list
    assert room3 in room_1_list

    # Checks if rooms where correctly attached to room2
    assert room1.name in room2.connected_names
    assert room2.name not in room2.connected_names    
    assert room3.name in room2.connected_names

    room_2_list = list(room2.connected_rooms.values())
    assert room1 in room_2_list
    assert room3 in room_2_list    

    # Checks if rooms where correctly attached to room3
    assert room1.name in room3.connected_names
    assert room2.name in room3.connected_names    
    assert room3.name not in room3.connected_names

    room_3_list = list(room3.connected_rooms.values())
    assert room1 in room_3_list
    assert room2 in room_3_list      

# Test case for checking a room star graph through the RoomGraphBuilder
def test_room_graph_builder_star_creation(sample_rooms):
    room1, room2, room3 = sample_rooms[:3]

    RoomGraphBuilder.star(room2, [room1, room3])

    # Checks if room1 is correctly attached to room2
    assert room1.name not in room1.connected_names
    assert room2.name in room1.connected_names
    assert room3.name not in room1.connected_names

    room_1_list = list(room1.connected_rooms.values())
    assert room1 not in room_1_list
    assert room2 in room_1_list
    assert room3 not in room_1_list

    # Checks if room2 is correctly attached to room1 and room3
    assert room1.name in room2.connected_names
    assert room2.name not in room2.connected_names
    assert room3.name in room2.connected_names

    room_2_list = list(room2.connected_rooms.values())
    assert room1 in room_2_list
    assert room2 not in room_2_list
    assert room3 in room_2_list    

    # Checks if room3 is correctly attached to room2
    assert room1.name not in room3.connected_names
    assert room2.name in room3.connected_names
    assert room3.name not in room3.connected_names

    room_3_list = list(room3.connected_rooms.values())
    assert room1 not in room_3_list
    assert room2 in room_3_list
    assert room3 not in room_3_list       