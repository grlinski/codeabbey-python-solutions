

# Parity Control
# https://www.codeabbey.com/index/task_view/parity-control


"""
Completed

End Notes:
Maybe make a series of function that convert between certain types
binToInt
intToBin
Hex
Oct
Etc...

Or even just one function, that converts based on what we want
Example
item is 5E
want binary, ie b
i = int
h = hex
and so on.
def convert(item,b)


"""




# Counts the Amount of 0s and 1s in a binary string
# If the amount of 1s is Even, returns True
# Else False
def bitCount(b):
    oneCount = 0
    zeroCount = 0

    for i in b:
        if i=='0':
            zeroCount+=1
        else:
            oneCount+=1

    if oneCount%2 == 0:
        return True
    else:
        return False



def bitChecker(b):
    oneCount = 0
    zeroCount = 0

    for i in b:
        if i == '0':
            zeroCount += 1
        else:
            oneCount += 1

    addTo = True
    if len(b) == 8 and oneCount%2 ==0:
        b = b[1:]
        addTo = True
    elif len(b) == 8 and oneCount%2==1:
        b = b[1:]
        addTo = False
    elif oneCount%2 == 1:
        addTo = False


    return b,addTo



# Takes in an Int
# Return a string binary version
def intToBinary(x):
    y = bin(x)
    s = y[2:]
    return s


def binaryToCharacter(b):
    x = int(b,2)
    y = chr(x)
    return y



q = list(map(int, input().strip().split(' ')))
ansList = []
for i in q:
    x = intToBinary(i)
    y,addTo = bitChecker(x)

    if addTo:
        z = binaryToCharacter(y)
        print(i, x, y)
        print(z)
        ansList.append(z)
print(ansList)

print()
for i in ansList:
    print(i,end='')
"""

65 238 236 225 46

"""



