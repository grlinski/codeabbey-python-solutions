

cards = ['CA' ,'C2' ,'C3' ,'C4' ,'C5' ,'C6' ,'C7' ,'C8' ,'C9' ,'CT' ,'CJ' ,'CQ' ,'CK' ,
         'DA', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'DT', 'DJ', 'DQ', 'DK',
         'HA' ,'H2' ,'H3' ,'H4' ,'H5' ,'H6' ,'H7' ,'H8' ,'H9' ,'HT' ,'HJ' ,'HQ' ,'HK' ,
         'SA' ,'S2' ,'S3' ,'S4' ,'S5' ,'S6' ,'S7' ,'S8' ,'S9' ,'ST' ,'SJ' ,'SQ' ,'SK']




x = list(map(int, input().strip().split(' ')))


c2 = cards
ori = 0

for i in x:
    if i >51:
        i = i%52

    holder = c2[i]
    c2[i] = c2[ori]
    c2[ori] = holder

    print(ori,i)

    print(c2[i],c2[ori])



    ori+=1

print(c2)





















