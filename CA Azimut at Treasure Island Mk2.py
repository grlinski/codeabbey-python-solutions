
# Azimuth at Treasure Island
# http://www.codeabbey.com/index/task_view/azimuth-at-treasure-island


import math, re


hold = input()
number = re.compile(r'\d+')
x,y = 0,0


while True:

    # This Inital Portion Takes in Input and Ends Properly
    hold = input()
    try:
        feet, azis = (number.findall(hold))
    except:
        break
    if hold == "":
        break

    ft = int(feet)
    az = int(azis)


    # Math in Python Annoyingly works bet with rads, which I never really learned
    # So unfortunately it's best to work in rads
    rads = math.radians(az)

    changex = math.sin(rads)*ft
    changey = math.cos(rads) * ft

    x = x+changex
    y = y+changey

    # Sin = X
    # Cos = Y
    # Convert ft and az into usable coordinates


x = round(x)
y = round(y)
print(x,y)




"""

Stand at the pole with the plaque START
go 140 feet by azimuth 332
go 460 feet by azimuth 78
Dig here!



Below Should end at x=0, y=50

Stand at the pole with the plaque START
go 100 feet by azimuth 90
go 100 feet by azimuth 270
go 100 feet by azimuth 0
go 50 feet by azimuth 360
Dig here!


Stand at the pole with the plaque START
go 100 feet by azimuth 90
go 100 feet by azimuth 45
go 100 feet by azimuth 225
go 100 feet by azimuth 270
go 100 feet by azimuth 0
go 50 feet by azimuth 360
Dig here!


Easy

Stand at the pole with the plaque START
go 100 feet by azimuth 45
go 100 feet by azimuth 225
Dig here!




"""


