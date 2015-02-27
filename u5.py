import math


def addSpanNaturals(nbr=20):
    product = 1
    limit = nbr**0.5
    for i in range(2, nbr):
        if isPrime(i):
            e = 1 if i > limit else int(math.log(nbr)/math.log(i))
            product *= i**e
    return product


def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    p = 3
    limit = n**0.5
    while not p > limit:
        if n % p == 0:
            return False
        else:
            p += 2
    return True

print(addSpanNaturals())
