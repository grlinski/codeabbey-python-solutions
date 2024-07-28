
# http://www.codeabbey.com/index/task_view/luhn-algorithm



def questionmark(x):

    for i in range(0,10):
        n = []
        for j in range(0, len(x)):
            if x[j] == "?":
                x[j] = int(i)
            # Even
            if (j) % 2 != 0:
                q = int(x[j])
                if q > 4:
                    q = (q * 2) - 9
                else:
                    q = (q * 2)
                n.append(q)
            # Odd
            elif (j + 1) % 2 == 0:
                q = int(x[j])
                n.append(q)
        total = 0
        for k in cnum:
            total = total +int(k)
        if total%10 == 0:
            return i





def swapped(x):
    pass


answers = []


items = int(input())

for i in range(0,items):
    digits = []
    answer = ""
    cnum = input()
    ori = cnum
    cnum = cnum[::-1]
    solved = False
    for j in range(0,len(cnum)):
        if cnum[j] == "?":
            digits.append(-1)
        # Even
        elif (j) % 2 != 0:
            q = int(cnum[j])
            if q > 4:
                q = (q*2)-9
            else:
                q = (q*2)
            digits.append(q)
        # Odd
        elif (j+1)%2 == 0:
            q = int(cnum[j])
            digits.append(q)

        # Check if correct, all digits add up to a mulitple of 10
        total = 0
        if -1 in digits:
            qdigit = questionmark(digits)
            r = str(qdigit)
            answer = ori.replace("?",r)
            solved = True

        for j in digits:
            j = int(j)
            total = total+j
        if total%10 == 0:
            solved = True
        else:
            swapped(cnum)
        if solved == True:
            answers.append(answer)
        else:
            print('error')




print(cnum)
total = 0


"""

1
4123175904981754


"""






