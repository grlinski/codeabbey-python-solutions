# Completed
# Note that my prime list could be way lower like 1000 max



# http://www.codeabbey.com/index/task_view/integer-factorization
# Integer Factorization

times = int(input())

# This creates a list of prime numbers to divide by.
# Makes further calculations easier
# Creates a list up to the number of items we supply
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
        if number % 2 == 0 or number % 3 == 0 or number % 5 == 0:
            prime = False
            # If that passes this checks every number under half of the number
        else:
            upto = int((number - 1) / 2)
            for i in range(2,upto):
                if number%i == 0:
                    prime = False
                    break
        if prime == True:
            list_of_primes.append(number)
            counter+=1


        number+=1
    return list_of_primes


primes = (prime_number_gen(10000))

print("Done")
answers = []

for i in range(0,times):
    x = int(input().strip())
    factors = []
    total = x
    counter = 0
    while total != 1:
        div = primes[counter]
        if total%div == 0:
            total = total/div
            factors.append(div)

        else:
            counter+=1
    holder = ""
    answer = ""
    for j in factors:
        holder = holder+str(j)+"*"
    answer = holder[:-1]
    answers.append(answer)



for q in answers:
    print(q,end=" ")












