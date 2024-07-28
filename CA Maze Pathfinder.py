
# Maze Pathfinder
# https://www.codeabbey.com/index/task_view/maze-pathfinder

"""
Completed


Ending Notes:







For this they recommend the wave propagation formula
Try my way first then theirs.


My Way, Still in Development
Remove Dead Ends
Maybe mark certain nodes which when touched lead to the end.
For example once dead ends are gone, try to reach From the top left corner to the bottom right.
Since I know this path will lead to the start, I can change any 1s to another value maybe 3 or something
And If I touch a 3 from another corner I know it will lead to the start.



"""

# Copy Grid
##############################################################################
def copyGrid(grid):
    newGrid = []

    for i in range(0,len(grid)):
        temp = []
        for j in range(0,len(grid[i])):
            x = grid[i][j]
            temp.append(x)
        newGrid.append(temp)
    return newGrid




def printGrid(grid):
    for i in grid:
        print(i)

# Adds 0s to the outside of the grid
def padding(x):
    rleng = len(x)
    cleng = (len(x[0]))

    #print(rleng,cleng)
    topper = []
    for i in range(cleng-2):
        topper.append('0')
    x.insert(0,topper)
    x.append(topper)
    for i in range(rleng+2):
        x[i].insert(0,'0')
        x[i].append('0')

    #print('Padding')
    #printGrid(x)

    return x


# Just adds Letters to Define Start points and Corners
def cornersABCS(grid):
    grid[1][1] = 'S'
    rleng = len(grid)
    cleng = (len(grid[0]))
    grid[rleng-2][cleng-2] = 'C'
    grid[rleng - 2][1] = 'B'
    grid[1][cleng - 2] = 'A'

    return grid



# Removes Dead Ends in the Grid
def refineMap(grid):


    changes = True
    rleng = len(grid)
    cleng = (len(grid[0]))
    i = 1
    j = 1


    while True:
        x = grid[i][j]
        if x == 'C' and changes == True:
            i = 1
            j = 1
            changes = False
        elif x== 'C' and changes == False:
            break
        elif x == 'A' or x == 'B' or x == 'S' or x == '0':
            pass
        elif x == '1':

            zeroCount = 0
            up = grid[i-1][j]
            rt = grid[i][j+1]
            dn = grid[i+1][j]
            lt = grid[i][j-1]

            if up == '0':
                zeroCount+=1
            if rt == '0':
                zeroCount += 1
            if dn == '0':
                zeroCount+=1
            if lt == '0':
                zeroCount+=1

            if zeroCount >=3:
                grid[i][j] = '0'
                changes = True


        j+=1
        if j == cleng:
            j = 0
            i+=1

    return grid










# Changes 1s to Ps if the 1 touches a P, or S.
def pathway(grid):
    changes = True
    rleng = len(grid)
    cleng = (len(grid[0]))
    i = 1
    j = 1

    while True:

        x = grid[i][j]
        #print(x,i,j)


        if x == 'C' and changes == True:
            i = 1
            j = 1
            changes = False
        elif x == 'C' and changes == False:
            break
        elif x == 'A' or x == 'B' or x == '0':
            pass
        elif x=='S':
            rt = grid[i][j + 1]
            dn = grid[i + 1][j]

            if rt =='1':
                grid[i][j + 1] = 'P'
            if dn =='1':
                grid[i + 1][j] = 'P'

        elif x == '1':

            up = grid[i - 1][j]
            rt = grid[i][j + 1]
            dn = grid[i + 1][j]
            lt = grid[i][j - 1]

            if up == 'P' or rt == 'P' or dn =='P' or lt == 'P':
                grid[i][j] = 'P'
                changes = True
        elif x == 'P':
            up = grid[i - 1][j]
            rt = grid[i][j + 1]
            dn = grid[i + 1][j]
            lt = grid[i][j - 1]

            if up == '1':
                grid[i - 1][j] = 'P'
                changes = True
            if rt == '1':
                grid[i][j + 1] = 'P'
                changes = True
            if dn == '1':
                grid[i + 1][j] = 'P'
                changes = True
            if lt == '1':
                grid[i][j - 1] = 'P'
                changes = True





        j += 1
        if j == cleng:
            j = 0
            i += 1

    return grid



