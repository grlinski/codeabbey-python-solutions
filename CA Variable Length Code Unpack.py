

# Variable Length Code Unpack
# https://www.codeabbey.com/index/task_view/variable-length-code-unpack
"""
https://en.wikipedia.org/wiki/Base32


"""
binSequences = ['11', '101',
'1001', '10001',
 '10000','011',
 '0101', '01001',
'01000', '0011',
 '00101', '001001',
 '001000', '00011',
 '000101', '000100',
'000011', '0000101',
 '0000100', '0000011',
 '0000010', '0000001',
 '00000001', '000000001',
 '0000000001', '00000000001',
 '000000000001', '000000000000']


dNum2Let = {'11': ' ', '101': 'e', '1001': 't', '10001': 'o', '10000': 'n', '011': 'a', '0101': 's', '01001': 'i',
       '01000': 'r', '0011': 'h', '00101': 'd', '001001': 'l', '001000': '!', '00011': 'u', '000101': 'c',
       '000100': 'f', '000011': 'm', '0000101': 'p', '0000100': 'g', '0000011': 'w', '0000010': 'b',
       '0000001': 'y', '00000001': 'v', '000000001': 'j', '0000000001': 'k', '00000000001': 'x',
       '000000000001': 'q', '000000000000': 'z'}






def convertToBinary(seq):
    binSeq = []
    letters = '0123456789ABCDEFGHIJKLMNOPQRSTUV'
    ans = []
    string1 = ''
    for i in seq:
        index = letters.find(i)
        binNum = bin(index)
        x = binNum[2:]
        if len(x) < 5:
            zeroes = 5-(len(x))
            for j in range(zeroes):
                x = '0'+x
        string1 = string1+x
    return string1



def convertToLetter(string1,binSequences,dNum2Let):

    sequence = ''
    ans = ''
    for i in range(0,len(string1)):

        sequence+=string1[i]
        #print(sequence)
        if sequence in binSequences:
            #print(dNum2Let[sequence])
            ans+=dNum2Let[sequence]
            sequence = ''
    print(ans)







seq = input()
#print(len(seq))
#converToBinary(seq)



x = convertToBinary(seq)
convertToLetter(x,binSequences,dNum2Let)



