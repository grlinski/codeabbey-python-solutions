


# Game of 2048
# https://www.codeabbey.com/index/task_view/game-of-2048

"""
Completed

Ending Notes
Well I don't have a whole lot to end here with other than that I really should have ending notes on programs I finish
And maybe those that I don't.
What did I learn, well I reinforced the notion that I need to use abstraction.
It is easier to do one thing over and over than to write it out in different ways many times.
As in what I did with the direction of the grid.
I rotated it to face right, slid, merged and rotated it back.
Rotations are fairly simple and keeping the orientation in the same direction made everything else easier.
Not that it happened here, but always remember to never fully copy an array
Otherwise what happens to one happens to the other.



"""







"""

2 2 4 2
4 2 2 4
2 2 2 2
2 4 2 2
D R D L U



New Idea/Slightly Change
Instead of mainly going down, go Right.
Makes things easier since I'm working with rows as opposed to columns.



pseudoGrid = [[1,2,3,4],[5,6,7,8],['a','b','c','d'],['w','x','y','z']]



"""
import math


def createNewGrid():
    newGrid = []
    for i in range(0,4):
        temp = []
        for j in range(0,4):
            temp.append(0)
        newGrid.append(temp)
    return newGrid


def printGrid(grid):
    for i in grid:
        print(i)





# Rotates Up to Down and Vice Versa
# Now used to Swap Left and Right
# Seemingly Works
def rotate180(grid):
    newGrid = createNewGrid()
    # Only cols are different.

    for r in range(0,4):
        for c in range(0,4):
            newC = 3-c
            newGrid[r][newC] = grid[r][c]

    return newGrid



# Rotates Counter Clockwise
# Use With Down Direction
# Seeminly Works
def rotateCCW(grid):
    newGrid = createNewGrid()

    for r in range(0,4):
        for c in range(0,4):
            newC = 3-c
            newR = 3-r
            # Row becomes its column
            newGrid[newC][r] = grid[r][c]
    return newGrid

# Rotates ClockWise
# Use With Up Direction
def rotateClock(grid):
    newGrid = createNewGrid()
    for r in range(0, 4):
        for c in range(0, 4):
            newC = 3 - c
            newR = 3 - r
            newGrid[c][newR] = grid[r][c]
    return newGrid


# All this does is move Tiles to the Right
# Replacing the '-' tiles
def slideRight(grid):
    r0 = grid[0]
    r1 = grid[1]
    r2 = grid[2]
    r3 = grid[3]

    i = 0
    counter = 0
    while True:
        if r0[i]!= '-' and r0[i+1] =='-':
            r0[i+1] = r0[i]
            r0[i] = '-'
        if r1[i]!= '-' and r1[i+1] =='-':
            r1[i+1] = r1[i]
            r1[i] = '-'
        if r2[i]!= '-' and r2[i+1] =='-':
            r2[i+1] = r2[i]
            r2[i] = '-'
        if r3[i]!= '-' and r3[i+1] =='-':
            r3[i+1] = r3[i]
            r3[i] = '-'

        i+=1
        if i==3:
            i=0
            counter+=1
        if counter==4:
            break
    newGrid = []
    newGrid.append(r0)
    newGrid.append(r1)
    newGrid.append(r2)
    newGrid.append(r3)

    return newGrid


# This Merges Tiles with the Same Values
def mergeTiles(row):


    # Double Merge
    if row[0]==row[1] and row[2] == row[3] and row[0] !='-' and row[3]!='-':
        row[3] += row[2]
        row[2] = row[0]+row[1]

        row[0] = '-'
        row[1] = '-'
    # 3 and 2 Merge
    elif row[3] == row[2] and row[2]!='-':
        row[3]+=row[2]
        row[2] = row[1]
        row[1] = row[0]
        row[0] = '-'
    # 2 and 1 Merge
    elif row[2] == row[1] and row[1]!='-':
        row[2]+=row[1]
        row[1] = row[0]
        row[0] = '-'
    # 1 and 0 Merge
    elif row[1] == row[0] and row[0]!='-':
        row[1]+=row[0]
        row[0] = '-'
    else:
        pass

    return row


# This is to split the Rows Up and Send them to Merge Tiles
def mergeTilesFlowControl(grid):

    r0 = mergeTiles(grid[0])
    r1 = mergeTiles(grid[1])
    r2 = mergeTiles(grid[2])
    r3 = mergeTiles(grid[3])

    newGrid = []
    newGrid.append(r0)
    newGrid.append(r1)
    newGrid.append(r2)
    newGrid.append(r3)
    return newGrid






def flowControl(grid,directions):
    #d = 'U'
    for d in directions:
        if d == 'D':
            grid = rotateCCW(grid)
        elif d =='U':
            grid = rotateClock(grid)
        elif d =='R':
            pass
        elif d =='L':
            grid = rotate180(grid)

        grid = slideRight(grid)
        grid = mergeTilesFlowControl(grid)
        if d == 'D':
            grid = rotateClock(grid)
        elif d =='U':
            grid = rotateCCW(grid)
        elif d =='R':
            pass
        elif d =='L':
            grid = rotate180(grid)
        #print('------',d)
        #printGrid(grid)
    return grid



# Count Numbers
def countNumbers(grid):
    dict = {}
    maxi = 0
    for i in range(0,4):
        for j in range(0,4):
            x = grid[i][j]
            if x == '-':
                pass
            else:
                maxi = max(maxi,x)
                if x in dict:
                    dict[x]+=1
                else:
                    dict[x] =1
    finalAnswer(dict,maxi)

# Prints out how many times a number appears up to Maxi
def finalAnswer(dict,maxi):
    items = [2,4,8,16,32,64,128,256,512,1024,2048]
    start = 2
    factor = 1
    #print(maxi)
    while True:
        start = 2**factor
        #print('Start',start)
        if start > maxi:
            break
        else:
            if start in dict:
                print(dict[start],end=' ' )
            else:
                print(0,end=' ')
        factor+=1






grid = []
for i in range(4):
    s = list(map(int, input().strip().split(' ')))
    grid.append(s)
directions = input().split()
grid = flowControl(grid,directions)
countNumbers(grid)


#flowControl(grid,directions)


#pseudoGrid = [[1,2,'-',4],[5,'-',7,8],['a','-','c','-'],['-','-','y','z']]

#pseudoGrid = [[1,2,2,4],[5,6,7,8],[2,2,2,4],[2,2,2,2]]


#x = slideRight(pseudoGrid)

#printGrid(x)




















