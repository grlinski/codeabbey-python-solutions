


# Dungeon's and Dragons Dice
# https://www.codeabbey.com/index/task_view/dungeons-and-dragons-dice
"""
Sides = 2,4,6,8,10,12
Dice 1 to 5

"""
"""
Algorithm
Simulate all combinations
Maybe 1000 rolls
Compare the chisquare value to my own
Choose best fit.







"""

import math,random


def chiSquare(simRolls,realRolls):
    diff = abs(len(simRolls)-len(realRolls))
    if len(simRolls) > len(realRolls):
        for i in range(diff):
            realRolls.append(0)
    elif len(realRolls) > len(simRolls):
        for i in range(diff):
            simRolls.append(0)

    totalChi =0

    for i in range(0,len(realRolls)):
        real = realRolls[i]
        sim = simRolls[i]
        diff = abs((real**2)-(sim**2))
        totalChi+=diff
    return totalChi




def probabilitiesConverter(x):
    count = 0
    for i in x:
        if x !=0:
            count+=i
    for i in range(0,len(x)):
        if x[i] !=0:
            x[i] = x[i]/count

    return x






def simluations(realRolls):
    # Sides = 2 to 12
    # Dice 1 to 5
    lowChi = 100000000
    ans = ''

    realRolls = probabilitiesConverter(realRolls)


    for sides in range(2,13,2):
        for dice in range(1,6):
            list1 = [0]*((dice*sides)+1)
            for times in range(10000):
                r = 0
                for q in range(dice):
                    r += random.randint(1,sides)
                list1[r]+=1
            list1 = probabilitiesConverter(list1)

            chi = chiSquare(list1,realRolls)
            print(chi,dice,sides)
            print(list1)
            print(realRolls)
            if chi < lowChi:
                #print(chi,sides,dice)
                ans = str(dice)+'d'+str(sides)
                print(ans,chi)
                lowChi = chi
    return ans








ans = []
times = 3
for t in range(times):
    rolls = list(map(int, input().strip().split(' ')))
    rolls = rolls[:-1]
    maxi = max(rolls)
    counts = [0]*(maxi+1)

    print('CASE',t+1)

    for i in rolls:
        counts[i]+=1
    ans.append((simluations(counts)))

for i in ans:
    print(i,end=' ')







"""
Exp
3d2 4d8 2d4

Mine
3d2 3d12 1d6 


5 4 4 5 6 5 5 5 4 5 5 6 4 5 5 5 5 6 4 6 4 5 5 5 4 5 4 4 4 3 6 5 6 3 4 5 5 5 5 4 6 4 4 5 5 4 5 5 5 3 3 5 5 5 3 4 4 5 5 5 5 6 5 5 4 6 4 3 5 4 4 5 5 6 5 6 6 4 6 3 4 4 4 6 6 3 4 4 3 6 4 4 3 4 5 4 4 4 5 5 0
24 20 19 21 24 19 23 17 23 13 24 21 15 12 25 19 8 12 25 19 25 21 13 12 23 10 10 11 11 25 20 23 27 25 28 19 14 19 14 9 20 21 18 26 22 25 21 12 20 16 24 24 22 14 15 10 12 10 11 19 17 20 18 15 13 13 27 20 17 18 14 23 20 13 21 10 18 15 20 15 16 22 21 17 18 18 19 13 16 23 21 14 18 14 13 22 16 10 6 11 0
3 4 4 7 6 3 5 6 4 5 3 7 3 5 5 4 6 7 3 5 2 6 5 8 5 5 4 5 7 7 4 5 5 4 3 4 3 4 5 6 2 2 4 4 8 4 3 3 2 2 6 6 7 6 7 6 8 6 2 8 2 3 6 5 6 2 3 5 4 6 5 4 2 5 5 2 6 5 3 6 5 5 5 7 6 5 4 8 4 3 4 5 6 3 4 3 6 8 6 5 0


"""
























