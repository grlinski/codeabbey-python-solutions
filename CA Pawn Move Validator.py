
# CA Pawn Move Validator
# https://www.codeabbey.com/index/task_view/pawn-move-validator

"""

Completed
End Notes
This is another program that didn't take too long
When things are annoying just change them so they fit my specs
Example this board goes in a weird order and has letters
So it is easiest to convert to normal standards.




White in Uppercase at Bottom
Black in Lowercase at Top

  +-----------------+
8 | r n b q k b n r |
7 | p p p p p p p p |
6 | - - - - - - - - |
5 | - - - - - - - - |
4 | - - - - - - - - |
3 | - - - - - - - - |
2 | P P P P P P P P |
1 | R N B Q K B N R |
  +-----------------+
    a b c d e f g h








"""




def boardSetup():
    b = [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]

    return b

def printBoard(b):
    for i in b:
        print(i)



def startEndCheck(sR,sC,eR,eC,b):
    piecesW = ['p', 'r', 'n', 'b', 'k', 'q']
    piecesB = ['P', 'R', 'N', 'B', 'K', 'Q']

    startP = b[sR][sC]
    endP = b[eR][eC]
    if endP == '-':
        return True
    elif startP in piecesW and endP in piecesW:
        return False
    elif startP in piecesB and endP in piecesB:
        return False
    return True



# PAWN MOVEMENT
# Unless I'm missing something, looks good.
def movePawn(sR,sC,eR,eC,b):
    # What can a pawn do?
    # Well it can move two, only if it starts on row 7 or 2
    # Otherwise it moves one space forward.
    # So check that first, if it moves 1 or 2 steps.
    # Also if the column changes there needs to be a piece to its diagonal



    # One Problem I get is Pawns Moving Backwards.
    # p moves increase
    # P moves decrease

    # CHECK IF PAWNS MOVE BACKWARDS
    x = b[sR][sC]
    if x =='p':
        if eR < sR:
            return b,False
    elif x == 'P':
        if eR > sR:
            return b,False



    # One Movement Forward
    if abs(sR-eR) == 1 and sC == eC:
        if b[eR][eC] == '-':
            b[eR][eC] = b[sR][sC]
            b[sR][sC] = '-'
            return b, True
    # Two Moves Forward
    elif abs(sR-eR) == 2 and sC ==eC and (sR == 1 or sR == 6):
        betweenRow = int(sR+eR)//2
        if b[eR][eC] == '-' and b[betweenRow][eC] =='-':
            b[eR][eC] = b[sR][sC]
            b[sR][sC] = '-'
            return b,True
    # Diagonal One Move Forward
    elif abs(sR-eR) ==1 and abs(sC-eC) == 1 and b[eR][eC] != '-':
        print('here')
        if b[eR][eC] != '-':
            b[eR][eC] = b[sR][sC]
            b[sR][sC] = '-'
            return b, True

    return b, False



# KNIGHT MOVEMENT N
def moveKnight(sR,sC,eR,eC,b):



    # Should be easy.
    """
    Valid moves as long as movement is 2 one way and 1 the other
    Doesn't matter if space is empty or not.


    """
    #print(sR,eR,sC,eC)
    rowM = abs(sR-eR)
    colM = abs(sC-eC)

    # Check if End Spot is Same Colour as Start Piece.



    if rowM == 1 and colM == 2:
        b[eR][eC] = b[sR][sC]
        b[sR][sC] = '-'

        return b, True
    elif rowM == 2 and colM == 1:

        b[eR][eC] = b[sR][sC]
        b[sR][sC] = '-'
        return b, True

    return b,False



