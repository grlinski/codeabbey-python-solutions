


#  Sweet Harvest
# https://www.codeabbey.com/index/task_view/sweet-harvest
"""


New Strategy
Formulate an entirely new Algorithm
Either make it smaller or larger.
Maybe just do single jumps of 2 and 3.


Newest New Idea
Break down into segments and optimize those segments
Only question right now is how long the segements should be.
Maybe 3 or 4 Jumps max
Try to positions 7 and 8
0 1 2 3 4 5 6 7 8 9 10
Then I have to optimize 4 routes.
From 7 to 14, 15
And 8 to 14,15.





0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35



"""
"""


9 7 12 7 16 3 7 17 14 13 4 6 11 6 3 3 5 4 11 3 15 12 14 2 15 19 11 12


"""

from itertools import permutations


def sixStep(i):

    p1 = i[2] + i[4] + i[6]
    p2 = i[3] + i[6]


    return max(p1, p2)


def sevenStep(i):
    # seven = [[2, 2, 3], [3, 2, 2], [2, 3, 2]]
    p1 = i[2]+i[4]+i[7]
    p2 = i[3] + i[5] + i[7]
    p3 = i[2] + i[5] + i[7]

    return max(p1,p2,p3)


def eightStep(i):
    eight = [[3, 2, 3], [2, 3, 3], [2, 2, 2, 2], [3, 3, 2]]
    p1 = i[3] + i[5] + i[8]
    p2 = i[2] + i[5] + i[8]
    p3 = i[2] + i[4] + i[6] + i[8]
    p4 = i[3] + i[6] + i[8]

    return max(p1,p2,p3,p4)




# MAIN FUNCTION
def pathFinder(islands):

    """
    Ways to make 6, 7 and 8 from, 2s and 3s
    Need to go from position 0 to 7 and 0 to 8 Initially.
    Then 7 to 14 and 15 and 8 to 14 and 15

    For this I'm going to assume we are including the two previous numbers
    Ie path1 and path2 starts in the segment.

    """
    six = [[2, 2, 2],[3, 3]]
    seven = [[2, 2, 3], [3, 2, 2], [2, 3, 2]]
    eight = [[3, 2, 3], [2, 3, 3], [2, 2, 2, 2], [3, 3, 2]]

    #Inital Setup
    path1 = islands[0]
    path2 = islands[0]
    segment = islands[:9]
    islands = islands[7:]

    print(segment)
    print(islands)
    path1 += (sevenStep(segment))
    path2 += (eightStep(segment))

    print(path1,path2)

    while len(islands) >9:
        segmentLagger = islands[:10]
        segmentLeader = islands[1:10]
        islands = islands[8:]

        # Lagger to Leader
        p1 = eightStep(segmentLagger)
        # Leader to Leader
        p2 = sevenStep(segmentLeader)

        # Leader to Lagger
        p3 = sixStep(segmentLeader)
        # Lagger to Lagger
        p4 = sevenStep(segmentLagger)


        if p1>p2:
            path2 += p1
        else:
            path2 += p2

        if p3 > p4:
            path1 += p3
        else:
            path1 += p4

        print(path1,path2)

    print(path1,path2)
    print(islands)






ans = []

#cases = int(input())
cases = 1
for i in range(0 ,cases):

    q = list(map(int, input().strip().split(' ')))
    ans.append(pathFinder(q))


for i in ans:
    print(i ,end=' ')


"""





3
11 4 10 8 5 18 5 17 16 10 11 9 7 17 8 4 8 5 4 15 5 6 15 4 6 9 17 16 14
9 18 7 14 14 13 17 12 12 11 17 9 16 17 11 2 6 15 8 17 8 3 8 4 5 19 4 5 9 10 4 17 8 10 11
3 9 13 14 19 10 3 16 8 12 16 13 7 4 10 14 6 16 17 10 16



Ans
168 205 127





"""
































