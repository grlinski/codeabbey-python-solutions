

# Transitive Closure on Candy States
# https://www.codeabbey.com/index/task_view/transitive-closure-on-candy-states
"""
Completed



End Notes
I'm decently impressed with my solution.
Basically it originally takes the pairs and adds those to a dictionary.
At first it just has a key = state, and values are all those directly adjacent to the key.
After this a second dictionary is created
This dictionary is similar,the key is a state but the value is a list of lists.
The position in the list is the distance of the state to the key.

Now for some actual notes:
Maybe at some point I should go back and shore up the program
Add better names for variables
Better comments
As with most things, each function should do a clear concrete thing.
I should also have more functions, each well documented.

!!!
I should check out the
Floyd–Warshall algorithm






"""









"""
From the original dictionary create another dict that has further roads.
Have a list of all states.
Then find the actual distance, if possible between all states.
Example:
Cowsome ['Honepy', 'Bawnty', 'Mikliday'] 2 ['Maycorn' 'Lacry', 'Mausse'] 3 ['Lednec']


Look up how to create multiple dictionary entries.


"""



def basicList(statePairs):
    states = []
    dict = {}

    for i in statePairs:
        a = i[0]
        b = i[1]
        if a in states:
            pass
        else:
            states.append(a)

        if b in states:
            pass
        else:
            states.append(b)


        if a in dict:
            dict[a].append(b)
        else:
            dict[a] = [b]
        if b in dict:
            dict[b].append(a)
        else:
            dict[b] = [a]

    return dict,states



# Simple Function That Gets A List of States From a Dictionary Entry:
"""
Basically I enter a state name
It looks up all states adjacent to that one from the dict
And then looks up and returns all states adjacent to those ones.
"""
def getStates(x,dict):
    pool = []
    set1 = set()
    for i in x:
        for j in i:
            y = dict[j]
            for k in y:
                set1.add(k)
    pool = list(set1)
    return pool




# FULL WEB
"""
# This Takes in a dictionary that contains a key of a state with its adjacent states.
# And it takes in a list of all states.
Then it creates finalDict, which has a key of a state and a list of adjcent states.
The position within the list is how many roads away the state is.
If not in the entry, the states are not connected.


"""
def fullWeb(dict,states):

    # final Dictionary
    finalDict = {}
    # Just do First State Cowsome
    for s in states:
        #print('State',s)

        distances = [[0]]*len(states)
        alreadyMeasured = []
        distances[0] =dict[s]

        for am in distances[0]:
            alreadyMeasured.append(am)

        # Basically that More States Were Added to the Map, ie No dead ends.
        added = True
        d = 0
        while added == True:
            d+=1
            added = False


            pool = getStates([distances[d-1]],dict)

            newRoads = []
            for i in pool:


                if i in alreadyMeasured:
                    pass
                else:
                    added = True
                    newRoads.append(i)
                    alreadyMeasured.append(i)

            if added == True:
                distances[d] = newRoads


        finalDict[s] = distances


    #for i in finalDict:
    #    print(i,finalDict[i])
    return finalDict





def findDistance(start,end,fDict):

    counter = 1
    for i in fDict[start]:
        if i == 0:
            return 1000000
        else:
            if end in i:
                return counter
        counter+=1






"""
    Cowsome['Honepy', 'Bawnty', 'Mikliday'] 2['Maycorn' 'Lacry', 'Mausse']  3['Lednec']
"""

statePairsNumber = int(input())

statePairs = []
for i in range(statePairsNumber):
    a,b = input().split(' - ')
    x = [a,b]
    statePairs.append(x)



dict,states = basicList(statePairs)
finalDict = fullWeb(dict,states)

cases = int(input())
casePairs = []

printAns =[]

for i in range(cases):
    a,b = input().split(' - ')
    x = [a,b]
    casePairs.append(x)
    ans = findDistance(a,b,finalDict)
    printAns.append(ans)

#for i in dict:
#    print(i,dict[i])




for i in printAns:
    print(i,end=' ')