# Starts at A,B or C and removes that pathway.
def killPath(grid,corner):
    rleng = len(grid)
    cleng = (len(grid[0]))


    if corner == 'A':
        r = 1
        c = cleng - 2
    elif corner == 'B':
        r = rleng - 2
        c = 1
    elif corner == 'C':
        r = rleng - 2
        c = cleng - 2

    while True:
        x = grid[r][c]
        up = grid[r - 1][c]
        rt = grid[r][c + 1]
        dn = grid[r + 1][c]
        lt = grid[r][c - 1]
        pcount = 0
        if up == 'P':
            pcount += 1
        if rt == 'P':
            pcount += 1
        if dn == 'P':
            pcount += 1
        if lt == 'P':
            pcount += 1

        if pcount == 1:
            grid[r][c] = '0'
            if up == 'P':
                r -= 1
            if rt == 'P':
                c += 1
            if dn == 'P':
                r += 1
            if lt == 'P':
                c -= 1

        else:
            break
    return grid


# PathFinder
# Hopefully the Final Function
def pathfinder(grid,corner):

    rleng = len(grid)
    cleng = (len(grid[0]))

    if corner == 'A':
        r = 1
        c = cleng - 2
    elif corner == 'B':
        r = rleng - 2
        c = 1
    elif corner == 'C':
        r = rleng - 2
        c = cleng - 2


    lastMove = 'Z'
    totalMove = 0
    path = ''
    ender = False
    while True:

        x = grid[r][c]

        if x == 'S':
            totalMove += 1
            step = str(totalMove) + lastMove
            path += step
            ender = True
        if ender == True:
            break

        up = grid[r - 1][c]
        rt = grid[r][c + 1]
        dn = grid[r + 1][c]
        lt = grid[r][c - 1]

        if up == 'P':
            grid[r][c] = 'X'
            r -= 1
            if lastMove == 'U':
                totalMove+=1
            else:
                step = str(totalMove)+lastMove
                path+=step
                lastMove = 'U'
                totalMove = 1
        elif rt == 'P':
            grid[r][c] = 'X'
            c += 1
            if lastMove == 'R':
                totalMove+=1
            else:
                step = str(totalMove)+lastMove
                path+=step
                lastMove = 'R'
                totalMove = 1
        elif dn == 'P':
            grid[r][c] = 'X'
            r += 1
            if lastMove == 'D':
                totalMove+=1
            else:
                step = str(totalMove)+lastMove
                path+=step
                lastMove = 'D'
                totalMove = 1
        elif lt == 'P':
            grid[r][c] = 'X'
            c -= 1
            if lastMove == 'L':
                totalMove+=1
            else:
                step = str(totalMove)+lastMove
                path+=step
                lastMove = 'L'
                totalMove = 1
        else:
            totalMove+=1
            step = str(totalMove) + lastMove
            path += step
            break
    path = path[2:]
    return path




# FLOW CONTROL
#########################################################################################################
def flowControl(grid):
    #printGrid(grid)
    #print('Pad')
    grid = (padding(grid))
    #print('Corn')
    grid = cornersABCS(grid)
    #print('Refine')
    grid = refineMap(grid)
    #printGrid(grid)
    grid = pathway(grid)

    gridA = copyGrid(grid)
    gridA = killPath(gridA,'B')
    gridA = killPath(gridA, 'C')

    gridB = copyGrid(grid)
    gridB = killPath(gridB,'A')
    gridB = killPath(gridB, 'C')


    gridC = copyGrid(grid)
    gridC = killPath(gridC, 'B')
    gridC = killPath(gridC, 'A')


    a = pathfinder(gridA,'A')
    b = pathfinder(gridB,'B')
    c = pathfinder(gridC, 'C')

    print(a,b,c)



















w,h = map(int, input().split(' '))
grid = []
for i in range(0,h):
    s = input()
    temp = []
    for j in s:
        temp.append((j))
    grid.append(temp)


flowControl(grid)



