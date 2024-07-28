
#  Sweet Harvest
# https://www.codeabbey.com/index/task_view/sweet-harvest
"""

Idea
So for this test case
11 5 3 17 2 13 19 7

We start at 11 and 5 doesn't factor in to this.
We can jump to either 3 or 17
And so on.
But let's just look up to 13
So on our second jump we can reach 13 from either 3 or 17.
So to get to that spot we want the largest value.
Getting to 3 there are two ways
11 3 13
Or
11 17 13
Obviously the second one is better.
So we don't immediately jump to 13 but rather jump to 17 and reassess.
So check the two numbers we can jump to and where they meet up
So
from pos0, to pos2 and po3 meeting up at pos5

Maybe not
One way though is to always stop at a number with a lower one in front of it if possible.



Other Idea
So this requires starts by jumping to Pos2  and Pos3, then trying from there.
So for the test case
11 5 3 17 2 13 19 7
Let's try starting at pos2 which is the 3
3, then we can jump to 2 or 13
13 Makes sense if the the nums beside it are less than 13.
So thats one optimization.
Lets try jumping to 2.
This makes sense if 13


Do on paper.
Basically I only care about 5 or 6 numbers at a time.
Making the best jump in that small range.
As most jumps can link up easily.



Formula
Testcase
9 7 12 7 16 3 7 17 14 13 4 6 11 6 3 3 5 4 11 3 15 12 14 2 15 19 11 12

1 2 3 4 5 6

Let's do paths as x and y
So start at 9
x goes 9 to 12
y goes 9 to 7

Paths


p1 = 1+3+5
p2 = 1+4+6
p3 = 1+3+6



Then x goes to both 16 and 3
y goes to 3
Choose the highest of the paths to 3.
Restart at 16 and 3

9 7 12 7 16 3



Next Part



16 3 7 17 14 13 4 6 11 6 3 3 5 4 11 3 15 12 14 2 15 19 11 12

Paths
p0 to p3
p1 to p3

p0 to p2 to p4
p1 to p4


Testcase
11 4 10 8 5 18 5 17 16 10 11 9 7 17 8 4 8 5 4 15 5 6 15 4 6 9 17 16 14

Ans = 168


"""


# MAIN FUNCTION
def pathFinder(islands):

    ender = len(islands)
    sections = (ender-6)//5
    x1 = islands[0]
    x2 = islands[0]
    y = islands[1]

    # Intial Step Requires 6 Positions
    p1 = islands[0] + islands[2] + islands[4]
    p2 = islands[0] + islands[3] + islands[5]
    p3 = islands[0] + islands[2] + islands[5]
    # Intial Paths
    """
    Requires 6 Positions
    path1 = 0+2+4
    path2 = 0+3+5
    path3 = 0+2+5
    Pick max of path2 and 3
    
    path1 = path1
    path2 = max(path2,path3)
    
    Next Paths
    path1 = path1 + 3
    path2 = path2 + 3
    
    path3 = path1 + 4
    path4 = path2 + 2 + 4
    
    
    p0 to p3
    p1 to p3
    
    p0 to p2 to p4
    p1 to p4
    
    """

    # Next Paths

    islands = islands[6:]
    print(p1,p2,p3)

    path1 = p1
    path2 = max(p2,p3)
    # Path 2 is the further path
    # Path 1 is the closer path
    print(path1,path2)
    while len(islands) >=4:

        pathN1 = path1 + islands[0] + islands[3]
        pathN2 = path1 + islands[1] + islands[3]
        pathN3 = path2 + islands[1] + islands[3]

        pathN4 = path2 + islands[2]
        pathN5 = path1 + islands[0] + islands[2]

        print('Start Path1,Path2')
        print(path1, path2, islands[:4])
        path1 = max(pathN4,pathN5)
        path2 = max(pathN1,pathN2,pathN3)
        islands = islands[4:]

        print('End Path1,Path2')
        print(path1, path2, islands[:4])
    ans = 0


    print('After Loop')
    print(islands,path1,path2)

    if len(islands) == 0:
        ans = max(path1,path2)
    elif len(islands) == 1:
        ans = max((path1+islands[0]),path2)
    elif len(islands) == 2:
        item1 = path1+islands[0]
        item2 = path1 + islands[1]
        item3 = path2 + islands[1]
        ans = max(item1,item2,item3)
    elif len(islands) == 3:
        item1 = path1+islands[0]+islands[2]
        item2 = path1 + islands[1]

        item3 = path2 + islands[1]
        item4 = path2 + islands[2]
        ans = max(item1,item2,item3,item4)

    elif len(islands) == 4:
        item1 = path1 + islands[0] + islands[2]
        item2 = path1 + islands[0] + islands[3]
        item3 = path1 + islands[1] + islands[3]

        item4 = path2 + islands[1]+ islands[3]
        item5 = path2 + islands[2]

        ans = max(item1, item2, item3, item4,item5)

    print(ans)
    return ans




ans = []
leng = []
cases = int(input())
#cases = 1
for i in range(0,cases):

    q = list(map(int, input().strip().split(' ')))

    ans.append(pathFinder(q))
    leng.append(len(q))

for i in ans:
    print(i,end=' ')
print()

for i in leng:
    print(i,end= ' ')


"""





3
11 4 10 8 5 18 5 17 16 10 11 9 7 17 8 4 8 5 4 15 5 6 15 4 6 9 17 16 14
9 18 7 14 14 13 17 12 12 11 17 9 16 17 11 2 6 15 8 17 8 3 8 4 5 19 4 5 9 10 4 17 8 10 11
3 9 13 14 19 10 3 16 8 12 16 13 7 4 10 14 6 16 17 10 16



Ans
168 205 127





"""