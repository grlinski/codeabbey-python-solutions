
# Rubix's Cube Mk5
# https://www.codeabbey.com/index/task_view/rubiks-cube


"""

Movements I Need to Recheck
BDR

So my program passes the initial input
5
L U F B B

However it was wrong with the test case
Note that L U F appear once Meaning likely they work correctly in my program
Back appears twice, which may mean it corrects itself,
R and D do not appear so who knows if it works.
Check again.



Mk5 Notes
Idea is to simplify
However this may mean to add more info and parts than is needed.
But that is to keep small part compartmentalized.

Major Note
I completely missed the fact that their ordering of the yellow faces is different than mine
Look at it again.
Goes in an idiotic order.







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

# COPY AND PRINTING FUNCTIONS
def printList(x):
    for i in x:
        print(i)

def copySeg(x):
    newX = []
    for i in range(0,len(x)):
        temp = []
        for j in range(0,len(x[i])):
            temp.append(x[i][j])
        newX.append(temp)
    return newX



def cubeInitial():

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

    # F B U D L R
    # Maybe simplify this, as corners only need 3 positons, FB, UD, LR
    # There is also likely an alg wherein I can just move positions of all colours one to get correct results.
    corners = [[[0, 'COR', 'FUL'], ['Y','O','G',7]],
               [[1, 'COR', 'FUR'], ['Y','O','B',9]],
               [[2, 'COR', 'BUR'], ['W','O','B',0]],
               [[3, 'COR', 'BUL'], ['W','O','G',0]],
               [[4, 'COR', 'FDL'], ['Y','R','G',1]],
               [[5, 'COR', 'FDR'], ['Y','R','B',3]],
               [[6, 'COR', 'BDR'], ['W','R','B',0]],
               [[7, 'COR', 'BDL'], ['W','R','G',0]]]


    # As far I can tell there's no good way to, define the sides without all positions
    # Since depending on where it is, it may lose one of its sides.
    # Example FR may become UL, losing the Front Back direction, and gaining UD
    # On second thought I can just do it with three positions again.
    # Same priority as above, but there will be one empty position
    # Check later to make sure colours match sides.
    sides = [[[0, 'SID', 'FUX'], ['Y', 'O', 'x',8]],
             [[1, 'SID', 'XUR'], ['x', 'O', 'B',0]],
             [[2, 'SID', 'BUX'], ['W', 'O', 'x', 0]],
             [[3, 'SID', 'XUL'], ['x', 'O', 'G',0]],
             [[4, 'SID', 'FXL'], ['Y', 'x', 'G',4]],
             [[5, 'SID', 'FXR'], ['Y', 'x', 'B',6]],
             [[6, 'SID', 'BXR'], ['W', 'x', 'B',0]],
             [[7, 'SID', 'BXL'], ['W', 'x', 'G',0]],
             [[8, 'SID', 'FDX'], ['Y', 'R', 'x',2]],
             [[9, 'SID', 'XDR'], ['x', 'R', 'B',0]],
             [[10, 'SID', 'BDX'], ['W', 'R','x',0]],
             [[11, 'SID', 'XDL'], ['x', 'R', 'G',0]]]


    middle = [[[0, 'MID', 'U'], [8, 'MID', 'U', 'O']],
              [[1, 'MID', 'F'], [10, 'MID', 'F', 'Y']],
              [[2, 'MID', 'R'], [12, 'MID', 'R', 'B']],
              [[3, 'MID', 'B'], [14, 'MID', 'B', 'W']],
              [[4, 'MID', 'L'], [16, 'MID', 'L', 'R']],
              [[5, 'MID', 'D'], [25, 'MID', 'D', 'R']]]


    return corners,sides



def moveUD(a,b,c,d,e,f,g,h,corners,sides):
    # a gets overtaken by b
    # And so on.
    oriA = copySeg(corners[a])
    oriB = copySeg(corners[b])
    oriC = copySeg(corners[c])
    oriD = copySeg(corners[d])




    holdA = copySeg(corners[a])
    holdB = copySeg(corners[b])
    holdC = copySeg(corners[c])
    holdD = copySeg(corners[d])

    holdA[1][0] = oriA[1][2]
    holdA[1][2] = oriA[1][0]
    holdB[1][0] = oriB[1][2]
    holdB[1][2] = oriB[1][0]
    holdC[1][0] = oriC[1][2]
    holdC[1][2] = oriC[1][0]
    holdD[1][0] = oriD[1][2]
    holdD[1][2] = oriD[1][0]

    corners[a][1] = holdB[1]
    corners[b][1] = holdC[1]
    corners[c][1] = holdD[1]
    corners[d][1] = holdA[1]

    #SIDES MOVEMENT
    ################################
    oriE = copySeg(sides[e])
    oriF = copySeg(sides[f])
    oriG = copySeg(sides[g])
    oriH = copySeg(sides[h])

    holdE = copySeg(sides[e])
    holdF = copySeg(sides[f])
    holdG = copySeg(sides[g])
    holdH = copySeg(sides[h])

    holdE[1][0] = oriE[1][2]
    holdE[1][2] = oriE[1][0]
    holdF[1][0] = oriF[1][2]
    holdF[1][2] = oriF[1][0]
    holdG[1][0] = oriG[1][2]
    holdG[1][2] = oriG[1][0]
    holdH[1][0] = oriH[1][2]
    holdH[1][2] = oriH[1][0]

    sides[e][1] = holdF[1]
    sides[f][1] = holdG[1]
    sides[g][1] = holdH[1]
    sides[h][1] = holdE[1]

    return corners,sides



def moveLR(a,b,c,d,e,f,g,h,corners,sides):
    # 0, 3, 4 7
    # a gets overtaken by b
    # And so on.
    oriA = copySeg(corners[a])
    oriB = copySeg(corners[b])
    oriC = copySeg(corners[c])
    oriD = copySeg(corners[d])

    #print(oriA)
    #print(oriB)


    holdA = copySeg(corners[a])
    holdB = copySeg(corners[b])
    holdC = copySeg(corners[c])
    holdD = copySeg(corners[d])

    holdA[1][0] = oriA[1][1]
    holdA[1][1] = oriA[1][0]
    holdB[1][0] = oriB[1][1]
    holdB[1][1] = oriB[1][0]
    holdC[1][0] = oriC[1][1]
    holdC[1][1] = oriC[1][0]
    holdD[1][0] = oriD[1][1]
    holdD[1][1] = oriD[1][0]

    corners[a][1] = holdB[1]
    corners[b][1] = holdC[1]
    corners[c][1] = holdD[1]
    corners[d][1] = holdA[1]

    # SIDES MOVEMENT
    # E is eaten by F
    ################################
    oriE = copySeg(sides[e])
    oriF = copySeg(sides[f])
    oriG = copySeg(sides[g])
    oriH = copySeg(sides[h])

    holdE = copySeg(sides[e])
    holdF = copySeg(sides[f])
    holdG = copySeg(sides[g])
    holdH = copySeg(sides[h])

    holdE[1][0] = oriE[1][1]
    holdE[1][1] = oriE[1][0]
    holdF[1][0] = oriF[1][1]
    holdF[1][1] = oriF[1][0]
    holdG[1][0] = oriG[1][1]
    holdG[1][1] = oriG[1][0]
    holdH[1][0] = oriH[1][1]
    holdH[1][1] = oriH[1][0]

    sides[e][1] = holdF[1]
    sides[f][1] = holdG[1]
    sides[g][1] = holdH[1]
    sides[h][1] = holdE[1]



    return corners, sides



def moveFB(a,b,c,d,e,f,g,h,corners,sides):
    oriA = copySeg(corners[a])
    oriB = copySeg(corners[b])
    oriC = copySeg(corners[c])
    oriD = copySeg(corners[d])

    holdA = copySeg(corners[a])
    holdB = copySeg(corners[b])
    holdC = copySeg(corners[c])
    holdD = copySeg(corners[d])

    holdA[1][1] = oriA[1][2]
    holdA[1][2] = oriA[1][1]
    holdB[1][1] = oriB[1][2]
    holdB[1][2] = oriB[1][1]
    holdC[1][1] = oriC[1][2]
    holdC[1][2] = oriC[1][1]
    holdD[1][1] = oriD[1][2]
    holdD[1][2] = oriD[1][1]

    corners[a][1] = holdB[1]
    corners[b][1] = holdC[1]
    corners[c][1] = holdD[1]
    corners[d][1] = holdA[1]
    #print(holdA)
    #print(holdB)
    #print(holdC)
    #print(holdD)


    # SIDES MOVEMENT
    # E is eaten by F
    ################################
    oriE = copySeg(sides[e])
    oriF = copySeg(sides[f])
    oriG = copySeg(sides[g])
    oriH = copySeg(sides[h])

    holdE = copySeg(sides[e])
    holdF = copySeg(sides[f])
    holdG = copySeg(sides[g])
    holdH = copySeg(sides[h])

    holdE[1][1] = oriE[1][2]
    holdE[1][2] = oriE[1][1]
    holdF[1][1] = oriF[1][2]
    holdF[1][2] = oriF[1][1]
    holdG[1][1] = oriG[1][2]
    holdG[1][2] = oriG[1][1]
    holdH[1][1] = oriH[1][2]
    holdH[1][2] = oriH[1][1]

    sides[e][1] = holdF[1]
    sides[f][1] = holdG[1]
    sides[g][1] = holdH[1]
    sides[h][1] = holdE[1]

    return corners,sides




def endGame(corners,sides):
    fullList = corners+sides
    preAnsList = []
    for i in fullList:
        if i[1][3] == 0:
            pass
        else:
            preAnsList.append(i)
    mid5 = [[1, 'MID', 'FXX'], ['Y','x','x',5]]
    preAnsList.append(mid5)


    ansList = sorted(preAnsList, key=lambda x: int(x[1][3]))



    for i in ansList:
        x = findY(i)
        print(x,end= ' ')




# This Will Find the Position of Y
# Return None if no Y in the second Position.
# Input is a single Row
def findY(row):
    if 'Y' not in row[1]:
        return None
    posY = row[1].index('Y')
    # Dimensions
    dim= row[0][2]
    return(dim[posY])



def flowControl(corners,sides,movements):

    for i in movements:
        if i == 'U':
            corners, sides = moveUD(0, 1, 2, 3, 0, 1, 2, 3, corners, sides)
        elif i == 'D':
            corners, sides = moveUD(5, 4, 7, 6, 11, 10, 9, 8, corners, sides)
        elif i == 'L':
            corners, sides = moveLR(0, 3, 7, 4, 3, 7, 11, 4, corners, sides)
        elif i == 'R':
            corners, sides = moveLR(1, 2, 6, 5, 1, 6, 9, 5, corners, sides)
        elif i == 'F':
            corners, sides = moveFB(1, 0, 4, 5, 0, 4, 8, 5, corners, sides)
        elif i == 'B':
            corners, sides = moveFB(2, 6, 7, 3, 2, 7, 10, 6, corners, sides)

    return corners,sides



corners,sides = cubeInitial()

cases = int(input())
q = input().split()
corners,sides = flowControl(corners,sides,q)
endGame(corners,sides)

printList(corners)




"""
Movement Checklist
U s,c
D s,c
L s,c
R s,c
U  s,c
B s,c

Looks Good
Only function I changes was Back, both sides and corners were wrong
Probably will have to check everything again.



"""































