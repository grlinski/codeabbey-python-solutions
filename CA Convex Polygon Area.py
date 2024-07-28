

# Convex Polygon Area
# https://www.codeabbey.com/index/task_view/convex-polygon-area

"""
Convex angle meaning each of its angels are less than Pi/2
In radians presumably.


Mid Point Idea
Do a continually sliding midpoint
Pick two point find midpoint between those.
Then pick another point and redetermine the midpoint with this and the old midpoint
Keep going.



Determining the Area of a Scalene Triangle
Needs all 3 sides and Heron's Formula

Note Heron's formula does not work on Isosoles triangles
!!!!!
Probably not on Right Angle either.






"""


def midpoint(list1):
    miniX = 1000000
    maxiX = 0
    miniY = 1000000
    maxiY = 0
    leng = len(list1)
    for i in range(0,len(list1)):
        x = list1[i][0]
        y = list1[i][1]

        miniX = min(x,miniX)
        maxiX = max(x,maxiX)
        miniY = min(y,miniY)
        maxiY = max(y,maxiY)

    midX = (maxiX+miniX)/2
    midY = (maxiY+miniY)/2

    return midX,midY


# Def Triangles
# This will create coordinate to determine our triangles.
# Need to create rules.
"""
Start with leftmost coordinate.
Create a triangle with the nearest other coordinate.
Use X1-X2, Y1-Y2. If a coordinate has been part of two triangles delete it.
Third coordinate is always the midpoint.

Will create as many triangles are there are vertices.

"""
import math


# In the fourth position on Vert adds distances to the first vertex in the list
def distances(oriX,oriY,vert):



    for i in range(0,len(vert)):
        x = vert[i][0]
        y = vert[i][1]
        distance = math.sqrt((abs(oriX-x)**2)+(abs(oriY-y)**2))
        vert[i][3] = distance
    return vert



# Gives the Area of a Triangle Defined by 3 sides
# Uses Heron's Formula
# AFAIK It works
def createTriangle(x1,y1,x2,y2,x3,y3):

    s1 = math.sqrt((abs(x1-x2)**2)+(abs(y1-y2)**2))
    s2 = math.sqrt((abs(x2 - x3) ** 2) + (abs(y2 - y3) ** 2))
    s3 = math.sqrt((abs(x1 - x3) ** 2) + (abs(y1 - y3) ** 2))

    sP= (s1+s2+s3)/2

    area = math.sqrt(sP*(sP-s1)*(sP-s2)*(sP-s3))
    print('Area',area)
    return area

def used3(vert):
    newvert = []
    for i in range(len(vert)):
        x = vert[i][2]
        if x == 2:
            pass
        else:
            newvert.append(vert[i])
    return newvert




def triangles(vert,midX,midY):
    totalArea = 0
    firstVert = True

    while len(vert) >1:
        x = vert[0][0]
        y = vert[0][1]
        vertMinus =vert[1:]
        holder = [vert[0]]
        vert = holder+distances(x,y,vertMinus)
        nextX = vert[1][0]
        nextY = vert[1][1]
        print('Distances')
        print(vert)
        print('X1 Y1, X2 Y2, MidX, MidY')
        print(x,y,nextX,nextY,midX,midY)
        totalArea+=createTriangle(x,y,nextX,nextY,midX,midY)
        vert[0][2]+=1
        vert[1][2]+=1

        if firstVert:
            nextX = vert[2][0]
            nextY = vert[2][1]

            print('X1 Y1, X2 Y2, MidX, MidY')
            print(x, y, nextX, nextY, midX, midY)
            totalArea += createTriangle(x, y, nextX, nextY, midX, midY)
            vert[2][2] += 1
            vert[0][2] += 1
            firstVert = False


        vert = used3(vert)
    print(totalArea)






# X Y U D
# As in x and y coordinates
# Used as in how many triangles this coordinate has been in and
# D as in distance from this coordinate to the one we are looking at.
vert = []

items = int(input())
for i in range(items):
    a,b = map(int, input().split(' '))
    vert.append([a,b,0,0])


# X,Y Coordinates in Vert
# Sort by X first.

vert = sorted(vert, key = lambda x: x[0])
print(vert)

midX,midY = midpoint(vert)

triangles(vert,midX,midY)







"""
Testcases


4
0 0
0 10
10 0
10 10

Area should be 100


Hexagon
Area = 259.80762

6
15 1
5 1
0 10
5 19
15 19
20 10






"""













