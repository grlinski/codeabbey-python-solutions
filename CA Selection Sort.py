
# Selection Sort
# https://www.codeabbey.com/index/task_view/selection-sort


"""

6
31 41 59 26 53 58


This wants the index of the largest item.


"""

def selectionSort(q):

    maxi = max(q)
    swap = True
    leng = len(q)
    sortq = []
    ans = []
    while len(q)!=1:
        lastValue = q[-1]
        maxi = 0
        posMaxi = 0
        for i in range(0,len(q)-1):
            if q[i] > maxi:
                posMaxi = i
                maxi = q[i]
        if maxi > lastValue:
            q[posMaxi] = lastValue
            sortq.append(maxi)
            q=q[:-1]
            ans.append(posMaxi)
        else:
            sortq.append(lastValue)
            sortq.append(maxi)
            ans.append(len(q)-1)
            q = q[:-1]

    print(q)
    print(sortq)
    return(ans)







items = int(input())

q = list(map(int, input().strip().split(' ')))

ans = selectionSort(q)

for i in ans:
    print(i,end= ' ')
