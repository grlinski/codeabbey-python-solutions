

# Binary Search
#  https://www.codeabbey.com/index/task_view/binary-search
"""
Why the none problem????

Try:

1
18.02453480 0.75865785 1732.96577937 -538.20262597


"""




import math

def equation(a,b,c,d):


    x = 73.595368554162
    top = 100
    bottom = 0

    for i in range(0,10000):


        middle = (top+bottom)/2
        # Top Part
        x = top
        p1 = (a * x + b * math.sqrt(x ** 3))
        p2 = -(-(c * (math.exp(-x / 50))) - d)
        ansTop = abs(p1-p2)


        if round(p1,7) == round(p2,7):
            return x

        # Bottom Part
        x = bottom
        p1 = (a * x + b * math.sqrt(x ** 3))
        p2 = -(-(c * (math.exp(-x / 50))) - d)
        ansBottom = abs(p1 - p2)

        print(top,bottom,ansTop,ansBottom)
        if round(p1,7) == round(p2,7):
            return x

        if ansBottom == ansTop:
            if ansBottom < 50:
                bottom = 0
            else:
                top = 100
        elif ansBottom < ansTop:
            top = middle
        else:
            bottom = middle




ans = []
cases = int(input())
for i in range(cases):
    a,b,c,d = map(float, input().split(' '))
    z = equation(a, b, c, d)
    ans.append(z)
#a,b,c,d = 0.59912051,0.64030348,263.33721367,387.92069617



for i in ans:
    print(i,end = ' ')








"""
print(a*x+b*math.sqrt(x**3))
print((a*x)+(b*math.sqrt(x**3)))

p1 = (a*x+b*math.sqrt(x**3))
print('.....................')
print(p1-(c*(math.exp(-x/50)))-d)
p2 = (-(c*(math.exp(-x/50)))-d)
print((a*x+b*math.sqrt(x**3))-(c*(math.exp(-x/50)))-d)

print(p2)
#print(c**(-x/50)-d)
"""












