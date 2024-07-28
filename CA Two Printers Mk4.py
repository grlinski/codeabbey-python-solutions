



# Two Printers
# https://www.codeabbey.com/index/task_view/two-printers


"""
Speed it up
Maybe do a factor system.
Go by a factor of 100
Slow down if the last one passes it.

If there are barely any pages just skip to the steps

List Scenarios
A and B <<<<< Pages add factor system.
A and B > Pages, skip to steps
A and B < Pages, skip to steps.


Works Finally!!!!!!!!!!!!!!!!!!!!!!!!


"""




cases = int(input())

import math,time
# 90 100 10

#cases = 1
ans = []
for i in range(cases):
    a,b,pages = map(int, input().split(' '))

    start = time.time()
    # Steps
    mini = min(a, b)
    maxi = max(a, b)
    totalMini = mini
    totalMaxi = maxi
    step1 = mini
    totalTime = 0
    totalPages = 0

    #print(a*b)



    if a*b*1000< pages:
        step2 = a*b*1000
        pagesPerStep2 = (a+b)*1000

        while (totalPages +pagesPerStep2) < pages:
            totalPages+=pagesPerStep2
            totalTime+=step2



    while totalPages < pages:
        if totalMini - step1 <= totalMaxi - step1:
            totalMini -= step1
            totalMaxi -= step1
            totalTime += step1
        elif totalMaxi - step1 < totalMini - step1:
            totalMini -= step1
            totalMaxi -= step1
            totalTime += step1
        if totalMaxi == 0 and totalMini == 0:
            totalPages += 1
        if totalMaxi == 0:
            totalMaxi = maxi
        if totalMini == 0:
            totalMini = mini
        step1 = min(totalMini, totalMaxi)
        totalPages += 1

    end = time.time()
    print(end-start)
    print(i+1,totalTime)
   # print(totalPages,pages,totalTime)
    ans.append(totalTime)






#print('ans')
for i in ans:
    print(i,end=' ')




"""

1
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

1
851 1082 826871
Ans
393879378 
Mine
393879393


"""













"""
Datasets 


1
1 1 5


1
3 5 4

1
13 1 71723420





1
851 1082 826871
Ans
393879378 
Mine
393879393


1
300 921 12311





393879378 
197041391 







16
851 1082 826871
113184 72180 8361
14 11 69811974
83674370 42014457 9
380375 776659 952
1 2 477860341
108590 142925 4938
2697 506 369768
1146668 8585003 71
76714 120622 2777
51 372 2082546
16996604 47314780 9
1 1 515085827
2 1 447873091
1 4 146417291
58355 58304 12226



























"""





