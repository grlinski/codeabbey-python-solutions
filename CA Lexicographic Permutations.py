

# CA Lexographic Permutations
# https://www.codeabbey.com/index/task_view/lexicographic-permutations

"""
Completed

Ending Notes
I really should learn how to create all permutations and combinations without itertools
And look up Lexicographic Permutations Functions
Really need a way to increase efficiency of this program.
Takes at least 10 minutes to run.






"""




"""
Total permutations
12! =
479001600

Should probably find out how to do lexicographic permutations

"""


import time
from itertools import permutations

def printSequence(letters):
    ans = ''

    for i in letters:
        ans+=str(i)
    return ans



listOfNums = []
#cases = 0
cases = int(input())
for i in range(cases):
    x = int(input())
    listOfNums.append(x)





letters = ['A','B','C','D','E','F','G','H','I','J','K','L']
#letters = ['A','B','C','D']

x = permutations(letters,12)
totalPerms = 479001600

counter = 0
printAt = 1
dict = {}

print('Done Part 1')

start = time.time()
endGame = False
for i in x:


    if counter in listOfNums:
        dict[counter] = i
    now = time.time()
    if counter == printAt:
        print(now-start,printAt)
        if endGame == False:
            printAt*=10
            if printAt == 100000000:
                endGame = True
        else:
            printAt+=100000000


    counter += 1




ans = []
for i in listOfNums:
    ans.append(printSequence(dict[i]))

for i in ans:
    print(i,end=' ')


