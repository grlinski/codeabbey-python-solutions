

# Sick Travellers
# https://www.codeabbey.com/index/task_view/sick-travellers

"""

Completed
Fairly simple despite its high rating
Just taking it step by step and keeping things simple makes life easy.







Right now all the info is contained in a single list of lists
No further depth, makes things too hard to deal with.
When cycling through the list of towns, start at index 3 to -1
Maybe change everything to lowercase, except for the town they are currently at.



List1 Info
Name, Status, Which City they are in Cities
Uppercase indicates city they are at.

print('asfasf'.islower())

print('ASfasadsa'.isupper())



Rules
3 Conditions
Healty Sick Recovering
If sick, moves to recovering the next day
If Recovering moves to healthy the next day
If healthy is same city with sick or recovering they become sick the next day.
Routes are cyclical

100 Days Pass
If 99 days are reached without total recovery output names of sick and recovering travellers
Otherwise if everyone becomes healthy
Print out the people from the previous day who were sick or recovering.








"""

# Should be able to check if there is a sick or recovering person in the same city
def checkIfSickInCity(nameX,cityX,curList):
    for person in curList:
        name = person[0]
        status = person[1]
        cityIndex = person[2]
        city = person[cityIndex+3]
        if name == nameX:
            pass
        else:
            if city==cityX:
                if status == 'sick' or status =='recovering':
                    return True
    return False



# Returns the names of Who is Currently Sick
def whoIsSick(list1):
    sick = []
    for person in list1:
        name = person[0]
        status = person[1]
        if status == 'sick' or status == 'recovering':
            sick.append(name)

    sick.sort()
    return sick




def nextDayList(curList):
    nextList = []

    for person in curList:
        name = person[0]
        status = person[1]
        cityIndex = person[2]
        city = person[cityIndex+3]
        totalCities = len(person)-3
        allCities = person[3:]
        #print(name,status,city,totalCities,cityIndex)

        # STATUS
        if status == 'sick':
            nextStatus = 'recovering'
        elif status == 'recovering':
            nextStatus = 'healthy'
        else:
            sickInCity = checkIfSickInCity(name,city,curList)
            if sickInCity == True:
                nextStatus = 'sick'
            else:
                nextStatus = 'healthy'

        # Next City
        nextCityIndex = cityIndex
        nextCityIndex+=1
        if nextCityIndex == totalCities:
            nextCityIndex = 0

        #next = person,nextStatus,nextCityIndex,curList[3:]
        next=  []
        next.append(name)
        next.append(nextStatus)
        next.append(nextCityIndex)
        for i in (allCities):
            next.append(i)

        nextList.append(next)

    return nextList


def flowControl(curList):

    for i in range(0,99):

        previouslySick = whoIsSick(curList)
        curList = nextDayList(curList)

        currentlySick = whoIsSick(curList)
        print(currentlySick)
        if len(currentlySick) == 0:
            print('All Cured at Day',i)
            return previouslySick,i

    return currentlySick,100







npeople = int(input())
list1 = []
for np in range(0,npeople):

    x,y,z = input().split(' ')
    q = [x,y,0]

    for i in range(0,len(z),4):
        zs = z[i:i + 3]
        if i == 0:
            pass
        else:
            pass
            zs = zs.lower()
        q.append(zs)
    list1.append(q)


for i in list1:
    print(i)

ansList,day = flowControl(list1)

for i in ansList:
    print(i,end=' ')
print(day)




