# import timeit


def isPal(n):
    nbr = str(n)
    return nbr == nbr[::-1]


def getPal(i=999, p=False):
    highPal = -1
    lowFactor = int(i/10)
    while i > lowFactor:
        for j in range(i, lowFactor, -1):
            n = i*j
            if not n > highPal:
                break
            elif isPal(n):
                highPal, lowFactor = n, j
                if p:
                    print("{}*{} = {}".format(i, j, n))
                break
        i -= 1
    return highPal

getPal(p=True)
# print(timeit.timeit(getPal, number=1000))
