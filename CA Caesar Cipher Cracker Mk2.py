

# Caesar Cipher Cracker Mk2
# http://www.codeabbey.com/index/task_view/caesar-cipher-cracker


# Decided to not bother with the first and start from the beginning on this one.

# One thing to add is whitespace frenquency
# In this case I would add whitespace maybe at 20 frequency
# And then readjust the other frequencies



freq = [8.1, 1.5, 2.8, 4.3, 13.0, 2.2, 2.0, 6.1, 7.0, 0.15, 0.77, 7.0, 2.4,
        6.8, 7.5, 1.9, 0.095, 6.0, 6.3, 9.1, 2.8, 0.98, 2.4, 0.15, 2.0, 0.074]



# Takes in a String x and amount of letters e
def cracker(s,e):

    # First Operation is to Shift Each Letter a Set Amount
    # Returns a list of Shifted x messages
    messages = shift(s)

    # Letter Counter
    lc = []
    for i in messages:
        x = lettercount(i)
        lc.append(x)

    # Least Squares
    ls = []
    for i in lc:
        x = least(i,e)
        ls.append(x)

    mini = min(ls)
    indy = ls.index(mini)

    return (messages[indy],indy)



    #mlv




def shift(s):
    messages = []
    for i in range(1, 26):
        ns = ''

        for j in range(0, len(s)):
            v = s[j]
            if v == " ":
                ns = ns + " "
            else:
                y = ord(v) + i
                if y > 90:
                    y = y - 26
                ns = ns + chr(y)

        messages.append(ns)
    return messages



# Takes in a Single String and Returns a Letter Count Array
# Excludes Spaces
def lettercount(s):
    letters = [0] * 26

    for i in s:
        if i!=" ":
            x = ord(i)-65
            letters[x]+=1
    return letters




def least(x,e):
    # e is the total amount of letters
    # x is an array of letter counts

    total = 0
    for i in range(0,len(x)):
        nf = (x[i]/e)
        diff = (freq[i]-x[i])**2
        total = total+diff
    return total


# This is just for formatting my answer the way the questions wants
# Takes the answer and the amount of times
# Returns the first three words and the number we are on
def chomp(x,t):

    three = 0
    ns = ''
    for i in x:
        if three == 3:
            break
        elif i == " ":
            three+=1
            if three == 3:
                break
            ns = ns+ " "
        else:
            ns = ns+i



    t = 24-t
    ans = ns+" "+str(t+1)
    return ans



alist  =[]
times = int(input())
for q in range(times):

    s = input()

    e = 0
    for i in s:
        if i != " ":
            e+=1

    x,t = cracker(s,e)


    aa = chomp(x,t)
    alist.append(aa)


for i in alist:
    print(i,end=' ')
