
# http://www.codeabbey.com/index/task_view/code-guesser
# Already done in Java
# Trying to make it better in Python

# As far as I can tell it fully works now

number_of_items = int(input())
guesses = []
correct_digits = []


first = []
second = []
third = []
fourth = []


#Digit Lists
for i in range(0,10):
    first.append(i)
    second.append(i)
    third.append(i)
    fourth.append(i)

# These are the correct digits
c1 = -1
c2 = -1
c3 = -1
c4 = -1

d1 = 0
d2 = 0
d3 = 0
d4 = 0


# Digit Locks
# When 1 the digit is confirmed
lock1 = 0
lock2 = 0
lock3 = 0
lock4 = 0




# Reads in input
while True:
    try:
        x,y = input().split()
    except:
        break
    guesses.append(x)
    correct_digits.append(int(y))




# Whenever there are zero correct numbers in a guess, this removes all those digits from the possibilities
# This probably could be incorporated into the main loop, but whatever
for i in range(0,len(guesses)):
    x = guesses[i]
    d1 = int(x[0])
    d2 = int(x[1])
    d3 = int(x[2])
    d4 = int(x[3])
    if correct_digits[i] == 0:
        if d1 in first:
            first.remove(d1)
        if d2 in second:
            second.remove(d2)
        if d3 in third:
            third.remove(d3)
        if d4 in fourth:
            fourth.remove(d4)


# Main Loop
# This is for guesses which have 1 or more correct digits

# Number Lock in

if len(first) == 1:
    c1 = first[0]
if len(second) == 1:
    c2 = second[0]
if len(third) == 1:
    c3 = third[0]
if len(fourth) == 1:
    c4 = fourth[0]

# Main Loop

while c1 == -1 or c2 == -1 or c3 == -1 or c4 == -1:

#for qt in range(0,12):

    for i in range(0,len(guesses)):
        numcorrect = correct_digits[i]
        x = guesses[i]

        truths = 0
        t1 = 0
        t2 = 0
        t3 = 0
        t4 = 0

        # Digit Locker
        # C is for the loop, lock is for other reasons
        # They probably cold be the same variable
        if len(first) == 1:
            lock1 = 1
            c1 = first[0]
        if len(second) == 1:
            lock2 = 1
            c2 = second[0]
        if len(third) == 1:
            lock3 = 1
            c3 = third[0]
        if len(fourth) == 1:
            lock4 = 1
            c4 = fourth[0]

        alreadyconfirmed = 0


        if numcorrect != 0:

            d1 = int(x[0])
            d2 = int(x[1])
            d3 = int(x[2])
            d4 = int(x[3])

            # Gives us the amount of digits we already know for this guess
            if d1 == c1:
                alreadyconfirmed+=1
            if d2 == c2:
                alreadyconfirmed+=1
            if d3 == c3:
                alreadyconfirmed+=1
            if d4 == c4:
                alreadyconfirmed+=1

            #
            if d1 in first:
                t1 = 1
                truths +=1
            if d2 in second:
                t2 = 1
                truths +=1
            if d3 in third:
                t3 = 1
                truths +=1
            if d4 in fourth:
                t4 = 1
                truths +=1


            if (numcorrect == truths):
                #print("T")
                #print(truths, x)
                #print(t1,t2,t3,t4)
                if t1 == 1:
                    c1 = d1
                    first = []
                    first.append(c1)
                if t2 == 1:
                    c2 = d2
                    second = []
                    second.append(c2)
                if t3 == 1:
                    c3 = d3
                    third = []
                    third.append(c3)
                if t4 == 1:
                    c4 = d4
                    fourth = []
                    fourth.append(c4)

            # If we know we already have the confirmed digit we can remove the other digits from the possibilities

            if ((numcorrect - alreadyconfirmed) == 0):

                if lock1 == 0 and d1 in first:
                    first.remove(d1)
                if lock2 == 0 and d2 in second:
                    second.remove(d2)
                if lock3 == 0 and d3 in third:
                    third.remove(d3)
                if lock4 == 0 and d4 in fourth:
                    fourth.remove(d4)


















print(first)
print(second)
print(third)
print(fourth)

print(c1,c2,c3,c4)

print(lock1,lock2,lock3,lock4)













"""

22
7999 0
0174 1
9248 0
7898 0
0395 1
1220 0
8008 1
1508 0
4075 1
1501 0
7494 0
2923 0
3284 0
5143 0
1412 1
9204 0
2804 0
3060 1
4547 0
5708 0
0935 1
0792 2


"""
"""
23
4628 0
9528 0
9561 0
7353 0
7375 1
4327 0
7628 0
7921 0
6505 0
0240 1
8125 0
4791 0
1675 1
0937 1
6553 0
4851 0
3573 1
8236 0
3528 0
3194 1
7607 0
6352 0
8063 1



"""

