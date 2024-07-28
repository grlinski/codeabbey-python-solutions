no = int(input())
nos = input()
nos = nos.split()
nos = [int(i) for i in nos]
sum = 0
for i in range(no):
    sum += nos[i]
print(sum)