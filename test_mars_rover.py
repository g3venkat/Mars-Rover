
import sys
import unittest
from helper_functions import RoverHelperClass  
from mars_rover import MarsRoverClass

class TestMarsRover(unittest.TestCase):

    def test_validate_boundaries(self):
        self.assertEqual(RoverHelperClass.validate_boundaries(6, 6, 5, 5), (5, 5))
        self.assertEqual(RoverHelperClass.validate_boundaries(-1, -1, 0, 0), (0, 0))

    def test_validate_instructions(self):
        self.assertTrue(RoverHelperClass.validate_instructions("LMLMLM"))
        self.assertFalse(RoverHelperClass.validate_instructions("XCV"))

    def test_find_rover_end_coordinates(self):
        test_imput_1 = """5 5
        1 2 N
        LMLMLMLM
        3 3 E
        MMRMMRMRRM"""
        expected_output = """1 3 N
        5 1 E"""

        self.assertEqual(MarsRoverClass.find_rover_end_coordinates(test_imput_1), expected_output)

        # 2. Test case - Positive Test case
        test_input_2 = """3 3
        0 0 S
        LMMLM
        1 2 W
        LMLMRM"""
        expected_output = """2 1 N
        2 0 E"""
        self.assertEqual(MarsRoverClass.find_rover_end_coordinates(test_input_2), expected_output)


        # 3. Test case for coordinate set to max_x/max_y when they exceed beyond the boundary
        test_input_3 = """5 5
        4 4 N
        MMMM
        """
        expected_output = """4 5 N"""
        self.assertEqual(MarsRoverClass.find_rover_end_coordinates(test_input_3), expected_output)

        # 4. Invalid Instructions
        test_input_4 = """5 5
        1 1 N
        XCV
        """
        expected_output = """Invalid instruction"""
        self.assertEqual(MarsRoverClass.find_rover_end_coordinates(test_input_4), expected_output)

        # 5. Test case for coordinates below 0. Per our assumption, it sets the boundary to 0,0
        test_input_5 = """-5 -5 
        -1 -2 N
        LMLM
        """
        expected_output = """Upper Right coordinates must be positive"""
        self.assertEqual(MarsRoverClass.find_rover_end_coordinates(test_input_5), expected_output)


    if __name__ == "__main__":
        unittest.main()