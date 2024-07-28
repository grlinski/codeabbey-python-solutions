
import math, datetime

times = int(input())
answer = []
start = datetime.datetime.now()

divisors = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71]


while times > 0:
    x1,y1,pq = input().split()
    x = int(x1)
    y = int(y1)
    pages = int(pq)

    semiprime = True
    for i in divisors:
        if pages%i==0:
            workable = pages//i
            pages = i
            semiprime = False
            break
    if semiprime == True:
        workable = pages
    print(workable)

    low = min(x,y)

    z = (1/x)+(1/y)

    ysec = 1/y
    xsec = 1/x


    #a = math.ceil(pages/z)
    total = 0
    check = True
    holder = 1
    seconds=0

    p1com = 0
    p2com = 0
    p1part = 0
    p2part = 0

    while total < pages:
        p1part = p1part+xsec
        p2part = p2part+ysec

        p1com = p1com+(p1part//1)
        p2com = p2com+(p2part//1)

        p1part = p1part-(p1part//1)
        p2part = p2part - (p2part // 1)

        total = p1com+p2com
        seconds+=1



    seconds = seconds*workable
    answer.append(seconds)
    print("To Go: ",times)
    times-=1

print()
print("Answers:")
for i in answer:
    print(i,end=" ")
end = datetime.datetime.now()
print()
print("Runtime")
print(end-start)
"""

2
1 1 5
3 5 4


"""



