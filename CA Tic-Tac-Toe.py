
# http://www.codeabbey.com/index/task_view/tic-tac-toe
# Sloppy but works


number_of_items = int(input())
list_of_items = []

# Reads in input
for i in range(0,number_of_items):
    try:
        x = input()
    except:
        break
    list_of_items.append(x)

list_of_plays = []

for i in list_of_items:
    plays = []
    for j in range(0,len(i),2):
        x = int(i[j])
        plays.append(x)
    list_of_plays.append(plays)


# Pain in the ass but everyhing is in my list of lists
# Which is list of plays

winners = []

for i in list_of_plays:
    # Wins
    # Player 1
    p1 = [1, 2, 3]
    p2 = [4, 5, 6]
    p3 = [7, 8, 9]
    p4 = [1, 4, 7]
    p5 = [2, 5, 8]
    p6 = [3, 6, 9]
    p7 = [1, 5, 9]
    p8 = [3, 5, 7]
    # Player 2
    q1 = [1, 2, 3]
    q2 = [4, 5, 6]
    q3 = [7, 8, 9]
    q4 = [1, 4, 7]
    q5 = [2, 5, 8]
    q6 = [3, 6, 9]
    q7 = [1, 5, 9]
    q8 = [3, 5, 7]

    player_turn = 1

    # Here's where everything is done
    for j in range(0,len(i)):
        x = i[j]

        # This removes the current play/value from the win conditions for the current player
        if player_turn == 1:
            if x in p1:
                p1.remove(x)
            if x in p2:
                p2.remove(x)
            if x in p3:
                p3.remove(x)
            if x in p4:
                p4.remove(x)
            if x in p5:
                p5.remove(x)
            if x in p6:
                p6.remove(x)
            if x in p7:
                p7.remove(x)
            if x in p8:
                p8.remove(x)

        if player_turn == 2:
            if x in q1:
                q1.remove(x)
            if x in q2:
                q2.remove(x)
            if x in q3:
                q3.remove(x)
            if x in q4:
                q4.remove(x)
            if x in q5:
                q5.remove(x)
            if x in q6:
                q6.remove(x)
            if x in q7:
                q7.remove(x)
            if x in q8:
                q8.remove(x)

        if len(p1) == 0 or len(p2) == 0 or len(p3) == 0 or len(p4) == 0 or len(p5) == 0 or len(p6) == 0 or len(
                p7) == 0 or len(p8) == 0:
            winners.append(j+1)
            break
        if len(q1) == 0 or len(q2) == 0 or len(q3) == 0 or len(q4) == 0 or len(q5) == 0 or len(q6) == 0 or len(
                q7) == 0 or len(q8) == 0:
            winners.append(j+1)
            break

        if player_turn == 1:
            player_turn = 2
        else:
            player_turn = 1
        if j == 8:
            winners.append(0)




for i in winners:
    print(i, end =" ")

"""

Winning Combinations
Across
123
456
789
Down
147
258
369
Diag
159
357

p1a1 = [1,2,3]
p1a2 = [4,5,6]
p1a3 = [7,8,9]
p1d1 = [1,4,7]
p1d2 = [2,5,8]
p1d3 = [3,6,9]
p1g1 = [1,5,9]
p1g2 = [3,5,7]

p2a1 = [1,2,3]
p2a2 = [4,5,6]
p2a3 = [7,8,9]
p2d1 = [1,4,7]
p2d2 = [2,5,8]
p2d3 = [3,6,9]
p2g1 = [1,5,9]
p2g2 = [3,5,7]










"""













