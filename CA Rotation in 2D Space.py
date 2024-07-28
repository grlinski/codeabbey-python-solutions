

import math

nstars,rot = map(int, input().split(' '))

# Rotation is Counter Clock Wise


stars = []
q = []

rad = math.radians(rot)
print(rad)
print(math.cos(rad))


for i in range(nstars):
    a,b,c = input().split(' ')
    b1 = int(b)
    c1 = int(c)
    q.append(a)
    q.append(b1)
    q.append(c1)
    stars.append(q)
    q = []

#x2 = xcos(deg) - ysin(deg)
#y2 = ycos(deg) + xsin(deg)

newstars = []
q = []

ss = []
xx = []
yy = []


for i in stars:
    x = i[1]
    y = i[2]

    sin = math.sin(rad)
    cos = math.cos(rad)

    nx = round((x*cos)-(y*sin))
    ny = round((y*cos)+(x*sin))

    q.append(i[0])
    q.append(nx)
    q.append(ny)

    ss.append(i[0])
    xx.append(nx)
    yy.append(ny)





    newstars.append(q)
    q = []

print(newstars)

print()
count = 0
endcount = len(ss)

# Some Other Time Getting a Better Sorting Algorithm
# For this one there is a possibility of a wrong answer if the y values are the same

while True:
    miniy = min(yy)
    for i in range(0,len(ss)):
        if yy[i] == miniy:
            print(ss[i])

            count+=1

            del(ss[i])
            del(yy[i])
            break
    if count==endcount:
        break

















