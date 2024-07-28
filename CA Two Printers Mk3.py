


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
    #printedPerMini = (mini/maxi)+1

    totalMini = mini
    totalMaxi = maxi
    totalTime = 0
    totalPages = 0
    step1 = mini

    # Factor 100
    totalMini100 = mini*100
    totalMaxi100 = maxi*100
    step100 = mini*100

    counter = 0
    print(totalMini,totalMaxi,step1,totalTime)



    while counter < pages:
        if totalMini-step1 <= totalMaxi-step1:
            totalMini-=step1
            totalMaxi-=step1
            totalTime +=step1
        elif totalMaxi-step1 < totalMini-step1:
            totalMini -= step1
            totalMaxi -= step1
            totalTime +=step1
        if totalMaxi == 0 and totalMini == 0:
            counter+=1
        if totalMaxi == 0:
            totalMaxi = maxi
        if totalMini == 0:
            totalMini = mini
        step1 = min(totalMini, totalMaxi)
        counter+=1



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








"""


1
A B Pages
3 5 4

3*5 = 15 seconds
In 15 seconds printer A prints 5 pages
B prints 3
So 8 pages in 15
Next Example
1
851 1082 826871
A*B = 920782
A+B = 1933 pages per 920782 seconds


"""









