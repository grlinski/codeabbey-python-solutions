

# Paths in the Grid
# https://www.codeabbey.com/index/task_view/paths-in-the-grid

def printGrid(x):
    for i in x:
        print(i)


# Adds X's around the top and left side
# Makes life easier.
def padding(x):
    rleng = len(x)
    cleng = (len(x[0]))

    #print(rleng,cleng)
    topper = []
    for i in range(cleng-2):
        topper.append('X')
    x.insert(0,topper)
    x.append(topper)
    for i in range(rleng+2):
        x[i].insert(0,'X')
        x[i].append('X')

    #print('Padding')
    #printGrid(x)

    return x


def refineMap(grid):


    changes = True
    rleng = len(grid)
    cleng = (len(grid[0]))
    i = 1
    j = 1




    while True:
        x = grid[i][j]
        if x == '$' and changes == True:
            i = 1
            j = 1
            changes = False
        elif x== '$' and changes == False:
            break
        elif x == '@' or x == 'X':
            pass
        elif x == '+':
            up = grid[i-1][j]
            rt = grid[i][j+1]
            dn = grid[i+1][j]
            lt = grid[i][j-1]

            if up =='X' and lt == 'X':
                grid[i][j] = 'X'
                changes = True
            elif dn =='X' and rt == 'X':
                grid[i][j] = 'X'
                changes = True

        j+=1
        if j == cleng:
            j = 0
            i+=1

    return grid



# MAIN FUNCTION
# Pathways determines how many ways there are to get to a single position
# Then the adjacent down and right + positions inherit the total of this number.
# Should wind up with the correct answer at the bottom.
def pathways(grid):
    changes = True
    rleng = len(grid)
    cleng = (len(grid[0]))
    i = 1
    j = 1

    while True:
        x = grid[i][j]
        if x == '$':
            up = grid[i - 1][j]
            lt = grid[i][j - 1]
            ans = 0
            if up == 'X':
                pass
            else:
                ans +=int(up)

            if lt == 'X':
                pass
            else:
                ans +=int(lt)

            #print(up,lt)
            #printGrid(grid)

            return ans


        elif x == '@':
            grid[i][j] = str(1)
        elif x == '+':
            up = grid[i - 1][j]
            rt = grid[i][j + 1]
            dn = grid[i + 1][j]
            lt = grid[i][j - 1]
            total = 0

            if up == 'X':
                pass
            else:
                total+=int(up)
            if lt == 'X':
                pass
            else:
                total+=int(lt)
            grid[i][j] = str(total)

        j += 1
        if j == cleng:
            j = 0
            i += 1

    printGrid(grid)







r,c = map(int, input().split(' '))
grid = []
temp = []
for i in range(0,r):
    temp = list(map(str, input().strip().split(' ')))
    grid.append(temp)


grid = padding(grid)

grid = refineMap(grid)

ans = pathways(grid)
print(ans)



