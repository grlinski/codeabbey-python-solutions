
# http://www.codeabbey.com/index/task_view/variable-length-code

seq = input()


dict = {' ': '11','e': '101',
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



vlc = {'11': ' ', '101': 'e', '1001': 't', '10001': 'o', '10000': 'n', '011': 'a', '0101': 's', '01001': 'i',
       '01000': 'r', '0011': 'h', '00101': 'd', '001001': 'l', '001000': '!', '00011': 'u', '000101': 'c',
       '000100': 'f', '000011': 'm', '0000101': 'p', '0000100': 'g', '0000011': 'w', '0000010': 'b',
       '0000001': 'y', '00000001': 'v', '000000001': 'j', '0000000001': 'k', '00000000001': 'x',
       '000000000001': 'q', '000000000000': 'z'}





s = ''

for i in seq:
    s = s+dict[i]


# Get it to Divisible By Eight
eight = len(s)
rem = eight%8

number8 = 8-rem

if rem != 0:
    s = s+('0'*number8)
else:
    pass

# Split into 8s
q = []

for i in range(0,len(s),8):
    x = s[i:i+8]
    #x = '0b'+x
    y = str(hex(int(x, 2)))
    #z = str(y)

    r = y[2:].upper()
    q.append(r)


for i in q:
    if len(i) == 1:
        print('0'+i,end= " ")
    else:
        print(i,end=' ')















