

# Dungeons and Dragons Dice
# http://www.codeabbey.com/index/task_view/dungeons-and-dragons-dice

def GCD(a,b):

    while a != b:
        if a > b:
            a = a-b
        else:
            b = b-a
    return a



def median(x):

    x.sort()

    leng = len(x)
    if leng%2 == 0:
        y1 = leng//2
        y2 = (leng//2)-1
        median = (x[y1]+x[y2])//2
    else:
        y1 = (len(x)-1)//2
        median = x[y1]

    return median




def checker(x):
    del(x[-1])
    mini = min(x)
    maxi = max(x)

    aver = sum(x)/100
    die = 0
    sides = 0



    print(str(mini)+'d'+str(maxi//mini),end=' ')
    #print((mini+maxi)/2)
    #print(GCD(mini,maxi))
    #print(aver)
    #print(median(x))



for i in range(3):
    q = list(map(int, input().strip().split(' ')))

    checker(q)















