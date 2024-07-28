

# Insertion Sort
# https://www.codeabbey.com/index/task_view/insertion-sort
"""
My problem with this was I was moving items up the list
I need to be moving them down.
Move the smallest values downwards to their correct positions.

In the example:
4
3 1 2 5
Ans
1 1 0

The 1 in the ans is the 1 from the array moving down past 3
Then 2 moving down past 3
And 5 doesn't move.




"""


def insertionSort(q):
    print('Start')
    i = 0
    swaps = True
    ans = []
    while swaps == True:
        if i == (len(q)-1):
            cur = q[i]
            next = cur+1
        else:
            cur = q[i]
            next = q[i+1]
        print(cur,next,i)
        if cur > next or i == len(q)-1:
            passes=1
            j = i
            while True:
                if j == 0:
                    break
                cur = q[j]
                prev = q[j-1]
                if prev > cur:
                    holder = q[j]
                    q[j] = prev
                    q[j-1] = cur
                    j-=1
                    passes+=1
                else:
                    break
            print(q)
            ans.append(passes)
        i+=1
        if i==len(q):
            break
    return ans














items = int(input())

q = list(map(int, input().strip().split(' ')))


ans = insertionSort(q)


print(' '.join(map(str, ans)))









