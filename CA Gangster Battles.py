

# Gangster Battles
# https://www.codeabbey.com/index/task_view/gangster-battles

"""
Completed
End Notes
Actually fully read the question
I had the correct idea at first, then screwed it up
The only important thing I came up with is the binary on/off method
When I want every permutation in which a part of a list is on or off
I can just cycle through a set of binary numbers, 0s and 1s.



So I screwed this up and made it harder than it should be
If I pick a member I take both p and g no matter what, not one or the other.
So I can go back to binary.



"""




clansT,pistolT,grenadeT = map(int, input().split(' '))

clans = []
for i in range(clansT):
    cases = int(input())
    temp = []

    for j in range(cases):
        p,g = map(int, input().split(' '))
        x = [p,g]
        temp.append(x)
    clans.append(temp)



# All data is stored in the clans List
# Each entry is the clan#
# After which each entry is the P,G for an individual member.

# '11111 11111 11111 11'
# 131071
#print(int('11111111111111111',2))
matches = []

# Create Matches
# Note I may need to just incorporate this into another function
# Instead of storing it into a list, may lead to overflow.
def createMatches(upTo):
    # Make every permuations of 0,1,2
    # 0 means 0th place, 1 is first place and 2 is off.
    # 0,1,2
    matches = []

    for i in range(0,131072):
        x = bin(i)
        y = str(x[2:])
        if len(y) < upTo:
            adder = ''
            for j in range(upTo-len(y)):
                adder+='0'
            y = adder+y
        if len(y) >upTo:
            break
        y = y[::-1]
        matches.append(y)

    return matches

def countOnes(item):
    total = 0
    for i in item:
        if i=='1':
            total+=1
    return total


def findWhichClans(c,ansP,ansG):

    matches = createMatches(len(c))
    for m in matches:
        totalP = 0
        totalG = 0
        for i in range(0,len(m)):
            if m[i] == '0':
                pass
            else:
                totalP +=c[i][0]
                totalG +=c[i][1]

        if totalP == ansP and totalG == ansG:
            ones = countOnes(m)
            return ones


def flowControl(clans,pistolT,grenadeT):
    ans = []
    for i in clans:
        print(i)
        x = findWhichClans(i,pistolT,grenadeT)
        ans.append(x)
    for i in ans:
        print(i,end=' ')


flowControl(clans,pistolT,grenadeT)








