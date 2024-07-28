

#  Variable Length Code
# https://www.codeabbey.com/index/task_view/variable-length-code

"""
Ending Notes
This was pretty easy except for again one minor problem, the end of the string
Nothing much more to note.
Maybe know how to do conversion between bin,hex,int better.







"""




"""
There is likely a problem with the very end of the string1
Maybe not enough zeroes or too many.
No idea why this is
Maybe add zeroes directly later on.




"""





dLet2Num = {' ': '11','e': '101',
't': '1001', 'o': '10001',
'n': '10000','a': '011',
's': '0101','i': '01001',
'r': '01000','h': '0011',
'd': '00101','l': '001001',
'!': '001000','u': '00011',
'c': '000101','f': '000100',
'm': '000011','p': '0000101',
'g': '0000100','w': '0000011',
'b': '0000010','y': '0000001',
'v': '00000001','j': '000000001',
'k': '0000000001','x': '00000000001',
'q': '000000000001','z': '000000000000'}


dNum2Let = {'11': ' ', '101': 'e', '1001': 't', '10001': 'o', '10000': 'n', '011': 'a', '0101': 's', '01001': 'i',
       '01000': 'r', '0011': 'h', '00101': 'd', '001001': 'l', '001000': '!', '00011': 'u', '000101': 'c',
       '000100': 'f', '000011': 'm', '0000101': 'p', '0000100': 'g', '0000011': 'w', '0000010': 'b',
       '0000001': 'y', '00000001': 'v', '000000001': 'j', '0000000001': 'k', '00000000001': 'x',
       '000000000001': 'q', '000000000000': 'z'}


def lettersToNumberSquence(string1,dLet2Num):
    ans = ''

    for i in string1:
        ans+=dLet2Num[i]
    return ans


def addZeroes(string1):
    leng = len(string1)
    zeroes = leng%8

    #print('Length,Zeroes')
    #print(string1)
    #print(leng,zeroes)

    for i in range(zeroes):
        string1+='0'


    return string1


def convertToHex(string1):

    hexes = []
    ans = []
    for i in range(0,len(string1),8):
        x = string1[i:i+8]
        hexes.append(x)

    for i in hexes:
        if len(i) < 8:
            leng = len(i)
            zeroes = 8-leng
            for j in range(zeroes):
                i+='0'
        y = int(i, 2)
        z = hex(y)
        ans.append(z)

    return ans


def convertHexToPrintableForm(hexes):
    ans = []
    lower = 'abcdefghijklmnopqrstuvwxyz'


    for i in hexes:
        y = i[2:]
        if len(y)==1:
            y='0'+y
        x =''
        for j in y:
            if j in lower:
                up = j.upper()
                x+=up
            else:
                x+=str(j)
        ans.append(x)
    return ans








def flowControl(string1,dLet2Num):
    string1 = lettersToNumberSquence(string1,dLet2Num)
    string1 = addZeroes(string1)
    ans = convertToHex(string1)
    ans = convertHexToPrintableForm(ans)
    if ans[-1] == '00':
        ans = ans[:-1]
    for i in range(0,len(ans)):
        print(ans[i],end=' ')


string1 = input()
flowControl(string1,dLet2Num)
#print(lettersToNumberSquence(string1,dLet2Num))











