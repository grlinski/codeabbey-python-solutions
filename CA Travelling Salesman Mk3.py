



# CA Travelling Salesman
# https://www.codeabbey.com/index/task_view/travelling-salesman

"""


Mark 3
I'm just going to do the row reduction method




Mark 2
For this I'm going to split up the codex into different parts
Maybe create a dictionary
Where the key is the city and the values are the connecting cities.



I just need a way to generate all paths
Which of course is a major problem so far.




"""


def generateMatrix(cities):
    matrix = []
    leng = len(cities)
    for i in range(0,leng):
        temp = []
        for j in range(0,leng):
            temp.append('x')
        matrix.append(temp)


    for i in cities:
        startCity = i[0]
        for j in range(1,len(i)):
            endCity = i[j][0]
            distance = i[j][1]
            #print(startCity,endCity,distance)
            matrix[startCity][endCity] = distance

    return matrix



# Converts the Data From Cities to an easier form
def easierCities(cities):
    newCities = []
    for c in cities:
        temp = []
        temp.append(int(c[0]))
        for i in range(1,len(c)):
            x = c[i]
            index = (x.index(':'))
            p1 = int(x[:index])
            p2 = int(x[index+1:])
            p3 = [p1,p2]
            temp.append(p3)
        newCities.append(temp)

    return newCities


"""
The Codex is a list of paths in the matrix.
The row is the city number
The first list item is the position for the second item
The second item is the list of paths from this city to others.
With the first item indicating the next move

"""
def createCodex(matrix):
    SUCodex = len(matrix)
    codex = []

    for i in range(SUCodex):
        temp = [0,[]]
        codex.append(temp)


    for i in range(0, len(matrix)):
        x = matrix[i]

        for j in range(0, len(x)):
            if x[j] == 'x':
                pass
            else:
                codex[i][1].append(j)

    # Too Lazy to Mess with the Codex
    # The dict and list are basically a split of the codex.

    cityStreets = {}
    positions = []


    for i in range(0,len(codex)):
        positions.append(0)
        x = codex[i][1]
        cityStreets[i] = x



    return codex,cityStreets,positions


def rowReduction(matrix):
    for r in range(0,len(matrix)):
        curRow = matrix[r]
        mini = 1000000000
        for j in curRow:
            if j=='x':
                pass
            else:
                mini = min(mini,j)
        for j in range(0,len(curRow)):
            if curRow[j] == 'x':
                pass
            else:
                matrix[r][j]-=mini

    return matrix



def rowToCol(matrix):
    newMatrix = []
    for r in range(0,len(matrix)):
        temp = []
        for c in range(0,len(matrix[r])):
            temp.append(matrix[c][r])
        newMatrix.append(temp)

    return newMatrix

def colReduction(matrix):
    # Flip Matrix

    matrix = rowToCol(matrix)

    for r in range(0,len(matrix)):
        curRow = matrix[r]
        mini = 1000000000
        for j in curRow:
            if j=='x':
                pass
            else:
                mini = min(mini,j)
        for j in range(0,len(curRow)):
            if curRow[j] == 'x':
                pass
            else:
                matrix[r][j]-=mini
    matrix = rowToCol(matrix)
    return matrix



def findCoordinates(matrix):
    coordinates = []
    for r in range(0,len(matrix)):
        for c in range(0,len(matrix[r])):
            x = matrix[r][c]
            if x == 0:
                coordinates.append(c)
                break

    return coordinates





def flowControl(matrix,originalMatrix):


    matrix = rowReduction(matrix)

    matrix = colReduction(matrix)
    matrix = rowReduction(matrix)

    matrix = colReduction(matrix)

    for i in matrix:
        print(i)


    #coordinates = findCoordinates(matrix)





cities = []

while True:
    x = input().split()
    if len(x) == 0:
        break
    cities.append(x)

cities = easierCities(cities)

matrix = generateMatrix(cities)
originalMatrix = generateMatrix(cities)

#codex,cityStreets,positions = createCodex(matrix)

flowControl(matrix,originalMatrix)


"""



0 1:90 2:42 3:90 5:29 
1 0:90 3:98 2:70 4:65 
2 0:42 1:70 5:30 3:36 4:97 6:46 
3 1:98 2:36 0:90 5:77 
4 1:65 2:97 6:68 
5 2:30 3:77 0:29 6:90 
6 5:90 2:46 4:68 









"""




























