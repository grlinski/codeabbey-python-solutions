

# Ticket Puzzle
# https://www.codeabbey.com/index/task_view/ticket-puzzle
"""
Completed

Ending Notes
Again another program I'm rather impressed with.
This could use a ton of revision.
Everything is scattered and there are likely better ways of doing everything.
Next time I do something this long add in the logging module
The order of operations and bracket adding functions I thought were fairly impressive
They are so relatively simple, I really should have thought of them on the spot.









This is Possibly a good program to split up
There are a ton of functions that are always the same, they return permutations to use.
I could store them elsewhere.
And I should have split up some more of my functions
Things are cluttered
I'm on the right track so far, but making a Mk2 would make things easier if I hit a wall.


TO DO
AFAIK everthing works.
The program returns an expression and the order of operations.
All I need to do know is convert the ooo into brackets.








"""







from itertools import permutations

# Creates all Permutations of Operations
# From 1 to 5 operators
# Returns 5 lists
def operationPermuations():
    # At Most All I need is 5 operators
    op = ['+','*','/','-']
    opsPerms1 = []
    opsPerms2 = []
    opsPerms3 = []
    opsPerms4 = []
    opsPerms5 = []

    add1 = True
    add2 = True
    add3 = True
    add4 = True



    for a in range(0,4):
        for b in range(0,4):
            for c in range(0,4):
                for d in range(0,4):
                    for e in range(0,4):

                        p1 = [op[e]]
                        p2 = [op[d], op[e]]
                        p3 = [op[c], op[d], op[e]]
                        p4 = [op[b], op[c], op[d], op[e]]
                        p5 = [op[a], op[b], op[c], op[d], op[e]]

                        if d==0 and add1 == True:
                            opsPerms1.append(p1)
                        else:
                            add1 = False
                        if c == 0 and add2 == True:
                            opsPerms2.append(p2)
                        else:
                            add2 = False

                        if b == 0 and add3 == True:
                            opsPerms3.append(p3)
                        else:
                            add3 = False
                        opsPerms4.append(p4)
                        if a == 0 and add4 == True:
                            opsPerms4.append(p4)
                        else:
                            add4 = False

                        opsPerms5.append(p5)
    return opsPerms1,opsPerms2,opsPerms3,opsPerms4,opsPerms5

# BRACKETS
"""
Brackets
Opening brackets come either before a number, or after an operator
Closing brackets come after a number or before an operator
I Only need as many bracket pairs as there are operators.
Or even one pair less, as one bracket pair can always just be added to the outside.
So I really at most have to place 3 bracket pairs, and 1 always on the outside.


New Idea
Alright so for brackets
I have a number sequence with Operators
Turn this into a list via another function.
I also have an order of operation sequence I need to go through
This is the main point of the function.
Find the correct order I need to use operators in.
After this I'll work on printing it properly.




"""
def brackets(x,orderOfOps,correctAns):

    # Turns the Expression into a List
    # Major Problem this undoes the creation of an expression
    # I forgot to not split up numbers.
    expList = expressionToList(x)


    for order in orderOfOps:
        # Problem with using the same list.
        copyExpList = copyList(expList)
        copyOrder = copyList(order)
        ans,goodAnswer = expressionAndOrder(copyExpList,copyOrder)
        #print(ans,correctAns)
        if ans == correctAns and goodAnswer:
            print(x,order)
            return True,x,order
    return False, x,order

# Preforms a Calculation with the Order of Operations and Expression List
"""
This is the main meat of the program
Finding the correct order for the expression to work in.
Needs to return an answer.
And if that matches the correct answer, ans
Then I need to return the expression and order of operations
And eventually use that order to place brackets.

"""
def expressionAndOrder(e,o):
    #print('EXP AND ORDER')
    #print(e)
    #print(o)
    ender = False
    # e is the list of expressions.
    # o is the Order of Operations
    while len(o)!= 0:
        cur = o[0]
        if cur == 1:
            #print(e,o)
            if e[1] == '/' and e[2] == '0':
                return 0, False
            try:
                newNum = eval(str(e[0]+e[1]+e[2]))
            except:
                return 0,False
            e[2] = str(newNum)
            del(e[0])
            del(e[0])
            del(o[0])
            for i in range(0,len(o)):
                if o[i] >1:
                    o[i]-=1
        if cur == 2:
            if e[3] == '/' and e[4] == '0':
                return 0, False
            try:
                newNum = eval(str(e[2]+e[3]+e[4]))
            except:
                return 0,False
            e[4] = str(newNum)
            del(e[2])
            del(e[2])
            del(o[0])
            for i in range(0,len(o)):
                if o[i] >2:
                    o[i]-=1
        if cur == 3:
            if e[5] == '/' and e[6] == '0':
                return 0, False
            try:
                newNum = eval(str(e[4]+e[5]+e[6]))
            except:
                return 0,False
            e[6] = str(newNum)
            del(e[4])
            del(e[4])
            del(o[0])
            for i in range(0,len(o)):
                if o[i] >3:
                    o[i]-=1
        if cur == 4:
            if e[7] == '/' and e[8] == '0':
                return 0, False
            try:
                newNum = eval(str(e[6]+e[7]+e[8]))
            except:
                return 0,False
            e[8] = str(newNum)
            del(e[6])
            del(e[6])
            del(o[0])
            for i in range(0,len(o)):
                if o[i] >4:
                    o[i]-=1
        if cur == 5:
            if e[9] == '/' and e[10] == '0':
                return 0, False
            try:
                newNum = eval(str(e[8]+e[9]+e[10]))
            except:
                return 0,False
            e[10] = str(newNum)
            del(e[8])
            del(e[8])
            del(o[0])


        #print(e)
        #print(o)

    goodAnswer = True

    ans = (e[0])
    ansFloat = float(ans)
    ansFloatToInt = int(ansFloat)
    if ansFloat == ansFloatToInt:
        goodAnswer = True
    else:
        goodAnswer = False

    ans = float(ans)
    ans = int(ans)

    return ans,goodAnswer




