# Rubix's Cube Mk2
# https://www.codeabbey.com/index/task_view/rubiks-cube


"""
Mark 2 Notes
I realized that an imporant part is the orientation of the cubes, not just their relocation.
So another section is needed in the current section.
This is the orientation of the colours.
This will be a position 1 of the individual cube list.
It will be sort of a combination of the current positions orientation
And the orientation of the colours.

Minor Note My Real Life Cube is a Mirror Image of the Virtual One
I'm going with Code Abbeys Version instead of mine.




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
def copyCubeSegment(cube,num):
    copyCat = []
    for i in cube[num]:
        copyCat.append(i)
    return copyCat

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
    corners = [[[0, 'COR', 'FUL'], [0, 'COR', 'FUL', 'YOG']],
               [[2, 'COR', 'FUR'], [2, 'COR', 'FUR', 'YOB']],
               [[4, 'COR', 'BUR'], [4, 'COR', 'BUR', 'WOB']],
               [[6, 'COR', 'BUL'], [6, 'COR', 'BUL', 'WOG']],
               [[17, 'COR', 'FDL'], [17, 'COR', 'FDL', 'YRG']],
               [[19, 'COR', 'FDR'], [19, 'COR', 'FDR', 'YRB']],
               [[21, 'COR', 'BDR'], [21, 'COR', 'BDR', 'WRB']],
               [[23, 'COR', 'BDL'], [23, 'COR', 'BDL', 'WRG']]]

    sides = [[[1, 'SID', 'FU'], [1, 'SID', 'FU', 'YO']],
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

    middle = [[[8, 'MID', 'U'], [8, 'MID', 'U', 'O']],
              [[10, 'MID', 'F'], [10, 'MID', 'F', 'Y']],
              [[12, 'MID', 'R'], [12, 'MID', 'R', 'B']],
              [[14, 'MID', 'B'], [14, 'MID', 'B', 'W']],
              [[16, 'MID', 'L'], [16, 'MID', 'L', 'R']],
              [[25, 'MID', 'D'], [25, 'MID', 'D', 'R']]]

    # Probably a better Idea to Keep Everything in one list.
    # cubes = [corners,sides,middle]
    # This now unclues a new portion 1, which is the orientation of the cube.
    """
    cube = [[[0, 'COR', 'FUL'], [['F', 'Y'], ['U', 'O'], ['L', 'G']] , [0, 'COR', 'FUL', 'YOG']],
    [[1, 'SID', 'FU'] , [['F', 'Y'], ['U', 'O']] , [1, 'SID', 'FU', 'YO']],
    [[2, 'COR', 'FUR'] , [['F', 'Y'], ['U', 'O'], ['R', 'B']] , [2, 'COR', 'FUR', 'YOB']],
    [[3, 'SID', 'UR'] , [['U', 'O'], ['R', 'B']], [3, 'COR', 'UR', 'OB']],
    [[4, 'COR', 'BUR'] , [['B', 'W'], ['U', 'O'], ['R', 'B']], [4, 'COR', 'BUR', 'WOB']],
    [[5, 'SID', 'BU'] , [['B', 'W'], ['U', 'O']], [5, 'SID', 'BU', 'WO']],
    [[6, 'COR', 'BUL'] , [['B', 'W'], ['U', 'O'], ['L', 'G']] , [6, 'COR', 'BUL', 'WOG']],
    [[7, 'SID', 'UL'] , [['U', 'O'], ['L', 'G']] , [7, 'SID', 'UL', 'OG']],
    [[8, 'MID', 'U'] ,[['U', 'O']] , [8, 'MID', 'U', 'O']],
    [[9, 'SID', 'FL'] , [['F', 'Y'], ['L', 'O']], [9, 'SID', 'FL', 'YO']],
    [[10, 'MID', 'F'] , [['F', 'Y']] , [10, 'MID', 'F', 'Y']],
    [[11, 'SID', 'FR'] , [['F', 'Y'], ['R', 'B']] , [11, 'COR', 'FR', 'YB']],
    [[12, 'MID', 'R'] , [['R', 'B']] , [12, 'MID', 'R', 'B']],
    [[13, 'SID', 'BR'] , [['B', 'W'], ['R', 'B']] , [13, 'SID', 'BR', 'WB']],
    [[14, 'MID', 'B'] , [['B', 'W']] , [14, 'MID', 'B', 'W']],
    [[15, 'SID', 'BL'] , [['B', 'W'], ['L', 'G']], [15, 'SID', 'BL', 'WG']],
    [[16, 'MID', 'L'] , [['L', 'R']] , [16, 'MID', 'L', 'R']],
    [[17, 'COR', 'FDL'] , [['F', 'Y'], ['D', 'R'], ['L', 'G']] , [17, 'COR', 'FDL', 'YRG']],
    [[18, 'SID', 'FD'] , [['F', 'Y'], ['D', 'R']] , [18, 'SID', 'FD', 'YR']],
    [[19, 'COR', 'FDR'] , [['F', 'Y'], ['D', 'R'], ['R', 'B']] , [19, 'COR', 'FDR', 'YRB']],
    [[20, 'SID', 'DR'] , [['D', 'R'], ['R', 'B']] , [20, 'SID', 'DR', 'RB']],
    [[21, 'COR', 'BDR'] , [['B', 'W'], ['D', 'R'], ['R', 'B']] , [21, 'COR', 'BDR', 'WRB']],
    [[22, 'SID', 'BD'] , [['B', 'W'], ['D', 'R']], [22, 'SID', 'BD', 'WR']],
    [[23, 'COR', 'BDL'] ,[['B', 'W'], ['D', 'R'], ['L', 'G']] , [23, 'COR', 'BDL', 'WRG']],
    [[24, 'SID', 'DL'] , [['D', 'R'], ['L', 'G']] , [24, 'SID', 'DL', 'RG']],
    [[25, 'MID', 'D'] , [['D', 'R']] , [25, 'MID', 'D', 'R']]]
    """
    cube = [[[0, 'COR', 'FUL'], [['F', 'Y'], ['U', 'O'], ['L', 'G']], [0, 'COR', 'FUL', 'YOG']],
            [[1, 'SID', 'FU'], [['F', 'Y'], ['U', 'O']], [1, 'SID', 'FU', 'YO']],
            [[2, 'COR', 'FUR'], [['F', 'Y'], ['U', 'O'], ['R', 'B']], [2, 'COR', 'FUR', 'YOB']],
            [[3, 'SID', 'UR'], [['U', 'O'], ['R', 'B']], [3, 'COR', 'UR', 'OB']],
            [[4, 'COR', 'BUR'], [['B', 'W'], ['U', 'O'], ['R', 'B']], [4, 'COR', 'BUR', 'WOB']],
            [[5, 'SID', 'BU'], [['B', 'W'], ['U', 'O']], [5, 'SID', 'BU', 'WO']],
            [[6, 'COR', 'BUL'], [['B', 'W'], ['U', 'O'], ['L', 'G']], [6, 'COR', 'BUL', 'WOG']],
            [[7, 'SID', 'UL'], [['U', 'O'], ['L', 'G']], [7, 'SID', 'UL', 'OG']],
            [[8, 'MID', 'U'], [['U', 'O']], [8, 'MID', 'U', 'O']],
            [[9, 'SID', 'FL'], [['F', 'Y'], ['L', 'O']], [9, 'SID', 'FL', 'YO']],
            [[10, 'MID', 'F'], [['F', 'Y']], [10, 'MID', 'F', 'Y']],
            [[11, 'SID', 'FR'], [['F', 'Y'], ['R', 'B']], [11, 'COR', 'FR', 'YB']],
            [[12, 'MID', 'R'], [['R', 'B']], [12, 'MID', 'R', 'B']],
            [[13, 'SID', 'BR'], [['B', 'W'], ['R', 'B']], [13, 'SID', 'BR', 'WB']],
            [[14, 'MID', 'B'], [['B', 'W']], [14, 'MID', 'B', 'W']],
            [[15, 'SID', 'BL'], [['B', 'W'], ['L', 'G']], [15, 'SID', 'BL', 'WG']],
            [[16, 'MID', 'L'], [['L', 'R']], [16, 'MID', 'L', 'R']],
            [[17, 'COR', 'FDL'], [['F', 'Y'], ['D', 'R'], ['L', 'G']], [17, 'COR', 'FDL', 'YRG']],
            [[18, 'SID', 'FD'], [['F', 'Y'], ['D', 'R']], [18, 'SID', 'FD', 'YR']],
            [[19, 'COR', 'FDR'], [['F', 'Y'], ['D', 'R'], ['R', 'B']], [19, 'COR', 'FDR', 'YRB']],
            [[20, 'SID', 'DR'], [['D', 'R'], ['R', 'B']], [20, 'SID', 'DR', 'RB']],
            [[21, 'COR', 'BDR'], [['B', 'W'], ['D', 'R'], ['R', 'B']], [21, 'COR', 'BDR', 'WRB']],
            [[22, 'SID', 'BD'], [['B', 'W'], ['D', 'R']], [22, 'SID', 'BD', 'WR']],
            [[23, 'COR', 'BDL'], [['B', 'W'], ['D', 'R'], ['L', 'G']], [23, 'COR', 'BDL', 'WRG']],
            [[24, 'SID', 'DL'], [['D', 'R'], ['L', 'G']], [24, 'SID', 'DL', 'RG']],
            [[25, 'MID', 'D'], [['D', 'R']], [25, 'MID', 'D', 'R']]]
    #cube.sort()
    return cube


def copyRow(row):
    newRow = []
    for i in row:
        newRow.append(i)
    return newRow

def cubeLookUp(cube):
    pass


# In this a becomes b, b becomes c... d becomes a
# a,b,c,d are numbers, and current positions
def fourWaySwap(a, b, c, d, cube, order):
    # A to B
    holderA = copyCubeSegment(cube,a)
    holderB = copyCubeSegment(cube,b)
    holderC = copyCubeSegment(cube,c)
    holderD = copyCubeSegment(cube,d)

    print('Holders')
    print(holderA)
    print(holderB)
    print(holderC)
    print(holderD)

    finalAOri = reorientCorners(holderA[1], holderD[1], order)
    finalBOri = reorientCorners(holderB[1],holderA[1],order)
    finalCOri = reorientCorners(holderC[1], holderB[1], order)
    finalDOri = reorientCorners(holderD[1], holderC[1], order)
    print(holderA[1])
    print(holderB[1])
    print(holderC[1])
    print(holderD[1])

    print()
    print('Finals ABCD')
    print(finalAOri)
    print(finalBOri)
    print(finalCOri)
    print(finalDOri)



    tempA2 = copyRow(cube[d][2])
    tempB2 = copyRow(cube[c][2])
    tempC2 = copyRow(cube[b][2])
    tempD2 = copyRow(cube[a][2])

    tempA0 = copyRow(cube[a][0])
    tempB0 = copyRow(cube[b][0])
    tempC0 = copyRow(cube[c][0])
    tempD0 = copyRow(cube[d][0])


    ansA = [tempA0,finalAOri,tempA2]
    ansB = [tempB0, finalBOri, tempB2]
    ansC = [tempC0, finalCOri, tempC2]
    ansD = [tempD0, finalDOri, tempD2]

    cube[a] = ansA
    cube[b] = ansB
    cube[c] = ansC
    cube[d] = ansD





    for i in cube:
        print(i)


    return cube

def reorientCorners(initial, incoming,order):

    # Order Needs to be more direct, intial at
    #order = [[0,2],[1,1],[2,0]]
    #print('Start')

    initial =copyRow(initial)
    imcoming = copyRow(incoming)
    print(initial)
    print(incoming)
    for i in order:
        x = i[0]
        y = i[1]
        print(initial[x][1],incoming[y][1])
        initial[x][1] = incoming[y][1]

    #print(initial)
    return initial





def moveUp(cube):
    a  = 6
    b = 4
    c = 2
    d = 0

    # For the order, the first letter is replaced by the second.
    # This so far is only for the corners.
    order = [[0,2],[1,1],[2,0]]
    fourWaySwap(a,b,c,d,cube,order)

    # Reorient
    # Up position Does Not Change
    """
    Right becomes front
    Front becomes left
    Left become Back
    Back becomes right
    
    
    """



"""
Up goes CW
Only involves Top Row
Basic Swap of Identities


"""


def movementFlowControl(x, cube):
    pass


cube = cubeInitial()
for i in cube:
    print(i)





#fourWaySwap(0, 2, 4, 6, cube)
moveUp(cube)
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



