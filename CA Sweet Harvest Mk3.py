
#  Sweet Harvest
# https://www.codeabbey.com/index/task_view/sweet-harvest
"""


New Strategy
Formulate an entirely new Algorithm
Either make it smaller or larger.
Maybe just do single jumps of 2 and 3.

Test Case
0 1 2 3 4 5 6 7 8 9

New Idea
Go from 0 to 2 and 3 to start




0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35







"""


# MAIN FUNCTION
def pathFinder(islands):
    ans =0

    jumps1 = []
    jumps2 = []
    jumps1.append(islands[0])
    jumps2.append(islands[0])
    #Starter
    path1 = islands[0]+islands[2]
    path2 = islands[0]+islands[3]
    # 0 1 2 3 4 5 6 7 8 9
    islands = islands[4:]
    print(islands)
    jumps1.append(islands[2])
    jumps2.append(islands[3])
    # This works in segments of 4
    while len(islands) >3:
        # Path1 Candidates
        i0 = islands[0]
        i1 = islands[1]
        i2 = islands[2]
        i3 = islands[3]

        pN1 = path1 + islands[0]+ islands[2]
        pN2 = path2 + islands[2]

        # Path 2 Candidates
        pN3 = path1 + islands[0]+ islands[3]
        pN4 = path1 + islands[1]+ islands[3]
        pN5 = path2 + islands[1]+ islands[3]

        if pN1 > pN2:
            jumps1.append(i0)
            jumps1.append(i2)
        else:
            jumps1.append(i2)

        if pN3 >= pN4 and pN3 >= pN5:
            jumps2.append(i0)
            jumps2.append(i3)
        elif pN4 >= pN5:
            jumps2.append(i1)
            jumps2.append(i3)
        else:
            jumps2.append(i1)
            jumps2.append(i3)

        path1 = max(pN1,pN2)
        path2 = max(pN3,pN4,pN5)

        islands = islands[4:]
        print(islands)


    if len(islands)==0:
        ans = max(path1,path2)
    elif len(islands)==1:
        item1 = path1+islands[0]
        ans = max(item1,path2)
    elif len(islands)==2:
        item1 = path1+islands[0]
        item2 = path2+islands[1]
        item3 = path1+islands[1]
        ans = max(item1,item2,item3)
    elif len(islands)==3:
        item1 = path1+islands[0]+islands[2]
        item2 = path1+islands[1]
        item3 = path2+islands[1]
        item4 = path2 + islands[2]
        ans = max(item1,item2,item3,item4)
    elif len(islands)==4:
        item1 = path1 + islands[0] + islands[3]
        item2 = path1 + islands[0] + islands[2]
        item3 = path1 + islands[1] + islands[3]

        item4 = path2 + islands[1] + islands[3]
        item5 = path2 + islands[2]

        ans = max(item1, item2, item3, item4,item5)

    print('Jumps1')
    print(jumps1)
    print('Jumps2')
    print(jumps2)
    return ans

ans = []
leng = []
cases = int(input())
#cases = 1
for i in range(0 ,cases):

    q = list(map(int, input().strip().split(' ')))

    ans.append(pathFinder(q))
    leng.append(len(q))

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



