def copyList(list1):
    list2 = []
    for i in list1:
        list2.append(i)
    return list2







# Depending on How Many Operators are Present I need to generate all permuations for that Number.
# These are Constant Lists.
def permutationOfOrderOfOperations():
    one = [[1]]
    two = [1,2]
    three = [1,2,3]
    four = [1,2,3,4]
    five = [1,2,3,4,5]

    twoP = permutations(two, 2)
    threeP = permutations(three, 3)
    fourP = permutations(four,4)
    fiveP = permutations(five,5)

    two = []
    three = []
    four = []
    five = []

    for i in twoP:
        x = list(i)
        two.append(x)
    for i in threeP:
        x = list(i)
        three.append(x)
    for i in fourP:
        x = list(i)
        four.append(x)
    for i in fiveP:
        x = list(i)
        five.append(x)

    return one,two,three,four,five



# Expression to List
"""
For some Parts its easier to work with a list than expression,
Needs a counterpart function, list to exp
"""
def expressionToList(x):
    ops = ['+','-','*','/']
    list1 = []
    y= ''
    for i in x:
        if i in ops:
            list1.append(y)
            list1.append(i)
            y = ''
        else:
            y+=i
    list1.append(y)
    return list1






# Used to Create the Intial Expression without Brackets
# Use this to generate bracket Placements
def generateInitialExpression(op1,op2,op3,op4,op5,numPer,ans):
    counter=0

    # These are Lists of Order of Operations, for 1 to 5 operators
    oneO,twoO,threeO,fourO,fiveO = permutationOfOrderOfOperations()
    correct = False
    order = []
    numbers = []

    for i in numPer:

        x = ''

        if len(i) == 6:
            for j in op5:
                x = i[0]+j[0]+i[1]+j[1]+i[2]+j[2]+i[3]+j[3]+i[4]+j[4]+i[5]
                #print(x)
                #print(eval(x))

                correct,numbers,order = brackets(x,fiveO,ans)
                if correct:
                    return numbers,order
                counter += 1
        if len(i) == 5:
            for j in op4:
                x = i[0]+j[0]+i[1]+j[1]+i[2]+j[2]+i[3]+j[3]+i[4]
                correct, numbers, order = brackets(x, fourO, ans)
                if correct:
                    return numbers, order
                counter += 1
        if len(i) == 4:
            for j in op3:
                x = i[0]+j[0]+i[1]+j[1]+i[2]+j[2]+i[3]
                correct, numbers, order = brackets(x, threeO, ans)
                if correct:
                    return numbers, order
                counter += 1
        if len(i) == 3:
            for j in op2:
                x = i[0]+j[0]+i[1]+j[1]+i[2]
                correct, numbers, order = brackets(x, twoO, ans)
                if correct:
                    return numbers, order
                counter += 1
        if len(i) == 2:
            for j in op1:
                x = i[0]+j[0]+i[1]
                correct, numbers, order = brackets(x, oneO, ans)
                if correct:
                    return numbers, order
                counter+=1
    print(counter)
    print('Nothing')
    return 0,0

