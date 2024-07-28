

# Linear Congruential Generator
# https://www.codeabbey.com/index/task_view/linear-congruential-generator


cases = int(input())

for i in range(cases):
    A, C, M, X0, N = map(int, input().split(' '))
    Xcur = X0
    for j in range(N):
        Xnext = (A * Xcur + C) % M
        Xcur = Xnext
        print(Xcur)
    print(Xcur)




