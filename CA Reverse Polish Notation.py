
# Reverse Polish Notation
# https://www.codeabbey.com/index/task_view/reverse-polish-notation
"""
Completed


Ending notes
Again Polish Notation is awful
I hopefully never need to use it again.
However I guess it's good I learned it.
I probably should add an entry into my Py Wiki
Not much else to note on this.











This notation is awful, there's a reason no one uses it
Anyways it seems that I need to do each block of operations until there is a single number and operator paired
Not true ignore this point.

70 11 mul 5 div 219 add 28 26 6 sub 6 sub div mul 448 7 mul sqrt add


Alright I figured out Reverse Polish Notation, So I'll go through the Example in detail
For the most part I just need to start at the left most side.
Starting:
70 11 mul 5 div 219 add 28 26 6 sub 6 sub div mul 448 7 mul sqrt add
Multiply 70*11 = 770
770 5 div 219 add 28 26 6 sub 6 sub div mul 448 7 mul sqrt add
Divide 770 by 5 = 154
154 219 add 28 26 6 sub 6 sub div mul 448 7 mul sqrt add
Add 154+219 = 373
373 28 26 6 sub 6 sub div mul 448 7 mul sqrt add
Now this is where I originally screwed up and things get annoying.
I need to apply the first operator to the last two numbers
So 26 6 sub, 26-6 = 20
373 28 20 6 sub div mul 448 7 mul sqrt add
And again same thing
20 6 sub, 20-6 = 14
373 28 14 div mul 448 7 mul sqrt add
Next 28 div 14 = 2
373 2 mul 448 7 mul sqrt add
Then 373 2 mul, 373*2 = 746
746 448 7 mul sqrt add
And 448 7 mul = 3136
746 3136 sqrt add
Now this is an important part!
With Sqrt we only need a single value
3136 sqrt = 56
746 56 add
Last Step 746 56 add = 802
The answer.




Ways About This
So what I'm thinking is having two lists
One with the numbers, the left side
And the other with the operators.
So for example at the start
70 11 mul 5 div 219 add 28 26 6 sub 6 sub div mul 448 7 mul sqrt add

nums = 70,11
ops = mul
Next step
nums = 770,5
ops = div


"""

import math







s = input().split()
operatorNames = ['mul','div','add','sub','mod','sqrt']

nums = []
ops = []
total = 0
for i in range(0,len(s)):
    x = s[i]
    # Inital Setup
    if x not in operatorNames:
        nums.append(int(x))
    else:
        ops.append(x)

    if len(ops)==0:
        pass
    elif ops[0] == 'sqrt':
        total = math.sqrt(nums[-1])
        ops = ops[1:]
        nums = nums[:-1]
        nums.append(total)
    elif ops[0] == 'add':
        total = nums[-1]+nums[-2]
        ops = ops[1:]
        nums = nums[:-2]
        nums.append(total)
    elif ops[0] == 'sub':
        total = nums[-2]-nums[-1]
        ops = ops[1:]
        nums = nums[:-2]
        nums.append(total)
    elif ops[0] == 'mul':
        total = (nums[-1])*(nums[-2])
        ops = ops[1:]
        nums = nums[:-2]
        nums.append(total)
    elif ops[0] == 'div':
        total = (nums[-2])/(nums[-1])
        ops = ops[1:]
        nums = nums[:-2]
        nums.append(total)
    elif ops[0] == 'mod':
        total = (nums[-2])%(nums[-1])
        ops = ops[1:]
        nums = nums[:-2]
        nums.append(total)
    print(nums,ops)


print(int(nums[0]))