# PRINTABLE ANSWER
# This takes in the expression and the order of operations.
# n = The numbers and operators
# First as a string then converted to a list
# o is a list of order of operations
def printableAnswer(n,o):
    n = expressionToList(n)
    exp = ''
    print('here')
    while len(o)!=0:
        print('order')
        x = o[0]
        if x == 1:
            b = ('('+n[0]+n[1]+n[2]+')')
            n[2] = b
            del(n[0])
            del(n[0])
            del(o[0])
            for i in range(0,len(o)):
                if o[i] >1:
                    o[i]-=1
        if x == 2:
            b = ('('+n[2]+n[3]+n[4]+')')
            n[4] = b
            del(n[2])
            del(n[2])
            del(o[0])
            for i in range(len(o)):
                if o[i] >2:
                    o[i]-=1
        if x == 3:
            b = ('('+n[4]+n[5]+n[6]+')')
            n[6] = b
            del(n[4])
            del(n[4])
            del(o[0])
            for i in range(len(o)):
                if o[i] >3:
                    o[i]-=1
        if x == 4:
            b = ('('+n[6]+n[7]+n[8]+')')
            n[8] = b
            del(n[6])
            del(n[6])
            del(o[0])
            for i in range(len(o)):
                if o[i] >4:
                    o[i]-=1
        if x == 5:
            b = ('('+n[8]+n[9]+n[10]+')')
            n[10] = b
            del(n[8])
            del(n[8])
            del(o[0])



        print(n)
        print(b)
        print(o)
    print('End')
    print(eval(b))
    print(n)
    return b





# Hopefully Every Permuation of digits for a Given Number
#Returns a List
def numberPermutations(n):
    a = (n[0])
    b = (n[1])
    c = (n[2])
    d = (n[3])
    e = (n[4])
    f = (n[5])
    numPerms = []
    #numPerms.append()

    # Normal
    numPerms.append([a,b,c,d,e,f])

    # 1 Conjoined, Two Numbers
    numPerms.append([a + b , c , d , e ,f])
    numPerms.append([a , b + c, d, e, f])
    numPerms.append( [a , b, c + d, e, f])
    numPerms.append( [a, b, c, d + e, f])
    numPerms.append( [a, b, c, d, e + f])

    # Two Conjoined Two Numbers
    numPerms.append([a + b, c+ d, e, f])
    numPerms.append( [a+ b, c, d + e, f])
    numPerms.append( [a+ b, c, d, e + f])
    numPerms.append( [a, b + c, d+ e, f])
    numPerms.append( [a, b + c, d, e + f])
    numPerms.append([a, b, c + d, e+ f])
    numPerms.append( [a, b, c, d, e, f])

    numPerms.append( [a + b , c + d, e+ f])

    # One Conjoined 3 Numbers
    numPerms.append( [a+ b+ c, d, e, f])
    numPerms.append( [a, b+ c+ d, e, f])
    numPerms.append( [a, b, c+ d+ e, f])
    numPerms.append( [a, b, c, d+ e+ f])

    # Two conjoined 3 numbers
    numPerms.append( [a+ b+ c, d+ e+ f])

    # 1 Conjoined 4 Numbers
    numPerms.append([a+ b+ c+ d, e, f])
    numPerms.append( [a, b+ c+ d+ e, f])
    numPerms.append([a, b, c+ d+ e+ f])

    # 1 Conjoined 5 Numbers
    numPerms.append([a+ b+ c+ d+ e, f])
    numPerms.append( [a, b+ c+ d+ e+ f])

    # 1 Conjoined 6 Numbers
    numPerms.append( [a+ b+ c+ d+ e+ f])

    # More Complex Variations
    # 1 2 3
    numPerms.append( [a, b+ c, d+ e+ f])
    # 2 1 3
    numPerms.append( [a+ b, c, d+ e+ f])

    # 1 3 2
    numPerms.append( [a, b+ c+ d, e+ f])
    # 2 3 1
    numPerms.append( [a+ b, c+ d+ e, f])
    # 3 1 2
    numPerms.append( [a+ b+ c, d, e+f])
    # 3 2 1
    numPerms.append( [a+ b+ c, d+ e, f])

    # 4 2
    numPerms.append( [a+ b+ c+ d, e+f])
    # 2 4
    numPerms.append( [a+ b, c+ d+ e+ f])

    return numPerms



#s = input()
#s = '123456'
#s= '151374'
#ans = 100

#s = '767494'
#ans = 168
#767494=168

finalList = []
op1,op2,op3,op4,op5 = operationPermuations()
cases = int(input())
for i in range(0,cases):
    a,b = input().split('=')
    s = a
    ans = int(b)
    print(s,ans)
    numPer = numberPermutations(s)
    numbers,order = generateInitialExpression(op1,op2,op3,op4,op5,numPer,ans)
    print(numbers,order)
    if numbers == 0 and order ==0:
        finalList.append('0')
    else:
        x = printableAnswer(numbers,order)
        finalList.append(x)
