# Mars-Rover

Requirement/Notes:
Surface to be explored - rectangular
Rover’s position (x,y, orientation) where x,y is the coordinates and orientation (N, S, E or W)

Input from NASA: 
         Simple string of letters 
Possible input 
L - Spin 90° to the left, in the same coordinate location
R - Spin 90° to the right, in the same coordinate location
M - Move forward, maintain the same heading

Input:
First line of input - upper right coordinate of the plateau
The surface area defined between lower left coordinates (0,0) and upper right coordinates is given as the first input

Subsequent inputs: Information about the rovers that have been deployed
Line 1 - Rover's position coordinate, y coordinate, orientation
Line 2 - Series of instructions to the rover

Output:
Final coordinate and heading for each rover

Assumptions:
    The order of input between line 1 and line 2 cannot be swapped.
    The first input should be the top right coordinates
    Coordinate positions
    The square directly N from (x,y) is (x, y+1)
    The square directly S from (x,y) is (x, y-1)
    The square directly E from (x,y) is (x-1, y)
    The square directly W from (x,y) is (x+1, y)
    Negative co-ordinates are allowed
    When a coordinate falls out of the boundary, it would be set to the (max_x,max_y) or (0,0)

Example:
Test Input 1:
5 5
1 2 N
LMLMLMLMM


*Move*  *Position*
Start 1 2 N
L     1 2 E
M     0 2 E
L     0 2 S
M     0 1 S
L     0 1 W
M     1 1 W
L     1 1 N
M     1 2 N
M     1 3 N





