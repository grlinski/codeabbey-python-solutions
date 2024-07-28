
# Primes Ranges
# http://www.codeabbey.com/index/task_view/prime-ranges


import math,datetime

def prime_number_gen(maxi):
    list_of_primes = [2,3,5]
    # 2 and 3 added since they are a pain in the ass
    counter = 3
    number = 7
    prime = True
    # Main Loop for Prime Gen
    # Goes until our counter of primes hits items
    while number <= maxi:

        prime = True
        # Quick check if prime
        # The number has to be either 6n+1 or 6n-1,
        # Note I had a problem before with using or instead of and.
        # It only needs to be one or the other, not nessicarily both.
        if (number+1)%6 != 0 and (number-1)%6 != 0:
            prime = False

        elif number % 2 == 0 or number % 3 == 0 or number % 5 == 0:
            prime = False
            # If all those fail check if it is divisible by any of the primes in the list
        else:
            # If the potential divisor is greater than the square root of the number it ends
            # This is one of the most important parts
            # Makes it much more efficient
            upto = int(math.sqrt(number))
            for i in range(2,len(list_of_primes)):
                if i > upto:
                    break
                if number%list_of_primes[i] == 0:
                    prime = False
                    break
        if prime == True:
            list_of_primes.append(number)
            counter += 1
            if len(list_of_primes)%10000 == 0:
                pass


        number+=1
    return list_of_primes






times = int(input())
items = []

startime = datetime.datetime.now()
while times !=0:
    x,y = input().split()
    bottom = int(x)
    top = int(y)
    items.append(bottom)
    items.append(top)


    times-=1
maximum = max(items)
minimum = min(items)

prime_list = prime_number_gen(maximum)
print(minimum, maximum)

range_list = []
for j in range(0,len(items),2):
    bottom = items[j]
    top = items[j+1]
    count=0
    for k in prime_list:
        if k == bottom:
            print("Start ",k)
        if k >= bottom:
            count+=1
        if k == top:
            print("End ",k)
            break
    range_list.append(count)


for i in range_list:
    print(i,end=" ")

#for i in prime_list:
#    print(i)

endtime = datetime.datetime.now()
print()
print("Elapsed: ", (endtime-startime))
#print(prime_list)



"""

3
2016361 2571733
2629223 2723363
1376317 1604737


"""





