
# Lucky Tickets
# https://www.codeabbey.com/index/task_view/lucky-tickets

"""


Ending Notes
There is an acutal mathematical way to solve this.
Obviously I just did something more akin to an optimized brute force method
Not that that's awful




Author's notes on this problem
When I wrote this problem, I have a relatively simple idea in mind:

Iterate through all numbers from 0 to 10^(N/2)-1, i.e for N=8 for example from 0000 to 9999.

Count how many times each sum of such "half-number" is encountered - it would be a kind of an array with indices from 0 to (B-1)*N/2.

The result is just the sum of squares of the values from this array.

However it looks that far more efficient DP algorithms exist, so I'll try to create an advanced version of the task...















May Actually Work
Just needs some amount of time
Could optimize


n = Max Amount of Digits
b = Numerical System use, ie binary, ternary, decimal, hexidecimal


# NOTE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
Create an Ending System that Actually works.






ALright
So I realize one potentially easy way to Optimize
First let's say n is 10,I at most only need to do up to 5 digits of numbers

So for my explanation let's just do
n = 6, b = 10

So 000000 to 999999
I only need work on numbers up to 999
So starting at 000
Only one way to make 0
Which is 000
3 ways to make 1
100,010 and 001

I could store the value, 1 and all combos that make this number.
In a dict.
They calculate how many ways they match up.

How to make 2
011
101
110
002
020
200
6 Way.
May actually just fit a pattern.



!!!!!!!!!!!!!!!!!!!!!
Will need to add in Correction Factor for all odd numbers
Example
7 10
9990999
9991999
My program ignore the middle number
So it wouldn't count these as seperate.







"""

import time

def addDictValues(dict,odd,b):
    total = 0
    if odd == False:
        for i in dict:
            x = dict[i]
            total+=(x*x)
        return total
    else:
        for i in dict:
            x = dict[i]
            total+=((x*x)*b)
        return total



def convertNumBaseAndAdd(n,b,leng,dict):
    if n == 0:
        dict[0] = 1
        return dict,1
    nums = []

    # For Values higher than 10
    counterPart = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    dcp = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

    while n:
        n, r = divmod(n, b)
        nums.append(int(r))


    while len(nums)<leng:
        nums.append(0)
    nums.reverse()
    total = sum(nums)
    #print(total)

    string1 = ''
    for i in nums:
        string1+=str(i)
    #print(string1)

    if total in dict:
        dict[total]+=1
    else:
        dict[total]=1




    return dict,len(nums)



def flowControl(n,b):
    counter = 0
    x = 0
    number = 0
    if n%2 == 0:
        odd = False
    else:
        odd = True


    n = n//2
    dict = {}


    while x <n+1:


        dict,x = convertNumBaseAndAdd(number,b,n,dict)
        number+=1
    if 1 in dict:
        dict[1]-=1


    ans = addDictValues(dict,odd,b)
    return ans


ans = []

cases = int(input())

start = time.time()

for i in range(cases):
    n,b = map(int, input().split(' '))

    x = flowControl(n,b)
    print(n,b)
    print((time.time()-start)/60)
    ans.append(x)


for i in ans:
    print(i,end= ' ')



"""







12
7 14
12 2
10 8
6 6
3 5
2 2
7 7
6 5
23 2
12 8
5 4
12 7


Exp
4150888 924 58199208 4332 25 2 65317 1751 1410864 3409213016 176 786588243


Mine
4150888 924 465593664 25992 25 4 65317 8755 1410864 3409213016 44 786588243 






"""



