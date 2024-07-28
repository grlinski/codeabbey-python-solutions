

# CA Travelling Salesman
# https://www.codeabbey.com/index/task_view/travelling-salesman

"""


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
    return codex






def checkTotal(matrix,used):

    total = 0

    for i in range(0,len(used)-1):
        a = used[i]
        b = used[i+1]
        x = matrix[a][b]
        total+=x
    return total















def flowControl(matrix,codex):

    # This really is more about going through the codex and comparing the path to the matrix to get total
    # So Most importantly how do I create a path through the codex?

    """
    If the current list of cities can go nowhere, as all its paths are in the used list.
    Then I need to increase the position of the previous city list and restart.
    Also make sure that if the position is == to the len of paths then I need to go back to zero.



    """


    totalCities = len(matrix)


    # How Many Times to Run?????
    counter = 0


    while True:
        # Start a City Zero
        # codex[?] = entire city row
        # codex[?][0] = position of next city
        # codex[?][1] = all connecting cities
        # codex[?][1][codex[?]] = next city

        #First City
        used = []
        used.append(0)
        curCity = 0
        cityRow = (codex[curCity])
        posOfNextCity = (codex[curCity][0])
        nextPaths = (codex[curCity][1])
        nextCity = codex[curCity][1][posOfNextCity]
        used.append(nextCity)
        checker = True

        while len(used) != len(codex):
            HoldCurCity = nextCity
            HoldPosOfNextCity = (codex[HoldCurCity][0])
            HoldNextPaths = (codex[HoldCurCity][1])
            HoldNextCity = codex[HoldCurCity][1][HoldPosOfNextCity]
            if HoldNextCity in used:
                codex[nextCity][0]+=1
                if codex[nextCity][0] == len(codex[nextCity][1]):
                    codex[nextCity][0] = 0

                # Get different in Items from this list1 and Used.
                # If the resulting list len == 0: break and checker == False.
                list1 = codex[nextCity][1]
                allSame = True
                for i in list1:
                    if i not in used:
                        allSame = False
                if allSame == True:
                    checker = False
                    break
            else:
                used.append(HoldNextCity)
                nextCity = HoldNextCity
            #print(used)

        if checker == True:
            total = checkTotal(matrix,used)
            print(total,used)



        codex[0][0]+=1
        if codex[0][0] == len(codex[0][1]):
            codex[0][0] = 0
        counter+=1
        if counter == 100:
            break

    for i in codex:
        print(i)

















cities = []

while True:
    x = input().split()
    if len(x) == 0:
        break
    cities.append(x)

cities = easierCities(cities)

matrix = generateMatrix(cities)

codex = createCodex(matrix)

flowControl(matrix,codex)


"""



0 1:90 2:42 3:90 5:29 
1 0:90 3:98 2:70 4:65 
2 0:42 1:70 5:30 3:36 4:97 6:46 
3 1:98 2:36 0:90 5:77 
4 1:65 2:97 6:68 
5 2:30 3:77 0:29 6:90 
6 5:90 2:46 4:68 









"""







