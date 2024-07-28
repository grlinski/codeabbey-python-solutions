


# Cards Shuffling
# https://www.codeabbey.com/index/task_view/cards-shuffling


def cardCreator():
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    suits = ['C', 'D', 'H', 'S']

    cards = []


    for i in suits:
        for j in ranks:
            x = i+j
            cards.append(x)

    return(cards)


cards = cardCreator()

s = list(map(int, input().strip().split(' ')))
ans = []

print(len(s))

for i in range(0,len(s)):

    x = s[i]

    if x >51:
        x = x%52

    # Swapping

    card1 = cards[i]
    card2 = cards[x]
    #print(card1,card2,i,x)

    cards[x] = card1
    cards[i] = card2

    #print(cards)


for i in cards:
    print(i,end=' ')








