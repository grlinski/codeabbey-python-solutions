

# Four Pics One Word
# https://www.codeabbey.com/index/task_view/four-pics-one-word

"""
Completed

Ending Notes
Hmm not too sure what to say,
Maybe incorporate importing text files more often
However this requires me to have them always located in the same folder.
If I do this name the text file and program exactly the same.



Requires the File wordsForCA.txt to work





"""

from itertools import permutations

def createWordStart(letters):
    x = permutations(letters,4)
    words = []

    for i in x:
        y = ''
        y +=str(i[0])+str(i[1])+str(i[2])+str(i[3])
        words.append(y)
    return words


# Compares a Single Word to the Rest of the Letter Pool
def remainingLetters(word,letterpool):
    #print(word)
    for i in word:
        if i in letterpool:
            letterpool.remove(i)
        else:
            return False
    return True


def copyList(list1):
    list2 = []
    for i in list1:
        list2.append(i)
    return list2



def wordCounter(length,letters,dWords):

    # Note Will Run into Problems if length is less than 4

    wordStart = createWordStart(letters)
    candidateWords = []
    startWords = []
    for i in range(0,len(dWords)):
        x = str(dWords[i])
        z = x.lstrip('[\'')
        z = z.rstrip(']\'')
        y = x[2:6]
        if y in wordStart:
            candidateWords.append(z)
            startWords.append(y)

    print(candidateWords)
    counter = 0
    for i in candidateWords:
        letterpool = copyList(letters)
        addTo =  remainingLetters(i,letterpool)
        if addTo == True:
            counter+=1
            #print(i,counter)
    return counter





wordFileName = 'wordsForCA.txt'
allWords = []
dictLength = {}

openfile = open(wordFileName, 'r')
x = (openfile.readlines())
already_list = []
for i in x:
    j = i.strip('\n')
    leng = len(j)
    if leng in dictLength:
        q = [j]
        dictLength[leng].append(q)
    else:
        dictLength[leng] = [j]

    allWords.append(j)

openfile.close()

times = int(input())
#times = 1
ans = []
for t in range(times):
    s = input().split()
    length = int(s[0])
    letters = s[1:]
    dWords = dictLength[length]
    a = wordCounter(length, letters,dWords)
    ans.append(a)

for i in ans:
    print(i,end= ' ')









