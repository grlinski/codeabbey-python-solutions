# Josephus Problem
# http://www.codeabbey.com/index/task_view/josephus-problem
# Which position is the last man standing?

# n = number of people
# k = steps

x,y = input().split()
n = int(x)
k = int(y)


people = []
for j in range(1,n+1):
    people.append(j)


#people = [1,2,3,4,5,6,7,8,9,10]
#k = 3

k = k-1
step = k
times = 1

length = len(people)
while len(people) != 1:

    # A Problem I encounter is when there are only 2 elements in the array and steps = length
    # In this case the first element in the array should be eliminated
    # So this if statement is used for that contingency
    if len(people) == step:
        del(people[0])
        break
    #print(length,step)
    #print("Dead ", people[step])
    del(people[step])
    step+=k
    length = len(people)
    if step >= length:
        step = step-length
    #print(people)







for i in people:
    print (i)






"""

10 2


5 2
Should go 2 4 1 5
With 3 being alive


3 3

ends on 2


10 3

ends on 4

5 3
ends on 3


"""








