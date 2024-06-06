import sys

class RoverHelperClass:
        
        # Dictionary Key-value pair to store next left direction
        @staticmethod
        def turn_left(direction) -> str:
            next_left_direction = {'N': 'W',
                                'W': 'S',
                                'S': 'E',
                                'E': 'N'}[direction]
            
            return next_left_direction
        
        # Dictionary key-value store to store next right direction
        @staticmethod
        def turn_right(direction) -> str:
            next_right_direction = {'N': 'E',
                                    'E': 'S',
                                    'S': 'W',
                                    'W': 'N'}[direction]
            
            return next_right_direction
        
        # Move 1 coordinate in the direction specified
        @staticmethod
        def move_forward(x, y, direction):
            if direction == 'N':
                y = y+1
            elif direction == 'S':
                y = y-1
            elif direction == 'E':
                x = x+1
            elif direction == 'W':
                x = x-1

            return x, y

        # Split the coordinates to x,y and direction
        @staticmethod
        def split_coordinates(rover_coordinates):
            position = rover_coordinates.split()
            
            if len(position) != 3:
                raise ValueError (f"Invalid rover coordinate entry, {position}")
                
            x, y = int(position[0]), int(position[1])
            direction = position[2]

            if direction not in {'N', 'E', 'S', 'W'}:
                raise ValueError("Invalid Direction")

            return x,y, direction

        
        # Validate if the rover co-ordinates fall within the boundary of the surface
        @staticmethod
        def validate_boundaries (x, y, max_x, max_y):
            if (max_x > 0 and max_y > 0):
                x = max(0, min(x, max_x))
                y = max(0, min(y, max_y))

            return x, y
        
        # Validate that the instruction has at least 1 actionable command. 
        # If not, return invalid instruction
        @staticmethod
        def validate_instructions(rover_instructions):
            actionable_commands = ['L', 'R', 'M']
            for char in rover_instructions:
                if char in actionable_commands:
                    return True
            
            return False 
        
        
       
        
    
    


        