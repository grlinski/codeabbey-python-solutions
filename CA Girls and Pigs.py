
# http://www.codeabbey.com/index/task_view/girls-and-pigs

times = int(input())


for i in range(0,times):
    l,b = map(int, input().split(' '))

    ways = 0
    pigs = 0
    girls = 0
    counter = 0

    # Minimum Amount of Girls that Must be Present in the Total
    # (legs%4)/2 == minigirls
    minigirls = (l%4)/2


    # Minimum Breasts Based on the minigirls amount
    breasts = b - (minigirls*2)

    b = int(breasts)
    l = int(l-(minigirls*2))
    #print(l,b)

    # pairs of Pig Breasts/Nipples
    # Actual Staring Values
    # b,l, pairs = 1, girls = 0
    # increase pairs and girls

    pairs = 1
    girls = 0

    maxpairs = int(b/2)
    maxgirls = int(l/2)

    # Contingency for 0 Pigs
    if l%b == 0:
        ways+=1

    while True:

        # Amount Of Each
        pigs = b//(pairs*2)


        # Then Does the Amount of Legs and Breasts Equal Correctly?
        breasts = (pigs*pairs*2)+(girls*2)
        legs = (pigs*4)+(girls*2)

        if breasts == b and legs == l:
            ways+=1

        pairs+=1
        if pairs > maxpairs:
            pairs = 1
            girls+=1
        if girls > maxgirls:
            break

    print(ways)










"""
Pig Any Even Number of Breasts and 4 Legs
Girls 2 Breasts 2 Legs



1
26 136



"""






















