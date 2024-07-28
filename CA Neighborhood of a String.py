

# Neighbourhood of a String
# https://www.codeabbey.com/index/task_view/neighborhood-of-a-string
"""

Completed
End Notes

Never knew about combinations_with_replacement
Add to Python Wiki
Otherwise my head is too messed up to think over things too much.
Bad sleep/possibly sick/drank last night
Some combination of the 3.





"""




from itertools import combinations_with_replacement
from itertools import permutations

def copyList(list1):
    list2 = []
    for i in range(0,len(list1)):
        x = list1[i]
        list2.append(x)
    return list2




def compressor(segment):
    string1 = ''
    for i in segment:
        string1+=str(i)

    return string1








def passwordGenerator(letter,number,ipass):
    newPass = copyList(ipass)
    #print(letter, number)
    for i in range(0,len(letter)):
        pos = int(number[i])
        newPass[pos] = letter[i]
    x = compressor(newPass)
    return x









def flowControl(items,ipass,diff):
    setOfWords = set()


    leng = len(ipass)
    numbers = []
    for i in range(0, len(ipass)):
        numbers.append(i)

    for n in range(1,diff+1):

        numberCombos = permutations(numbers, n)
        letterCombos = combinations_with_replacement(items, n)
        letters = []
        numPositions = []

        for l in letterCombos:
            letters.append(l)
        for num in numberCombos:
            numPositions.append(num)

        for let in letters:
            for num in numPositions:
                s = passwordGenerator(let,num,ipass)
                setOfWords.add(s)
    listOfWords = list(setOfWords)
    listOfWords.sort()
    for i in listOfWords:
        print(i,end= ' ')


items = input().split(' ')
tpass = input()
ipass = []
for i in tpass:
    ipass.append(i)
diff = int(input())


flowControl(items,ipass,diff)







