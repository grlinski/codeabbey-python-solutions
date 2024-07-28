# 65 238 236 225 46
# Need to remove all inital binary numbers with odd amounts of 1s
# 1 2 4 8
# 16 32 64 128
"""
a = 97
z = 122
A = 65
Z = 90
0 = 48
9 = 57
" " = 32
. = 46

"""

originalinput = input()
counter = 0
endvalue = len(originalinput)
string1 = ""
lister = []
x = 0

# Putting Everything into a list
for i in originalinput:
    if i == " ":
        x = int(string1)
        lister.append(x)
        string1 = ""
    else:
        string1 = string1+i
#lister.append(".")
print(lister)

for i in lister:
    if (i > 64 and i < 91) or (i > 96 and i < 123) or (i > 47 and i < 58) or (i==32 or i ==46):
        print (chr(i))
    else:
        i = i-128
        print(chr(i))

















