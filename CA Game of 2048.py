

# Game of 2048
# https://www.codeabbey.com/index/task_view/game-of-2048
"""
Important Notes
I have no idea how the game actually works
I assume that the tiles fully slide if possible, but no idea.
I need to add this in if that's the case.
Maybe play the game and see.


Tiles do slide
Slide first merge later.


"""


def printGrid(grid):
    for i in grid:
        print(i)



def createCols(grid):

    c0 = []
    c1 = []
    c2 = []
    c3 = []
    for i in range(0,len(grid)):
        for j in range(0,len(grid)):
            x= grid[i][j]
            if j == 0:
                c0.append(x)
            elif j == 1:
                c1.append(x)
            elif j == 2:
                c2.append(x)
            elif j == 3:
                c3.append(x)
    return c0,c1,c2,c3



def deCreateCols(grid,c0,c1,c2,c3):
    for i in range(0,4):
        grid[i][0] = c0[i]
    for i in range(0,4):
        grid[i][1] = c1[i]
    for i in range(0,4):
        grid[i][2] = c2[i]
    for i in range(0,4):
        grid[i][3] = c3[i]
    return grid





# Easier to Create 4 Movement Functions than 1
def moveDown(col):
    if col[3] == col[2] and col[3]!= '-':
        col[3] = col[3]+col[2]
        col[2] = col[1]
        col[1] = col[0]
        col[0] = '-'
    elif col[2] == col[1] and col[2]!='-':
        col[2] = col[2]+col[1]
        col[1] = col[0]
        col[0] = '-'
    elif col[1] == col[0] and col[1]!='-':
        col[1] = col[1]+col[0]
        col[0] = '-'

    return col


def moveUp(col):
    if col[0] == col[1] and col[0] != '-':
        col[0] = col[1] + col[0]
        col[1] = col[2]
        col[2] = col[3]
        col[3] = '-'
    elif col[1] == col[2] and col[1] != '-':
        col[1] = col[1] + col[2]
        col[2] = col[3]
        col[3] = '-'
    elif col[2] == col[3] and col[2] != '-':
        col[2] = col[2] + col[3]
        col[3] = '-'

    return col


def moveRight(grid):
    r0 = grid[0]
    r1 = grid[1]
    r2 = grid[2]
    r3 = grid[3]






def movements(grid,directions):
    direct = 'R'

    if direct == 'D':
        c0, c1, c2, c3 = createCols(grid)
        c0 = moveDown(c0)
        c1 = moveDown(c1)
        c2 = moveDown(c2)
        c3 = moveDown(c3)
        grid = deCreateCols(grid,c0,c1,c2,c3)
    elif direct == 'U':

        c0, c1, c2, c3 = createCols(grid)
        c0 = moveUp(c0)
        c1 = moveUp(c1)
        c2 = moveUp(c2)
        c3 = moveUp(c3)
        grid = deCreateCols(grid, c0, c1, c2, c3)

    printGrid(grid)


grid = []
for i in range(4):
    s = list(map(int, input().strip().split(' ')))
    grid.append(s)
directions = input().split()

movements(grid,directions)



