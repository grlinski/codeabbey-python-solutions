
# Parity Control
# https://www.codeabbey.com/index/task_view/parity-control

s = list(map(int, input().strip().split(' ')))


def bitCount(item):
    oneCount = 0
    zeroCount = 0

    for i in item:
        if i=='0':
            zeroCount+=1
        else:
            oneCount+=1

    if oneCount%2 == 0:
        return True
    else:
        return False


def binaryToCharacter(item):
    x = int(item,2)
    y = chr(x)
    return y





for i in s:
    x = bin(i)
    #print(x)
    y = str(x[2:])
    if bitCount(y):
        print(binaryToCharacter(y))










