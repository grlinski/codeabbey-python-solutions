
import math, re


hold = input()
number = re.compile(r'\d+')
x,y = 0,0

totalx = 0
totaly = 0


while True:
    hold = input()
    try:
        feets, azis = (number.findall(hold))
    except:
        break
    if hold == "":
        break
    azi = int(azis)
    feet = int(feets)
    # Azimuth direction

    direction = int(azi/90)
    azi = azi%90
    # 0++, 1+-, 2--, 3-+
    degs = math.radians(azi)
    x = math.sin(degs)
    y = math.cos(degs)
    x = x*feet
    y = y*feet

    totalx = totalx+x
    totaly = totaly+y
    print(direction)
    if direction == 0:
        totalx = totalx + x
        totaly = totaly + y
    if direction == 1:
        totalx = totalx + x
        totaly = totaly - y
    if direction == 2:
        totalx = totalx - x
        totaly = totaly - y
    if direction == 3:
        totalx = totalx - x
        totaly = totaly + y



    print(totalx,totaly)



























