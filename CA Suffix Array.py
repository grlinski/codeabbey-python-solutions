

# Suffix Array
# https://www.codeabbey.com/index/task_view/suffix-array

"""
End Notes
Fairly Trivial
Nothing of note to note.


# Spaces go first.





"""

def indexList(q):
    preIndex = []
    for i in range(0,len(q)):
        x = q[i:]
        a = [x,i]
        preIndex.append(a)

    preIndex.sort()

    ansIndex = []
    for i in preIndex:
        ansIndex.append(i[1])
    return ansIndex



q = input()
ans = indexList(q)

for i in ans:
    print(i,end=' ')

















