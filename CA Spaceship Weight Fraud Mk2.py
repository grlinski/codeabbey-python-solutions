




# CA Spaceship Weight Fraud
# https://www.codeabbey.com/index/task_view/spaceship-weight-fraud
"""

Completed
End Notes
Keep things simple, I did something a bit dumb when I bothered with an index
I already have an index if I keep the list in the same order.








"""


def listToString(x):
    string1 = ''
    counterPart = { 10:'A', 11:'B', 12:'C',13:'D', 14:'E', 15:'F'}

    for i in x:
        if i in counterPart:
            y = counterPart[i]
        else:
            y = str(i)
        string1+=(y)

    return string1



# FIND LARGEST
def findLargest(x,list1):
    # So for this I want to swap a smaller number near the start with the first instance of a larger number
    # As long as this larger number is after the smaller number.
    #

    # First find a larger number than the first index
    # Check cases where I need to move to the second index and where there's nothing larger.


    ender = False
    for i in range(0,len(list1)):
        if ender == True:
            break
        maxi = 0
        for k in range(len(list1)-1,i,-1):
            maxi = max(maxi,int(list1[k]))
        #print(maxi)
        for j in range(len(list1)-1,i,-1):
            back = list1[j]
            front = list1[i]
            if back > front and back == maxi:
                holder1 = list1[j]
                holder2 = list1[i]

                list1[j] = holder2
                list1[i] = holder1

                ender = True

    return list1



# FIND LARGEST
def findSmallest(x,list1):
    # Opposite of Largest.
    # First largest number swapped with last smallest number
    #print(list1)
    ender = False
    for i in range(0,len(list1)):
        if ender == True:
            break
        mini = 20
        for k in range(len(list1)-1,i,-1):
            if i == 0 and list1[k] == 0:
                pass
            else:
                mini = min(mini,int(list1[k]))

        for j in range(len(list1)-1,i,-1):
            back = list1[j]
            front = list1[i]
            zeroer = True

            if back < front and back == mini and zeroer:
                holder1 = list1[j]
                holder2 = list1[i]

                list1[j] = holder2
                list1[i] = holder1

                ender = True

    return list1


# INDEXER
"""
To Make Life Somewhat Easier this does multiple things
Separates a string into multiple parts with their index
Also the Full list contains everything, with letters converted to their numerical counterpart


"""
def indexer(x):
    full = []
    num = '0123456789'
    counterPart = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
    for i in range(0,len(x)):
        y = x[i]
        if y in num:
            a = int(y)
            full.append(a)
        else:
            y = counterPart[y]
            a = y
            full.append(a)
    return full



def flowControl(x):
    ans = []
    list1 = indexer(x)
    list2 = indexer(x)

    maxi = findLargest(x,list1)
    mini = findSmallest(x,list2)

    a1 = listToString(mini)
    a2 = listToString(maxi)


    return a1,a2

ans = []
cases = int(input())
#cases = 1
for i in range(cases):
    x = input()
    temp1,temp2 = flowControl(x)
    ans.append(temp1)
    ans.append(temp2)

for i in ans:
    print(i,end= ' ')














