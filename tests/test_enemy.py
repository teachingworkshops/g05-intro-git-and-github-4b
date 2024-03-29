# -*- coding: utf-8 -*-
"""
@author: Brian Morillo
Enemy class test
"""
import pytest
from enemy import Enemy

# Fixture for creating an instance of the Enemy class
@pytest.fixture
def enemy_instance():
    enemy_type = "Enemy Type"
    art = "ASCII Art"
    action = "Action Message"
    math_problem = "5 + 5", "10"
    return Enemy(enemy_type, art, action, math_problem)

# Test case for checking the initialization of the Enemy class
def test_enemy_initialization(enemy_instance):
    assert enemy_instance.enemy_type == "Enemy Type"
    assert enemy_instance.art == "ASCII Art"
    assert enemy_instance.action == "Action Message"
    assert enemy_instance.get_question() == "5 + 5"
    assert enemy_instance.get_answer() == "10"

# Test case for the type property
def test_enemy_type_property(enemy_instance):
    assert enemy_instance.enemy_type == "Enemy Type"

# Test case for the art property
def test_enemy_art_property(enemy_instance):
    assert enemy_instance.art == "ASCII Art"

# Test case for the action property
def test_enemy_action_property(enemy_instance):
    assert enemy_instance.action == "Action Message"

# Test case for the math_problem question
def test_enemy_math_question(enemy_instance):
    assert enemy_instance.get_question() == "5 + 5"

# Test case for the math_problem answer
def test_enemy_math_answer(enemy_instance):
    assert enemy_instance.get_answer() == "10"   