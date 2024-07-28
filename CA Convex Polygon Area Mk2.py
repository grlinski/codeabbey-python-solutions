



# Convex Polygon Area
# https://www.codeabbey.com/index/task_view/convex-polygon-area

"""
Completed Notes
Well this was way easier than I tried to make it.
A simple approach is often the best.
Divide and conquer the problem.
I eventually did this by merely splitting the points up, above and below the midpoint.
This made the problem trivial at that point
However I learned some important things I should store for later.
Area of a Polygon
Area of a scalene triangle via Heron's Algorithm
Distance Between Points












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






Mark 2 Approach
So similar idea except we are just going left to right and never go past the mid point Y when making triangles
Except with the first Vertex and possibly the Last!!!!!!!









"""
import math

def printGrid(grid):
    for i in grid:
        print(i)



def midpoint(list1):

    midX = 0
    midY = 0
    amt = len(list1)
    for i in range(0,len(list1)):
        midX+=list1[i][0]
        midY+=list1[i][1]

    midX=midX/amt
    midY=midY/amt

    return midX,midY




# In the fourth position on Vert adds distances to the first vertex in the list
def distances(oriX,oriY,vert):

    for i in range(0,len(vert)):
        x = vert[i][0]
        y = vert[i][1]
        distance = math.sqrt((abs(oriX-x)**2)+(abs(oriY-y)**2))
        vert[i][3] = distance
    return vert

def distanceTwoPoints(a,b):
    x1 = a[0]
    y1 = a[1]

    x2 = b[0]
    y2 = b[1]
    distance = math.sqrt((abs(x1 - x2) ** 2) + (abs(y1 - y2) ** 2))
    return distance

# Returns the Area of a Triangle Based on 3 sets of coordinates.
def triangleArea(x1,y1,x2,y2,x3,y3):

    s1 = math.sqrt((abs(x1-x2)**2)+(abs(y1-y2)**2))
    s2 = math.sqrt((abs(x2 - x3) ** 2) + (abs(y2 - y3) ** 2))
    s3 = math.sqrt((abs(x1 - x3) ** 2) + (abs(y1 - y3) ** 2))

    sP= (s1+s2+s3)/2

    area = math.sqrt(sP*(sP-s1)*(sP-s2)*(sP-s3))
    print('Area',area)
    return area



def asAboveSoBelow(vert):
    above = []
    below = []
    midX, midY = midpoint(vert)
    for i in range(0,len(vert)):
        y = vert[i][1]
        if i == 0:
            above.append(vert[i])
            below.append(vert[i])
        elif i ==(len(vert)-1):
            above.append(vert[i])
            below.append(vert[i])
        else:
            if y >= midY:
                above.append(vert[i])
            else:
                below.append(vert[i])

    return above,below




# MAIN FUNCTION
# Sort Vertices into 2 lists, one above midpoint, the other below
# However keep first and last vertice in each.

# Reminder Vertices are sorted by X coordinate, lowest to highest
def createTriangles(vert):
    midX,midY = midpoint(vert)
    totalArea = 0
    above,below = asAboveSoBelow(vert)

    #print(len(above))
    #print(above)
    #print(len(below))
    #print(below)

    for i in range(0,len(above)-1):
        x1 = above[i][0]
        y1 = above[i][1]
        x2 = above[i+1][0]
        y2 = above[i+1][1]
        totalArea+=triangleArea(x1,y1,x2,y2,midX,midY)
    for i in range(0,len(below)-1):
        x1 = below[i][0]
        y1 = below[i][1]
        x2 = below[i+1][0]
        y2 = below[i+1][1]
        totalArea+=triangleArea(x1,y1,x2,y2,midX,midY)

    print(round(totalArea,1))







vert = []

items = int(input())
for i in range(items):
    a,b = map(int, input().split(' '))
    vert.append([a,b])


vert = sorted(vert, key = lambda x: x[0])

createTriangles(vert)





"""
Testcases


12
48 6
61 8
72 17
95 39
77 75
67 92
45 96
25 90
12 77
3 67
10 36
24 9

Mid Points
44.9 51



"""
































