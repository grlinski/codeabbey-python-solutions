
# Enumerating Combinations
# https://www.codeabbey.com/index/task_view/enumerating-combinations

from itertools import combinations
import time

def compressor(segment):
    string1 = ''
    for i in segment:
        string1+=str(i)

    print(string1,end = ' ')




items = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
         'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']

start = time.time()
#x = combinations(items,16)


cases = int(input())

for i in range(cases):
    leng, amt,nth = map(int, input().split(' '))
    counter = 0
    tempitems = items[:leng]
    combos = combinations(tempitems,amt)
    for j in combos:
        if counter == nth:
            compressor(j)
            break
        counter+=1











