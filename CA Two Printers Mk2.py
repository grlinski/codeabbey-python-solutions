
# Two Printers
# https://www.codeabbey.com/index/task_view/two-printers


"""
Speed it up
Maybe do a factor system.
Go by a factor of 100
Slow down if the last one passes it.






"""




cases = int(input())

import math
# 90 100 10

#cases = 1
ans = []
for i in range(cases):
    a,b,pages = map(int, input().split(' '))

    # Steps
    mini = min(a,b)
    maxi = max(a,b)

    # Pages Printed per Mini
    printedPerMini = (mini/maxi)+1

    totalMini = 0
    totalMaxi = 0
    totalTime = 0
    totalPages = 0
    print(printedPerMini)

    while totalPages < pages:

        if totalPages+(100*printedPerMini) > pages:
            totalPages+=printedPerMini
            totalTime+=mini
        else:
            totalPages += (printedPerMini*100)
            totalTime += (mini*100)


        #print(counter,totalTime)
    ans.append(totalTime)



print('ans')
for i in ans:
    print(i,end=' ')









"""

1631 1164 462405


Need to do this in steps.
I need to determine the difference between the two printers and work up in those steps.
Example
90 100 10

So the first page is printed at 90 seconds
At this stage the other page is 90% complete.
Then after 10 seconds the other page is complete.
The 3rd page is now 1/9th complete.

So first step is 90
Next is 10,
Then 80
Then 20
Then 70
Then 30

One step is increasing the other is decreasing
Eventually they overlap/reset.

NOTE!
Need to account for that fact that the smaller value may be multiple times smaller than the larger
Example

1 and 100
Meaning the step between is always 1





"""










