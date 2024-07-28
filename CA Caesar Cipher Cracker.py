

# Caesar Cipher Cracker
# http://www.codeabbey.com/index/task_view/caesar-cipher-cracker

freq = [8.1, 1.5, 2.8, 4.3, 13.0, 2.2, 2.0, 6.1, 7.0, 0.15, 0.77, 7.0, 2.4,
        6.8, 7.5, 1.9, 0.095, 6.0, 6.3, 9.1, 2.8, 0.98, 2.4, 0.15, 2.0, 0.074]





# Generates Every Possible Message by Shifting Letter Values
# Returns them as a list along with the amount of letters in the message
def shift(s):


    messages = []
    for i in range(1, 26):
        ns = ''
        amt = 0
        for j in range(0, len(s)):
            v = s[j]
            if v == " ":
                ns = ns + " "
            else:
                amt+=1
                y = ord(v) + i
                if y > 90:
                    y = y - 26
                ns = ns + chr(y)

        messages.append(ns)
    return messages,amt


# Least Squares
def least_squares(s,leng):
    print('length',leng)
    lsvalue = []


    for i in s:
        letters = [0]*26
        total = 0

        for j in range(0,len(i)):
            x = i[j]
            if x == ' ':
                pass
            else:
                y = ord(x)-65
                letters[y]+=1

        #print(letters)

        for k in range(0,len(letters)):
            #print(letters[k]/leng, freq[k])

            diff = ((letters[k]/leng)-freq[k])**2
            total = total+diff
        lsvalue.append(total)

    return lsvalue















# Main Control for Caesar Cracker
def cracker(x):

    messages,amt = shift(x)

    lsvalues = least_squares(messages,amt)

    for i in lsvalues:
        print(i)

    maxi = max(lsvalues)

    indy = lsvalues.index(maxi)

    print(messages[indy])






    #return messages




times = int(input())




for i in range(times):
    x = input()
    print(x)
    r = cracker(x)

for i in r:
    print(i)





"""


1
XIP DBSFT PG ESFBNT


1
VJQWIJ KV OCMGU VJKPIU XGTA SWGGT


"""







