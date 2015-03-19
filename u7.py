def findPrime(x=10001):
    count = 2
    term = 4
    candidate = 1
    while count < x:
        candidate += term
        term = 2 if term is 4 else 4
        if isPrime(candidate):
            count += 1
    return candidate


def isPrime(n):
    if n % 3 == 0:
        return False
    for p in range(5, int(n**0.5) + 1, 6):
        if n % p == 0 or n % (p + 2) == 0:
            return False
    return True


print(findPrime())
