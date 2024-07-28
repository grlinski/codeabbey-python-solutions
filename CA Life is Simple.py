

# Life is Simple
# https://www.codeabbey.com/index/task_view/life-is-simple



"""
Diagonals are Neighbours
Any organism that does have 2 or 3 neighbours die
Any empty cell with exactly 3 neighbours births a new organism


Seems to Work






"""


def gridExtension(grid):
    # How many rows and cols to add to each side.
    extend = 3
    col = len(grid[0])
    row = len(grid)




    for i in range(extend):
        addRow1 = []
        addRow2 = []
        for j in range(col):
            addRow1.append('-')
            addRow2.append('-')
        grid.insert(0,addRow1)
        grid.append(addRow2)

    for i in range(0,len(grid)):
        for j in range(extend):
            grid[i].insert(0,'-')
            grid[i].append('-')

    return grid


# Simply counts the number of Xs
def xCounter(grid):
    counter = 0
    for i in grid:
        for j in i:
            if j == 'X':
                counter+=1
    return counter



# Changes N to X and D to -
def setGrid(grid):
    col = len(grid[0])
    row = len(grid)

    for i in range(row):
        for j in range(row):
            if grid[i][j] == 'N':
                grid[i][j] = 'X'
            elif grid[i][j] == 'D':
                grid[i][j] = '-'
    return grid













def pg(grid):
    for i in grid:
        print(i)



# MAIN FUNCTION
#########################################
def nextTurn(grid):
    col = len(grid[0])
    row = len(grid)

    # B = Born
    # D = Dead
    times = 0
    for i in range(row):
        for j in range(col):
            #times+=1
            #print('Times',i,j,i+1)
            x = grid[i][j]
            # Positions starting at Up clockwise


            up = 'A'
            ur = 'A'
            ri = 'A'
            dr = 'A'
            do = 'A'
            dl = 'A'
            le = 'A'
            ul = 'A'

            # y,x
            if i-1 >=0:
                up = grid[i-1][j]
            if j+1 <col and i-1 >=0:
                ur = grid[i-1][j+1]
            if  j + 1 < col:
                ri = grid[i][j+1]
            if j + 1 < col and i + 1 < row:
                dr = grid[i+1][j+1]
            if i + 1 < row:
                do = grid[i+1][j]
            if j -1 >=0 and i +1 < row:
                dl = grid[i+1][j-1]
            if j - 1 >= 0:
                le = grid[i][j-1]
            if j - 1 >= 0 and i - 1 >= 0:
                ul = grid[i-1][j-1]

            #print(up,ur,ri,dr,do,dl,le,ul)
            #print(grid[i][j])
            #print(i,j)
            #print(j-1,grid[i][j-1])
            directions = [up,ur,ri,dr,do,dl,le,ul]
            if x == '-':
                counter = 0
                for d in directions:
                    # Can be X or an X that died this round, but still neighboured
                    if d=='X' or d == 'D':
                        counter+=1
                if counter == 3:
                    grid[i][j] = 'N'
            if x == 'X':
                counter = 0
                for d in directions:
                    if d=='X' or d == 'D':
                        counter+=1
                if counter == 2 or counter == 3:
                    pass
                else:
                    grid[i][j] = 'D'

    #pg(grid)
    grid = setGrid(grid)
    print(xCounter(grid),end= ' ')
    return grid

    #pg(grid)












grid = []
while True:
    x=input()
    if len(x) == 0:
        break
    y = []

    for i in x:
        y.append(i)
    grid.append(y)


grid = gridExtension(grid)
print('Original Grid, With Extension')
pg(grid)
print()


for t in range(5):
    grid = nextTurn(grid)

print()
pg(grid)




















