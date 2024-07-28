


# Girls and Pigs
# http://www.codeabbey.com/index/task_view/girls-and-pigs

"""

Completed
Annoyingly it never states there must be at least 1 girl and pig in the calculation
I corrected it for the girls but didn't bother with the pigs
May want to change that someday.



Notes

Minimum Girls
Minimum Amount of Girls that Must be Present in the Total
(legs%4)/2 = minigirls
This is because the pigs have 4 legs
Example if we have 6 legs, at least one must be a girl





"""






times = int(input())


def calculations(legs,b):

    # Minimum Amount of Girls that Must be Present in the Total
    # (legs%4)/2 == minigirls
    # This is because the pigs have 4 legs
    """
    Example if we have 6 legs, at least one must be a girl
    """
    minigirls = int((l % 4) // 2)
    if minigirls == 0:
        minigirls+=1
    ways = 0
    for i in range(minigirls,legs//2):
        girls = i

        remainingLegs = legs-(girls*2)
        remainingBreasts = b - (girls * 2)

        #print(girls,remainingLegs,remainingBreasts)
        if remainingLegs%4 == 0:
            pigs = remainingLegs//4
            if remainingBreasts%pigs == 0 and (remainingBreasts//pigs)%2 ==0:
                ways+=1
                print('Number',ways)
                print('Girls, Pigs Legs B')
                print(girls,pigs,l,b)
                print('Total Legs and Breasts Minus Girls')
                print(l-(girls*2),(b-(girls*2)))
                print('Total Breasts Per Pig')
                print((b-(girls*2))/pigs)

        else:
            pass

    print('Total Ways',ways)
    return ways



ans = []

for i in range(0,times):
    l,b = map(int, input().split(' '))

    x = calculations(l,b)
    ans.append(x)

for i in ans:
    print(i,end= ' ')

"""

Testcases

4
6 10
26 136
106 336
200 500




"""






