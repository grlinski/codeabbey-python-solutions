


# Emirp primE
# https://www.codeabbey.com/index/task_view/emirp-prime


"""
Ending Notes
Learned about different primality tests
This one uses a probabilistic test call miller-rabin
I have a py file on it, but add to wiki main.




"""











import math

import random


# Where n is an odd integer to be tested for primality.
# Returns True or False for Primality.
# However this number is not guaranteed to be prime, just very high likelyhood
def millerRabin(n):
    # This is what I return if the number is probably prime
    # As in it passes the test k times.
    probablyPrime = True
    # I Skipped This Part
    # Just returned True or False

    # Fast Checks for Annoying Numbers
    passPrimes = [2, 3, 5, 7]
    autoFail = [0, 1, 4, 6, 8, 9]
    if n in passPrimes:
        return True
    if n in autoFail:
        return False

    d = n - 1
    s = 0
    # (2**s)*d == n-1
    # This needs to be true.

    while d % 2 == 0:
        # Bit Shift
        d >>= 1
        s += 1

    def trial_composite(a):
        x = pow(a, d, n)
        if x == 1:
            return False
        for i in range(s):
            if pow(a, (2 ** i) * d, n) == n - 1:
                return False
        return True

    # Trials is the parameter that determines accuracy of the test.
    # Basically how many random checks are done on the number.
    # There is always a chance of picking a number that gives false positive.
    # The more trials the more accurate but longer
    trials = 1

    for i in range(trials):
        a = random.randint(2, n - 1)
        if trial_composite(a):
            return False

    return True


# This moves our number up to a possibly prime number
# Example if x == 800, Nothing in the 800s will work
# I need an odd number in front and back
# So I'd bump the number up to 901

def moveTo(x):
    # May as well do this dynamically
    # I can't think of a mathematical approach off the top of my head
    # So I'll do it lazily.
    string1 = str(x)
    firstDigit = str(int(string1[0])+1)
    leng = len(string1)

    print(firstDigit,leng)
    zeros = leng-1

    string2 = firstDigit
    for i in range(zeros):
        string2+='0'

    number = int(string2)+1

    return number




def basicChecks(x):
    if x%2==0:
        return False
    if x%3==0:
        return False
    if ((x+1)%2 !=0) or ((x+1)%2 !=0):
        return False

    total = 0
    string1 = str(x)
    for i in string1:
        total+=int(i)
    if total%3 == 0:
        return False

    return True



ans = []
cases = int(input())


for i in range(cases):
    x = int(input())
    if x%2 ==0:
        x+=1
    print('X',x)

    while True:

        if basicChecks(x):
            primer = millerRabin(x)
            if primer:
                rev = str(x)
                rev = int(rev[::-1])
                primer = millerRabin(rev)
                if primer:
                    print('Ans',x)
                    ans.append(x)
                    break
        x+=2
        string1 = str(x)
        num1 = int(string1[0])
        if int(num1%2 == 0 or num1%5==0):
            x = moveTo(x)

#
print('ANSWERS')
for i in ans:
    print(i,end= ' ')







"""
Problems

40450182697091728401819



"""


