# http://www.codeabbey.com/index/task_view/matching-brackets



"""
4 Types of brackets
([[<
to solve this keep track of how many starting and ending brackets and of which types
They need to match at the end
Also just keep track of the last starting bracket you encounter
If it doesn't match the next ending bracket then the brackets are incorrect
If they match cancel them out and go back to the previous open bracket



starts = '<[[('
ends = '>]})'


Note Just checked this below won't work
Or create two lists one that adds start and the other that adds ends
Reverse and compare the lists





"""

# Two lists with start and end brackets
starts = ['(',"{","[","<"]
ends = [')','}',']','>']


# How many times to run
times = int(input())
answer_list = []


# Main loop
for i in range(0,times):
    x = []
    y = []
    correct = 1
    position = 0

    # r is the string we are working with
    r = input().strip()
    # For every character in r we see if it is in starts or ends, otherwise we ignore
    for j in r:
        if j in starts:
            x.append(j)
        # Basically when we encounter an end bracket it has to match the last start bracket
        # Otherwise the orientation is incorrect
        elif j in ends:
            #print(j)
            if j == ")" and x[-1] == "(":
                del(x[-1])
            elif j == "}" and x[-1] == "{":
                del(x[-1])
            elif j == "]" and x[-1] == "[":
                del(x[-1])
            elif j == ">" and x[-1] == "<":
                del(x[-1])
            else:
                correct = 0
                break
    # If there are any start brackets without a corresponding end bracket then the orientation is incorrect
    if len(x) >0:
        correct = 0
    answer_list.append(correct)



for q in answer_list:
    print(q,end=" ")

























