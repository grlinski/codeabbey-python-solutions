


# Parity Control
# http://www.codeabbey.com/index/task_view/parity-control



def decode(x):


    bib = bin(x)
    y = str(bib)
    y = y[2:]


    length = len(y)
    rem = 8-length
    y = '0'*rem+y

    # Here's What to Do
    # If the first number is 1, remove it and count the other 1's
    # If there are an even number the item is corrupted, remove it
    # Else if the first number is 0, count the number of 1's

    count = 0
    if y[0] == '1':
        y = y[1:]
        for i in y:
            if i == '1':
                count+=1
        if count%2==0:
            print('ab',y)
            return None
        else:

            return y

    y = y[1:]

    return y





s = list(map(int, input().strip().split(' ')))
#s = [65, 238, 236, 225, 46]



print(s)
ns = ''
for i in s:
    r = decode(i)
    try:
        num = int(r,2)
        ns = ns+chr(num)
        print(chr(num))
    except:
        pass



print(ns)














