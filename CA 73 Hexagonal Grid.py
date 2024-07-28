

"""
3
AABF
FEDCBA
BCB

X Y movements
A = 1 0
B = 0.5 1
C = -0.5 1
D = -1 0
E = -0.5 -1
F = 0.5 -1


"""
import math
holder = input()
timestorun = int(holder)
listofmoves = []
for i in range(0,timestorun):
    string1 = input()
    listofmoves.append(string1)
    string1 = ""
print(listofmoves)

x = 0
y = 0
upper = math.sqrt(0.75)



for i in listofmoves:
    x = 0
    y = 0
    distance = 0
    holder = i
    for j in holder:
        if j == "A":
            x = x +1
            y = y +0
        elif j == "B":
            x = x + 0.5
            y = y + upper
        elif j == "C":
            x = x -0.5
            y = y + upper
        elif j == "D":
            x = x -1
            y = y + 0
        elif j == "E":
            x = x - 0.5
            y = y - upper
        elif j == "F":
            x = x + 0.5
            y = y - upper
    #Here is the distance
    x = abs(x)
    y = abs(y)
    hyp = math.sqrt(x**2 + y**2)
    #print(x,y)
    print(hyp, end = " ")













