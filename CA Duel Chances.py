
# http://www.codeabbey.com/index/task_view/duel-chances
# Duel Chances

import datetime, math
ab = []

times = int(input())
answers = []

while times > 0:
    awin = 0
    bwin = 0


    x,y = input().split()
    a = int(x)/100
    b = int(y)/100
    missa = 1-a
    missb = 1-b

    total = 0

    awin = a
    bwin = missa*b

    step = missa*missb
    aturn = True

    for i in range(1,10):

        print('A ',awin)
        print('B ',bwin)
        print('M ',step)
        print('T ', awin+bwin+step)
        step = step * step

        awin=awin+(step*a)
        bwin=bwin+(step*b)



















    answers.append(awin)






    times-=1

print(answers)
# A is always first







"""
1
30 50


"""














