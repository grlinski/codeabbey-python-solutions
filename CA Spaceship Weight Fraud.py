

# CA Spaceship Weight Fraud
# https://www.codeabbey.com/index/task_view/spaceship-weight-fraud



def listToString(x):
    string1 = ''
    counterPart = { 10:'A', 11:'B', 12:'C',13:'D', 14:'E', 15:'F'}

    for i in x:
        if i[0] in counterPart:
            y = counterPart[i[0]]
        else:
            y = str(i[0])
        string1+=(y)

    return string1



# FIND LARGEST
def findLargest(x,list1):
    # So for this I want to swap a smaller number near the start with the first instance of a larger number
    # As long as this larger number is after the smaller number.
    #

    # First find a larger number than the first index
    # Check cases where I need to move to the second index and where there's nothing larger.
    ender = False
    for i in range(0,len(list1)):
        if ender == True:
            break
        maxi = 0
        for k in range(len(list1)-1,i,-1):
            maxi = max(maxi,int(list1[k]))
        print(maxi)
        for j in range(len(list1)-1,i,-1):
            back = list1[j]
            front = list1[i]
            if back > front:
                holder1 = list1[j]
                holder2 = list1[i]

                list1[j] = holder2
                list1[i] = holder1

                ender = True

    # If there is no higher number possible, return a False Value
    if ender!=True:
        return list1,False
    else:
        return list1,True





def findSmallest(x,list1):
    # I want to swap the first Largest Number with the first smallest Number.
    ender = False
    for i in range(0,len(list1)):
        if ender == True:
            break
        for j in range(len(list1)-1,i,-1):
            back = list1[j]
            front = list1[i]
            if back > front:
                holder1 = list1[j]
                holder2 = list1[i]

                list1[j] = holder2
                list1[i] = holder1

                ender = True

    # If there is no higher number possible, return a False Value
    if ender!=True:
        return list1,False
    else:
        return list1,True







# INDEXER
"""
To Make Life Somewhat Easier this does multiple things
Separates a string into multiple parts with their index
Also the Full list contains everything, with letters converted to their numerical counterpart


"""
def indexer(x):
    numbers = []
    letters = []
    zeroes = []
    full = []
    num = '0123456789'
    counterPart = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}


    for i in range(0,len(x)):
        y = x[i]
        if y in num:
            a = [int(y)]
            full.append(a)
        else:
            y = counterPart[y]
            a = [y]
            full.append(a)

        y = x[i]

        if y in num:
            a = [y,i]
            numbers.append(a)
        elif y == '0':
            a = [y,i]
            zeroes.append(a)
        else:
            a = [y,i]
            letters.append(a)

    letters.sort()
    numbers.sort()
    zeroes.sort()

    #print(letters)
    #print(numbers)


    return full



def flowControl(x):

    list1 = indexer(x)
    list2 = indexer(x)

    maxi,goodValue = findLargest(x,list1)
    #mini,goodValue = findSmallest(x,list2)


    print(listToString(maxi))


cases = int(input())
for i in range(cases):
    x = input()
    flowControl(x)
    #indexer(x)






