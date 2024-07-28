# 65 238 236 225 46
# Need to remove all inital binary numbers with odd amounts of 1s


originalinput = input()
counter = 0
endvalue = len(originalinput)
string1 = ""
lister = []

# Putting Everything into a list
for i in originalinput:
    if i == " ":
        lister.append(string1)
        string1 = ""
    else:
        string1 = string1+i
#lister.append(".")
print(lister)

binarylist = []

#Creating a Binary List
for i in lister:
    x = int(i)
    z = bin(x)
    binarylist.append(z)

string3 = ""
string4 = ""
gbinarylist = []


rbinarylist = []

#If = Len == 10 and has odd amount of zeroes.
for i in binarylist:
    if len(i) == 10:
        string3 = i[3:]
        string4 = i[:2] + i[3:]
        x = 0
        for j in string3:
            x = int(j)+x

        if x%2 == 0:
            rbinarylist.append(i)
            print(x)
    else:
        rbinarylist.append(i)

print(rbinarylist)


#Removes Top 1
for i in binarylist:
    if len(i) == 10:
        string3 = i
        string4 = string3[:2] + string3[3:]
        gbinarylist.append(string4)
    else:
        gbinarylist.append(i)

print(binarylist)
print(gbinarylist)








clist = []
for i in gbinarylist:
    x = int(i,2)
    clist.append(chr(x))

#print(gbinarylist)
cstring = ""
for i in clist:
    cstring= cstring+i
    #print (i, "")


print (cstring)








