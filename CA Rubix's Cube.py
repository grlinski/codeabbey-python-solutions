
# Rubix's Cube
# https://www.codeabbey.com/index/task_view/rubiks-cube



"""
Maybe this may be a bit too much but the best way for me is to map the entire cube

# There are 3 basic types of cube.
# Corners which have 3 sides.
# Middle Sides which have 2 sides
# Middle which has a single side.


Parts
8 corners
6 middles
12 Middle Sides

6 Colours
RWBOGY
Red White Blue Orange Green Yellow

However Likely Better to Determine Where these parts are by their relative location to the front.

Sides
Up, Down
Front, Back
Left, Right

# Priority
Front, Back, Up, Down, Left, Right

Create an Array
Seperate Cubes based on type.
Given them all colour designations, type and inital position designations.

Naming
# Orientation Priority
Front, Back, Up, Down, Right, Left
# Colour Priority
Yellow, White, Orange, Red, Blue, Green
If I am correct, check real cube, with Yellow Forward and orange ontop
Front = Yellow
Back = White
Up = Orange
Down = Red
Right = Blue
Left = Green

Numbering
Start at FUL, Front Up Left = 0
Go Counter Clock Wise to UL, Up Left = 8
And Up = 9
Then start at FL = 10 and go around
Down is the last and is 25
26 cubes total.





"""

"""
Creates the Initial Cube
Returns a list of many lists

Cube
Corners, Sides, Middle
Each of These consists of two Lists for the cubes inside.
Current Position, Inital
Current
number, type, position
Initial
number, type, position, colour

"""
def cubeInitial():
    # Each cube should be define first by its current position
    # Which is to be both its numerical position and orientation position.
    # Then the second portion is its original state
    # This is its original position, its numerical position and its colour.
    """
    Cube Specs
    Top Level, position 0 = Corners, 1 = Sides, 2 = Middles
    Then each cube is defined by 2 lists
    Current Position and initial
    cur = 0, inital = 1
    Current
    current Numerical Position, Type, Orientation
    Initial, Note Never Changes, used for reference
    Inital Position, Type, Orientation, Colour



    """
    """
    All Cubes Inital Positions
    Top Row
    0 COR FUL YOG
    1 SID FU YO
    2 COR FUR YOB
    3 SID UR OB
    4 COR BUR WOB
    5 SID BU WO 
    6 COR BUL WOG
    7 SID UL OG
    8 MID U O
    
    Middle Row
    9 SID FL YO
    10 MID F Y
    11 SID FR YB
    12 MID R B
    13 SID BR WB
    14 MID B W
    15 SID BL WG
    16 MID L G
    
    Bottom Row
    17 COR FDL YRG
    18 SID FD YR
    19 COR FDR YRB
    20 SID DR RB
    21 COR BDR WRB
    22 SID BD WR
    23 COR BDL WRG
    24 SID DL RG
    25 MID D R

    
    
    
    
    
    
    
  
    """
    corners = [[[0,'COR','FUL'],[0,'COR','FUL','YOG']],
    [[2, 'COR', 'FUR'], [2, 'COR', 'FUR', 'YOB']],
    [[4, 'COR', 'BUR'], [4, 'COR', 'BUR', 'WOB']],
    [[6, 'COR', 'BUL'], [6, 'COR', 'BUL', 'WOG']],
    [[17, 'COR', 'FDL'], [17, 'COR', 'FDL', 'YRG']],
    [[19, 'COR', 'FDR'], [19, 'COR', 'FDR', 'YRB']],
    [[21, 'COR', 'BDR'], [21, 'COR', 'BDR', 'WRB']],
    [[23, 'COR', 'BDL'], [23, 'COR', 'BDL', 'WRG']]]


    sides = [[[1,'SID','FU'],[1,'SID','FU','YO']],
    [[3, 'SID', 'UR'], [3, 'COR', 'UR', 'OB']],
    [[5, 'SID', 'BU'], [5, 'SID', 'BU', 'WO']],
    [[7, 'SID', 'UL'], [7, 'SID', 'UL', 'OG']],
    [[9, 'SID', 'FL'], [9, 'SID', 'FL', 'YO']],
    [[11, 'SID', 'FR'], [11, 'COR', 'FR', 'YB']],
    [[13, 'SID', 'BR'], [13, 'SID', 'BR', 'WB']],
    [[15, 'SID', 'BL'], [15, 'SID', 'BL', 'WG']],
    [[18, 'SID', 'FD'], [18, 'SID', 'FD', 'YR']],
    [[20, 'SID', 'DR'], [20, 'SID', 'DR', 'RB']],
    [[22, 'SID', 'BD'], [22, 'SID', 'BD', 'WR']],
    [[24, 'SID', 'DL'], [24, 'SID', 'DL', 'RG']]]


    middle = [[[8,'MID','U'],[8,'MID','U','O']],
    [[10, 'MID', 'F'], [10, 'MID', 'F', 'Y']],
    [[12, 'MID', 'R'], [12, 'MID', 'R', 'B']],
    [[14, 'MID', 'B'], [14, 'MID', 'B', 'W']],
    [[16, 'MID', 'L'], [16, 'MID', 'L', 'R']],
    [[25, 'MID', 'D'], [25, 'MID', 'D', 'R']]]

    # Probably a better Idea to Keep Everything in one list.
    #cubes = [corners,sides,middle]

    cube = []
    for i in corners:
        cube.append(i)
    for i in middle:
        cube.append(i)

    for i in sides:
        cube.append(i)

    cube.sort()
    return cube



def cubeLookUp(cube):
    pass


# In this a becomes b, b becomes c... d becomes a
# a,b,c,d are numbers, and current positions
def fourWaySwap(a,b,c,d,cube):

    # A to B
    holderX = cube[d][1]
    cube[d][1] = cube[c][1]
    cube[c][1] = cube[b][1]
    cube[b][1] = cube[a][1]
    cube[a][1] = holderX

    print('Swap')
    for i in cube:
        print(i)



def moveUp(cube):
    pass


"""
Up goes CW
Only involves Top Row
Basic Swap of Identities


"""


def movementFlowControl(x,cube):
    pass




cube = cubeInitial()
for i in cube:
    print(i)

fourWaySwap(1,2,4,6,cube)

































"""
All Cubes Inital Positions
Top Row
0 COR FUL YOG
1 SID FU YO
2 COR FUR YOB
3 SID UR OB
4 COR BUR WOB
5 SID BU WO 
6 COR BUL WOG
7 SID UL OG
8 MID U O

Middle Row
9 SID FL YO
10 MID F Y
11 SID FR YB
12 MID R B
13 SID BR BW
14 MID B W
15 SID BL WG
16 MID L G

Bottom Row
17 COR FDL YRG
18 SID FD YR
19 COR FDR YRB
20 SID DR RB
21 COR BDR WRB
22 SID BD WR
23 COR BDL WRG
24 SID DL RG
25 MID D R



"""



