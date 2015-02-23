import timeit
NUMBER_TO_CHECK = 600851475143
BIG_PRIME = 59604644783353249


def prime1(n=NUMBER_TO_CHECK, p=3):
    while n % 2 == 0:
        n /= 2
    if n == 1:
        return 2
    while True:
        if p*p > n:
            return p if n == 1 else n
        elif n % p == 0:
            n /= p
        else:
            p += 2


def prime2(n=NUMBER_TO_CHECK, p=3):
    while n % 2 == 0:
        n /= 2
    if n == 1:
        return 2
    while not p*p > n:
        if n % p == 0:
            n /= p
        else:
            p += 2
    return p if n == 1 else n


time1 = timeit.timeit(prime1, number=20000)
print("P1:", time1)
time2 = timeit.timeit(prime2, number=20000)
print("P2:", time2)
print("P1/P2:", time1/time2)
