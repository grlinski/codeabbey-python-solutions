
# Works decently enough


# http://www.codeabbey.com/index/task_view/luhn-algorithm
# Works except I guess swap digits should start from the end and work

# All this does is add the digits up. Only works on string lists
# Returns total of digits
def adddigitsup(x):
    total = 0
    q = 1
    for i in x:
        r = int(i)
        if q%2 == 1:
            total = total+int(i)
        elif int(i) >4:

            total = total + ((r*2)-9)
        else:
            total = total + (r*2)
        q+=1
    return total






# Continually Passed a list with a 0-9 replacing the ? in the list into addingdigitsup
# Works on test case
def questionmark(x):
    holder = 100
    for j in range(0,len(x)):
        if x[j] == '?':
            holder = j


    for i in range(0,10):
        x[holder] = str(i)
        ten = adddigitsup(x)
        if ten%10 == 0:
            return i






# Swaps two adjacent digits and throws them into adddigitsup
def swapdigits(x):
    holder = 0
    #print(x)
    answer = ''
    q = x
    for i in range(len(x)-1,0,-1):
        ori = x[i]
        second = x[i-1]
        q[i-1] = ori
        q[i] = second
        #print(q)

        ten = adddigitsup(q)
        #print(ten)

        if ten % 10 == 0:
            for j in q:
                answer = answer + str(j)
            return answer
        q[i] = ori
        q[i-1] = second










answer_list = []
answer = ""

times = int(input())

for i in range(0,times):

    # This section takes in input and creates two lists, one in normal order the other reversed.
    # Note the lists are in string format not int
    original = input().strip()
    digits = []
    reverseddigits = []
    for i in original:
        digits.append(i)
    reverseddigits = digits[::-1]

    # Questionmark Remover
    if '?' in reverseddigits:
        #print(reverseddigits)
        singledigit = questionmark(reverseddigits)
        for d in range(0,len(original)):

            if original[d] == "?":
                answer = original[:d] + str(singledigit) + original[d+1:]
                break

    # Checks if the digits add to a multiple of ten
    # If not it goes through digit swapping
    else:
        ten = adddigitsup(reverseddigits)
        if ten%10 == 0:
            answer = original
        else:
            ranswer = swapdigits(reverseddigits)
            answer = ranswer[::-1]
    answer_list.append(answer)



for l in answer_list:
    print(l,end = " ")







"""
a = ['5', '9', '9', '4', '4', '1', '1', '5', '1', '0', '0', '4', '7', '1', '2', '1']
b = ['5', '9', '9', '4', '1', '1', '4', '5', '1', '0', '0', '4', '7', '1', '2', '1']
a1 = a[::-1]
b1 = b[::-1]

print(adddigitsup(a1))
print(adddigitsup(b1))
"""

"""

1
4123175904981754

1
4123175?04981754



"""






