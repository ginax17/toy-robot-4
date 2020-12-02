from world.text import world
import world
import unittest
import robot
import sys
from world.text import world as world
from unittest.mock import patch
from io import StringIO

class TestWorldFunction(unittest.TestCase):
    @patch("sys.stdin", StringIO("hal\nforward 10\nforwar 10"))
    def test_showing_positions(self):
        #robot.robot_start()
        # actual_outcome = world.text.world.show_position('hal')
        # expected_outcome = ('> HAL moved forward by 10 steps.')
        self.assertFalse(world.is_position_allowed(210,0),False)

    def test_showing_positions_min(self):
        #robot.robot_start()
        # actual_outcome = world.text.world.show_position('hal')
        # expected_outcome = ('> HAL moved forward by 10 steps.')
        self.assertTrue(world.is_position_allowed(10,0),True)

    
