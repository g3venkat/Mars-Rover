import sys

from helper_functions import RoverHelperClass

class MarsRoverClass:
    @staticmethod
    def find_rover_end_coordinates(input_data):
         # parse input into a list
        
        input_lines = input_data.strip().split('\n')
        
        # Input validations
        if len(input_lines) < 1:
            raise ValueError("No valid input provided")
        
        upper_right_coord = input_lines[0].split()

        if len(upper_right_coord) != 2:
            raise ValueError ("Invalid upper right co-ordinates")

        max_x, max_y = int(upper_right_coord[0]), int(upper_right_coord[1])
        
        # upper_right_coordinates should not be the same as lower left coordinates (0,0)
        if ((max_x <= 0 ) and (max_y <= 0)):
            raise ValueError("Upper Right coordinates must be positive. Invalid coordinates.", max_x, max_y ) 
        
        i = 1
        results = []
        while i < len(input_lines):
            rover_coordinates = input_lines[i]
            rover_instructions = input_lines[i+1]

            try:
                # Split the rover co-ordinates as x, y and direction
                x, y, direction = RoverHelperClass.split_coordinates (rover_coordinates)

                # Validate if the rover coordinates are in the boundary of (0,0) and (max_x max_y), 
                x, y = RoverHelperClass.validate_boundaries (x, y, max_x, max_y) 

                # Check if there is at least one valid actionable instruction to proceed
                is_valid_instruction = RoverHelperClass.validate_instructions (rover_instructions)
                if is_valid_instruction ==  False:
                    print (rover_instructions)
                    raise ValueError("Invalid instruction", rover_instructions)
                    i = i+2
                    continue   

                for command in rover_instructions:
                    if command == 'L':
                        direction = RoverHelperClass.turn_left(direction)
                    elif command == 'R':
                        direction = RoverHelperClass.turn_right(direction)
                    elif command == 'M':
                        x, y = RoverHelperClass.move_forward (x, y, direction)

                        # Validate if the move coordinates are in boundary of 0,0 and max_x/max_y.
                        x, y = RoverHelperClass.validate_boundaries(x, y, max_x, max_y)
                    
                    else: # donot do anything if the instruction is not L,R,M
                        continue
                        

                results.append(f"{x} {y} {direction}")
            except ValueError as e:
                print(e)
            finally:
                i = i+2
    
        return "\n".join(results)
    
        
 
# 1. Test case - Positive Test case
test_input_1 = """5 5
1 2 N
LMLMLMLMM
3 3 E
MMRMMRMRRM"""

# 2. Test case - Positive Test case
test_input_2 = """3 3
0 0 S
LMMLM
1 2 W
LMLMRM"""

# 3. Test case for coordinate set to max_x/max_y when they exceed beyond the boundary
test_input_3 = """5 5
4 4 N
MMMM
"""

# 4. Invalid Instructions
test_input_4 = """5 5
1 1 N
XCV
"""

# 5. Test case for coordinates below 0. Per our assumption, it sets the boundary to 0,0
test_input_5 = """-5 -5 
-1 -2 N
LMLM
"""

# 6. Test case - Incorrect order
test_input_6 = """5 5
LMLMLMLMM
1 2 N
MMRMMRMRRM
3 3 E"""


def main():
    print("TestCase1: ")
    print( MarsRoverClass.find_rover_end_coordinates(test_input_1))  # Expected Output: 1 3 N \n 5 1 E
    
    print("TestCase2: ")
    print( MarsRoverClass.find_rover_end_coordinates(test_input_2))  # Expected Output: 2 1 N \n 

    print("TestCase3: ")
    print( MarsRoverClass.find_rover_end_coordinates(test_input_3))  

    print("TestCase4: ")
    try:
        print( MarsRoverClass.find_rover_end_coordinates(test_input_4)) 
    except ValueError as e:
        print (e)
    
    print("TestCase5: ")
    try:
        print( MarsRoverClass.find_rover_end_coordinates(test_input_5)) 
    except ValueError as e:
        print (e)

    print("TestCase6: ")
    print( MarsRoverClass.find_rover_end_coordinates(test_input_6))

if __name__ == "__main__":
    main()

    
