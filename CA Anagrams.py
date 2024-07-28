
# http://www.codeabbey.com/index/task_view/anagrams
import itertools, sys, os

# This Creates a List of all the Words in AnagramsWords.txt
wordlist = []
openfile = open("AnagramWords.txt")
for i in openfile:
    if i != "":
        j = i[0:-1]
        wordlist.append(j)




def permutations(lst):
    n =len(lst)
    if n == 0:
        return []
    if n == 1:
        return [lst]
    l = []

    for i in range(n):
        m = lst[i]

        remLst = lst[:i] + lst[i + 1:]

        for p in permutations(remLst):
            l.append([m] + p)

    return l


# Create own permutation function
# Rearranges letters in however many different ways
# For each permutation checks wordlist if it appears
# then append that word to a new list
# Then later flatten the list to remove duplicates
# Since words with double of the same letter will return the same word






items = int(input())

full_list = []
for i in range(0,items):
    word = input()
    letters = []
    counter = 0
    for j in word:
        letters.append(j)
    full_list.append(permutations(letters))

answer = []

for i in full_list:
    permute_list = []
    counter = -1
    for j in i:
        worder = ""
        for k in j:
            worder = worder+k
        permute_list.append(worder)
    permute_list = set(permute_list)
    permute_list = list(permute_list)
    for q in permute_list:
        if q in wordlist:
            counter+=1
    answer.append(counter)



#print(permute_list)
for i in answer:
    print(i,end =" ")
"""

2
bat
cat

"""
"""

3
bat
coal
lots

"""
















