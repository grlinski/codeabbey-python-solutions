
# http://www.codeabbey.com/index/task_view/prime-numbers-generation
import math


def prime_number_gen(items):
    list_of_primes = [2,3,5]
    # 2 and 3 added since they are a pain in the ass
    counter = 3
    number = 7
    prime = True
    # Main Loop for Prime Gen
    # Goes until our counter of primes hits items
    while counter != items:

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
            upto = int(math.sqrt(number))
            for i in range(2,len(list_of_primes)):
                if i > upto:
                    break
                if number%list_of_primes[i] == 0:
                    prime = False
                    break
        if prime == True:
            list_of_primes.append(number)
            if len(list_of_primes)%10000 == 0:
                print(counter)
            counter+=1


        number+=1
    return list_of_primes



items = int(input())

list1 = list(map(int, input().strip().split(' ')))
x = 0
print(list1)
for j in list1:
    x = max(x,j)

primes = (prime_number_gen(x))
for i in list1:
    print(primes[i-1], end = " ")
    #print(primes[q])











"""


2
7 1


 or ((number+1)%6 != 0 or (number-1)%6 != 0)

"""





