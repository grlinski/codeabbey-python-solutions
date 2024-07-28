


# Most Frequent Word
# https://www.codeabbey.com/index/task_view/most-frequent-word


# Consonants at Odd
# Vowels at even
# Mod 19 for Cons, Mod 5 for Vowels
def funnyWordsGen(next):

    vowels = 'aeiou'
    cons = 'bcdfghjklmnprstvwxz'


    ans = ''

    n = 6
    #next = 99658
    counter = 1
    dict1 = {}
    maxi = 0

    for i in range(900000):
        word =''
        counter = 1
        for j in range(n):
            next = (445 * next + 700001) % 2097152
            if counter%2 !=0:
                word+=cons[next%19]
                #print(cons[next%19])
            else:
                #print(vowels[next%5])
                word += vowels[next % 5]
            counter+=1
        if word in dict1:
            dict1[word]+=1

            if dict1[word] > maxi:
                maxi = dict1[word]
                ans = word
        else:
            dict1[word] = 1
    return dict1,ans



#A = 445, C = 700001, M = 2097152

next = int(input())

dict1,ans = funnyWordsGen(next)

print(ans)


