
# http://www.codeabbey.com/index/task_view/yacht-or-dice-poker

numberoftimes = int(input())

types = {2:'pair', 3:'three', 4:"four", 5:"yacht",6:"two-pairs",
         7:"full-house", 8:"small-straight", 9:"big-straight"}

bigstraight = [2,3,4,5,6]
smallstraight = [1,2,3,4,5]
answers = []
for i in range(0,numberoftimes):
    hand = []
    counter = [0,0,0,0,0,0,0]
    pairs = 0
    x = input()
    for j in range(0,len(x),2):
        hand.append(int(x[j]))
    hand.sort()


    for i in hand:
        counter[i]+=1
    if hand == bigstraight:
        answers.append(types[9])
    elif hand == smallstraight:
        answers.append(types[8])
    elif 5 in counter:
        answers.append(types[5])
    elif 4 in counter:
        answers.append(types[4])
    elif 3 in counter and 2 in counter:
        answers.append(types[7])
    elif 3 in counter:
        answers.append(types[3])
    else:
        for i in counter:
            if i == 2:
                pairs+=1
        if pairs == 1:
            answers.append(types[2])
        else:
            answers.append(types[6])

print("")
for i in answers:
    print(i,end=" ")


"""

3
3 6 5 6 1
1 6 6 1 6
2 4 3 5 1


3
3 6 5 6 1
1 6 6 1 6
2 4 3 5 1



"""








