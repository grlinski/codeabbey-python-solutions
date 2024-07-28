# Fibonacci Divisibility
# http://www.codeabbey.com/index/task_view/fibonacci-divisibility


times = int(input())
values = list(map(int, input().strip().split(" ")))
maximum = max(values)+1

def fibonacci_gen(x):
    fib_list = []
    fib_list.append(0)
    fib_list.append(1)
    count = 0
    c = 1
    j = 0
    while count < x-2:
        # Semi Explanation
        # h stores the previous value of c
        # c the current value then has last times c value, which is stored in j added on to it
        # Obviously things are a bit different the first time the loop runs
        # then h, the holder value transfers its value to j

        h = c
        c = c + j
        j = h
        fib_list.append(c)
        count += 1
    return fib_list


x = fibonacci_gen(maximum)


for div in values:
    for num in range(1,len(x)):
        if x[num]%div == 0:
            print(num,end = ' ')
            break











