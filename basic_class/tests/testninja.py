from basic_class import ninja

import unittest

class TestNinja(unittest.TestCase):
    def setUp(self):
        player1 = ninja.Ninja("Player1")
        player2 = ninja.Ninja("Player2")
        
    def test_ninja_kick(self):
        
