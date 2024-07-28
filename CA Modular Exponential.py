


# Modular Exponentiation
# https://www.codeabbey.com/index/task_view/modular-exponentiation
"""
I did something similar to this in Euler I believe.
bascially I only need to keep a certain amount of decimal places.
Anything beyond that is superfluous
Apparently not

Even with the formula I have going now it requires several billion calculations for one entry
Likely there is a pattern I can exploit

For example
Let's say
a b m
10 882 3




"""



def calculation(a,b,m):

    c = 1
    ep = 0

    for i in range(0,b):
        c = (a*c)%m
        print(c)
    print(c)











cases = int(input())


final = []
for i in range(cases):
    a,b,m = map(int, input().split(' '))
    print((a**b)%m)
    ans = calculation(a,b,m)
    final.append(ans)


for i in final:
    print(i,end= ' ')

