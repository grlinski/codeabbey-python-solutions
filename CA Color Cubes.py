

# Colour Cubes
# https://www.codeabbey.com/index/task_list





def scorer(count):
    score = (count * (count + 1) )/ 2
    return score



def rowToCol(grid):
    newGrid = []




    for r in range(0,len(grid)):
        temp = []
        for c in range(0, len(grid)):
            temp.append(grid[c][r])
        newGrid.append(temp)

    return newGrid



# STEP 1
# This takes in coordinates x,y
# Any cells of the same type touching are replaced with 'X'
# Count how many X's added/numbers removed.
# Collapse later.
# Returns the count and the new grid
def removeAdjacentCells(x,y,grid):

    # q is the number I'm looking for

    q = grid[x][y]
    if q == '-':
        return 0,grid

    count=1
    grid[x][y] = 'X'


    changes = True
    while changes == True:
        changes = False
        for r in range(0,len(grid)):
            for c in range(0,len(grid)):
                cur = grid[r][c]
                try:
                    up = grid[r+1][c]
                except:
                    up = 'N'
                try:
                    down = grid[r-1][c]
                except:
                    down = 'N'
                try:
                    right = grid[r][c+1]
                except:
                    right = 'N'
                try:
                    left = grid[r][c-1]
                except:
                    left = 'N'
                if cur =='X':
                    if up == q:
                        grid[r + 1][c] = 'X'
                        changes = True
                        count+=1
                    if down == q:
                        grid[r -1][c] = 'X'
                        changes = True
                        count+=1
                    if right == q:
                        grid[r][c+1] = 'X'
                        changes = True
                        count+=1
                    if left == q:
                        grid[r][c-1] = 'X'
                        changes = True
                        count+=1

    # Easier Count
    count = 0
    for r in range(0,len(grid)):
        for c in range(0,len(grid[0])):
            if grid[r][c] == 'X':
                count+=1

    print('Count',count)
    for i in grid:
        print(i)

    return count,grid


# STEP 2
# Collapses the grid downward first
# After which if there is an entire row empty, or rather full of '-'
# Move rows to fill the left.
def collapseGrid(grid):

    #MOVE DOWN

    changes = True
    while changes == True:
        changes = False

        for r in range(0, len(grid)):
            for c in range(0, len(grid)):
                cur = grid[r][c]
                try:
                    down = grid[r + 1][c]
                except:
                    down = 'N'

                if cur != 'X' and cur!= '-':
                    if down == 'X':
                        grid[r+1][c] = cur
                        grid[r][c] = 'X'
                        changes = True

    for c in range(0, len(grid)):
        for r in range(0, len(grid)):
            cur = grid[r][c]
            if cur == 'X':
                grid[r][c] ='-'

    grid = rowToCol(grid)
    toDelete = []
    newGrid = []
    blankRow = []
    nBlankRows = 0

    for i in grid:
        add = False
        for j in i:
            if j !='-':
                add = True
        if add == True:
            newGrid.append(i)
        else:
            nBlankRows+=1
            blankRow = i
    for i in range(nBlankRows):
        newGrid.append(blankRow)

    grid = rowToCol(newGrid)


    # Collapse




    return grid








def flowControl(moves,grid):
    totalScore = 0
    for i in moves:
        x = i[0]
        y = i[1]
        #print('Remove',i)
        count,grid = removeAdjacentCells(x,y,grid)
        print(count)
        totalScore+=scorer(count)
        #print('Collapse')
        grid = collapseGrid(grid)
    print(totalScore)












size = int(input())
grid = []

for i in range(size):
    temp = []
    x = input()
    for j in x:
        temp.append(int(j))
    grid.append(temp)


nmoves =  int(input())
umoves = input()
moves = []
for i in range(0,len(umoves),5):
    a = int(umoves[i])
    a = (size-a)-1
    b = int(umoves[i+2])
    temp = [a,b]
    moves.append(temp)


flowControl(moves,grid)



