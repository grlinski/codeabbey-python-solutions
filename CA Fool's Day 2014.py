

times = int(input())
answers = []

for i in range(0,times):
    list1 = list(map(int, input().strip().split(' ')))

    total = 0
    for j in list1:
        total = total + j**2
    answers.append(total)


for i in answers:
    print(i, end = " ")











