# Used for Permutations

# https://en.wikipedia.org/wiki/Heap%27s_algorithm


x = [1,2,3]
holder = 0

def permutation(lst):
    n =len(lst)
    if n == 0:
        return []
    if n == 1:
        return [lst]
    l = []

    for i in range(n):
        m = lst[i]

        remLst = lst[:i] + lst[i + 1:]

        for p in permutation(remLst):
            l.append([m] + p)
    return l


# Driver program to test above function
data = list('123')
print(permutation(data))