print('Answer !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
for i in finalList:
    print(i,end=' ')


#fiveO = [[1, 2, 3, 4, 5], [1, 2, 3, 5, 4], [1, 2, 4, 3, 5], [1, 2, 4, 5, 3], [1, 2, 5, 3, 4], [1, 2, 5, 4, 3], [1, 3, 2, 4, 5], [1, 3, 2, 5, 4], [1, 3, 4, 2, 5], [1, 3, 4, 5, 2], [1, 3, 5, 2, 4], [1, 3, 5, 4, 2], [1, 4, 2, 3, 5], [1, 4, 2, 5, 3], [1, 4, 3, 2, 5], [1, 4, 3, 5, 2], [1, 4, 5, 2, 3], [1, 4, 5, 3, 2], [1, 5, 2, 3, 4], [1, 5, 2, 4, 3], [1, 5, 3, 2, 4], [1, 5, 3, 4, 2], [1, 5, 4, 2, 3], [1, 5, 4, 3, 2], [2, 1, 3, 4, 5], [2, 1, 3, 5, 4], [2, 1, 4, 3, 5], [2, 1, 4, 5, 3], [2, 1, 5, 3, 4], [2, 1, 5, 4, 3], [2, 3, 1, 4, 5], [2, 3, 1, 5, 4], [2, 3, 4, 1, 5], [2, 3, 4, 5, 1], [2, 3, 5, 1, 4], [2, 3, 5, 4, 1], [2, 4, 1, 3, 5], [2, 4, 1, 5, 3], [2, 4, 3, 1, 5], [2, 4, 3, 5, 1], [2, 4, 5, 1, 3], [2, 4, 5, 3, 1], [2, 5, 1, 3, 4], [2, 5, 1, 4, 3], [2, 5, 3, 1, 4], [2, 5, 3, 4, 1], [2, 5, 4, 1, 3], [2, 5, 4, 3, 1], [3, 1, 2, 4, 5], [3, 1, 2, 5, 4], [3, 1, 4, 2, 5], [3, 1, 4, 5, 2], [3, 1, 5, 2, 4], [3, 1, 5, 4, 2], [3, 2, 1, 4, 5], [3, 2, 1, 5, 4], [3, 2, 4, 1, 5], [3, 2, 4, 5, 1], [3, 2, 5, 1, 4], [3, 2, 5, 4, 1], [3, 4, 1, 2, 5], [3, 4, 1, 5, 2], [3, 4, 2, 1, 5], [3, 4, 2, 5, 1], [3, 4, 5, 1, 2], [3, 4, 5, 2, 1], [3, 5, 1, 2, 4], [3, 5, 1, 4, 2], [3, 5, 2, 1, 4], [3, 5, 2, 4, 1], [3, 5, 4, 1, 2], [3, 5, 4, 2, 1], [4, 1, 2, 3, 5], [4, 1, 2, 5, 3], [4, 1, 3, 2, 5], [4, 1, 3, 5, 2], [4, 1, 5, 2, 3], [4, 1, 5, 3, 2], [4, 2, 1, 3, 5], [4, 2, 1, 5, 3], [4, 2, 3, 1, 5], [4, 2, 3, 5, 1], [4, 2, 5, 1, 3], [4, 2, 5, 3, 1], [4, 3, 1, 2, 5], [4, 3, 1, 5, 2], [4, 3, 2, 1, 5], [4, 3, 2, 5, 1], [4, 3, 5, 1, 2], [4, 3, 5, 2, 1], [4, 5, 1, 2, 3], [4, 5, 1, 3, 2], [4, 5, 2, 1, 3], [4, 5, 2, 3, 1], [4, 5, 3, 1, 2], [4, 5, 3, 2, 1], [5, 1, 2, 3, 4], [5, 1, 2, 4, 3], [5, 1, 3, 2, 4], [5, 1, 3, 4, 2], [5, 1, 4, 2, 3], [5, 1, 4, 3, 2], [5, 2, 1, 3, 4], [5, 2, 1, 4, 3], [5, 2, 3, 1, 4], [5, 2, 3, 4, 1], [5, 2, 4, 1, 3], [5, 2, 4, 3, 1], [5, 3, 1, 2, 4], [5, 3, 1, 4, 2], [5, 3, 2, 1, 4], [5, 3, 2, 4, 1], [5, 3, 4, 1, 2], [5, 3, 4, 2, 1], [5, 4, 1, 2, 3], [5, 4, 1, 3, 2], [5, 4, 2, 1, 3], [5, 4, 2, 3, 1], [5, 4, 3, 1, 2], [5, 4, 3, 2, 1]]

#brackets('1/2-3*4-5*6',fiveO)

#e = ['1', '/', '2', '-', '3', '*', '4', '-', '5', '*', '6']
#o = [1, 2, 4, 3, 5]

#expressionAndOrder(e,o)








