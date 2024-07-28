
# CA Duel Chances Mk2
# https://www.codeabbey.com/index/task_view/duel-chances

"""
A first then B, repeated until one is dead.
Only need percentages to the 2nd decimal place.


Apparently I need a huge refresher in probability



"""


def probabilities(aHit,bHit):
    aNoHit = (100-a)/100
    bNoHit = (100-b)/100
    aHit = aHit/100
    bHit = bHit/100
    rounds = 1
    aWin = 1
    bWin = 1
    aMiss = 1
    bMiss = 1
    noW = 1

    # Write Events as they happen

    ff = 0.5
    totalFF = 1
    fWin = 1
    fContinue = 1
    for i in range(0,10):


        print(fWin)



    print(aWin,bWin,noW)






times = int(input())

for i in range(times):
    a,b = map(int, input().split(' '))

    probabilities(a,b)













