# http://www.codeabbey.com/index/task_view/king-and-queen



times = int(input())

answers = []

for i in range(0,(times)):
    check = False


    king, queen = input().split()

    holder = ord(king[0])
    holder = holder-96
    kx = int(holder)
    ky = int(king[1])


    holder = ord(queen[0])
    holder = holder-96
    qx = int(holder)
    qy = int(queen[1])

    #Same Row
    if qx == kx:
        check = True
    #Same Column
    if qy == ky:
        check = True
    #Check Diagonals
    diffx = abs(qx-kx)
    diffy = abs(qy-ky)
    if diffx == diffy:
        check = True




    if check == True:
        answers.append("Y")
    elif check == False:
        answers.append("N")





for i in answers:
    print(i,end= " ")







