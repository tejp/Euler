def isPal(n):
    nbr = str(n)
    return nbr == nbr[::-1]


def getPal(i=999, p=False):
    highPal = -1
    lowFactor = int(i/10)
    while i > lowFactor:
        start = i if i % 11 == 0 else i-i % 11
        increment = -1 if i % 11 == 0 else -11
        for j in range(start, lowFactor, increment):
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