# BISHOP MOVEMENT
def moveBishop(sR,sC,eR,eC,b):

    if abs(sR-eR)!=abs(sC-eC):
        return b,False

    diff = abs(sR-eR)
    empty = True
    # Four Directions
    #UL to DR
    if sC < eC and sR < eR:
        for i in range(1,diff):
            if b[sR+i][sC+i]!='-':
                empty = False
    #DL UR
    elif sC < eC and sR > eR:
        for i in range(1,diff):
            if b[sR-i][sC+i]!='-':
                print(b[sR-i][sC+i])
                empty = False

    # DR to UL
    elif sC > eC and sR > eR:
        for i in range(1, diff):
            if b[sR - i][sC - i] != '-':
                print(b[sR - i][sC - i])
                empty = False
    #UR to DL
    elif  sC > eC and sR < eR:
        for i in range(1, diff):
            if b[sR + i][sC - i] != '-':
                print(b[sR + i][sC - i])
                empty = False


    if empty == False:
        return b,False
    else:
        b[eR][eC] = b[sR][sC]
        b[sR][sC] = '-'
        return b, True


def moveRook(sR,sC,eR,eC,b):
    # Is it moving UpDown or LR?

    # First Check move is legal at all
    if sR!=eR and sC!= eC:
        return b,False

    empty = True
    # UP DOWN Movement
    if sC == eC:
        diff = abs(sR-eR)
        mini = min(sR,eR)
        print(diff,mini)

        for i in range(mini+1,mini+diff):
            x = b[i][sC]
            if x!='-':
                empty = False
    elif sR == eR:
        diff = abs(sC-eC)
        mini = min(sC,eC)
        print(diff,mini)
        for i in range(mini+1,mini+diff):
            x = b[sR][i]
            if x!='-':
                empty = False

    if empty == False:
        return b,False
    else:
        b[eR][eC] = b[sR][sC]
        b[sR][sC] = '-'
        return b, True


def moveKing(sR,sC,eR,eC,b):
    # Check if Move is Legal

    rowCheck = abs(sR-eR)
    colCheck = abs(sC-eC)
    if rowCheck >1 or colCheck > 1:
        return b,False
    else:
        b[eR][eC] = b[sR][sC]
        b[sR][sC] = '-'
        return b, True

def moveQueen(sR,sC,eR,eC,b):

    goodMove = True

    # Is it moving diagonally?
    if abs(sR-eR) == abs(sC-eC):
        b,goodMove = moveBishop(sR,sC,eR,eC,b)
    else:
        b,goodMove = moveRook(sR,sC,eR,eC,b)

    return b,goodMove




def flowControl(q,b):

    dictCols = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
    counter = 1
    for i in q:
        # Note I need to Convert all Rows and Cols to py format
        sC = i[0]
        sR = int(i[1])
        eC = i[2]
        eR = int(i[3])
        # Conversions
        sR = 8-sR
        eR = 8-eR

        sC = dictCols[sC]
        eC = dictCols[eC]


        print(sR,sC,eR,eC)

        if startEndCheck(sR,sC,eR,eC,b):
            pass
        else:
            print('Failed Start End Check')
            return counter


        x = b[sR][sC].upper()
        # P R N B Q K
        if x == 'P':
            b,goodMove = movePawn(sR,sC,eR,eC,b)

        elif x == 'N':

            b,goodMove = moveKnight(sR,sC,eR,eC,b)

        elif x == 'B':
            b,goodMove = moveBishop(sR,sC,eR,eC,b)

        elif x == 'R':
            b,goodMove = moveRook(sR,sC,eR,eC,b)

        elif x == 'K':
            b,goodMove = moveKing(sR,sC,eR,eC,b)

        elif x == 'Q':
            b,goodMove = moveQueen(sR,sC,eR,eC,b)
        #printBoard(b)

        if goodMove == False:
            return counter
        counter+=1
    return 0


cases = int(input())
ans = []
for i in range(cases):
    q = input().split(' ')
    b = boardSetup()
    x = flowControl(q,b)
    ans.append(x)

for i in ans:
    print(i,end=' ')




"""

Problems


2
b1c3 b8c6 b2b4 b7b8
b2b4 b7b5 b4b3 b5b6


Should be 4,3
I get 0,0


"""