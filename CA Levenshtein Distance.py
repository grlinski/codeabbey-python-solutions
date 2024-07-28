
# https://www.youtube.com/watch?v=We3YDTzNXEk

# Levenshtein Distance
# http://www.codeabbey.com/index/task_view/levenshtein-distance

def dist(a,b):
    dif = abs((ord(a)-ord(b)))
    return dif





def leve_dist(x,y):
    col = len(x)+1
    row = len(y)+1
    m1 = [0]*col
    mat = []
    for i in range(row):
        m2 = m1[::]
        mat.append(m2)

    # Distance in First Row and Column
    for i in range(0,row):
        mat[i][0] = i

    for i in range(0,col):
        mat[0][i] = i



    for i in range(1,row):

        for j in range(1,col):
            left = mat[i][j-1]
            up = mat[i-1][j]
            diag = mat[i-1][j-1]

            mini = min(left,up,diag)
            if x[j-1] == y[i-1]:
                mat[i][j] = diag
            else:
                mat[i][j] = mini+1



    return mat[-1][-1]









#first,last = 'plain','plan'
#first,last = 'abcdef','azced'
times = int(input())
anslist = []

for q in range(times):
    first, last = input().split(' ')

    f = []
    e = []

    for i in first:
        f.append(i)
    for i in last:
        e.append(i)

    anslist.append(leve_dist(f,e))


for i in anslist:
    print(i,end=' ')










































