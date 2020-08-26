'''
On an infinite plane, a robot initially stands at (0, 0) and faces north.  The robot can receive one of three instructions:

"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degress to the right.
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.
'''

def move_robot(instructions, x=0, y=0, direction='N'):
    direction_left,  invert_left  = {'N':0, 'L':1, 'S':2, 'R':3}, {0:'N', 1:'L', 2:'S', 3:'R'}
    direction_right, invert_right = {'N':0, 'R':1, 'S':2, 'L':3}, {0:'N', 1:'R', 2:'S', 3:'L'}
    
    for instruction in instructions:
        if instruction == 'G':
            if direction == 'N':
                x, y = x, y+1

            elif direction == 'S':
                x, y = x, y-1

            elif direction == 'L':
                x, y = x-1, y

            elif direction == 'R':
                x, y = x+1, y
                
        elif instruction == 'L':
            direction = invert_left[(direction_left[direction] + 1)%4]
            
        
        elif instruction == 'R':
            direction = invert_right[(direction_right[direction] + 1)%4]
    return x, y, direction

def is_robot_bounded(instructions: str) -> bool:
    x, y, direction = move_robot(instructions)

    if (x, y) == (0, 0):
        return True
    else:
        x, y, direction = move_robot(instructions*4, 0, 0, 'N')
        if (x, y) == (0, 0):
            return True 
    return False
    
    
instructions = 'GGLLGG'
is_robot_bounded(instructions)
