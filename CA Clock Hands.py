

# Clock Hands
# https://www.codeabbey.com/index/task_view/clock-hands

# Completed



import math
# Center is 10,10
# Minute Hand is 9 long
# Hour is 6 long


# Need to Correct for minute hand
# Example if minutes = 30, and hour = 9
# then the hour hand needs to be halfway between 9 and 10
# Basically hour+(minutes/60*30)
def coordinatesHour(hour,minutes):
    correction = (minutes / 60) * 30
    arc = ((30 * hour) % 360) + correction

    hyp = 6


    # ++
    if arc >= 0 and arc <= 90:
        arc = math.radians(arc)
        a = math.sin(arc)
        b = math.cos(arc)
        x = 10+(a*hyp)
        y = 10+(b*hyp)

    elif arc >90 and arc <= 180:
        arc = arc%90


        arc = math.radians(arc)

        a = math.sin(arc)
        b = math.cos(arc)
        y = 10 - (a * hyp)
        x = 10 + (b * hyp)



    elif arc > 180 and arc <= 270:
        arc = arc%90
        arc = math.radians(arc)
        a = math.sin(arc)
        b = math.cos(arc)
        x = 10 - (a * hyp)
        y = 10 - (b * hyp)

    else:
        arc = arc%90
        arc = math.radians(arc)
        a = math.sin(arc)
        b = math.cos(arc)
        y = 10 + (a * hyp)
        x = 10 - (b * hyp)



    return(x,y)

#####################################Minutes
##################################################
def coordinatesMinute(minute):
    arc = ((minute / 60) * 360)
    hyp = 9
    # ++ Looks Good
    if arc >= 0 and arc <= 90:
        arc = math.radians(arc)
        a = math.sin(arc)
        b = math.cos(arc)

        x = 10 + (a * hyp)
        y = 10 + (b * hyp)



    elif arc > 90 and arc <= 180:
        arc = arc % 90
        arc = math.radians(arc)

        a = math.sin(arc)
        b = math.cos(arc)
        y = 10 - (a * hyp)
        x = 10 + (b * hyp)



    elif arc > 180 and arc <= 270:
        arc = arc % 90
        arc = math.radians(arc)
        a = math.sin(arc)
        b = math.cos(arc)
        x = 10 - (a * hyp)
        y = 10 - (b * hyp)


    else:
        arc = arc % 90
        arc = math.radians(arc)
        a = math.sin(arc)
        b = math.cos(arc)
        y = 10 + (a * hyp)
        x = 10 - (b * hyp)
    return (x, y)



pi = math.pi

#hour = 12
#minute = 5
cases = int(input())

list1 = input().split()


for i in list1:
    a,b = i.split(':')
    hour = a
    minute = b
    hourx,houry = (coordinatesHour(int(hour),int(minute)))
    minx,miny = (coordinatesMinute(int(minute)))
    print(hourx,houry,minx,miny,end= ' ')




