def rek(a=1, b=2, boundary=4000000):
    return 0 if b >= boundary else b + rek(b, a + b) if (b % 2 == 0) else rek(b, a + b)


def rekBetter(a=2, b=8, boundary=4000000):
    return 2 if b >= boundary else b + rekBetter(b, a+4*b)

print(rekBetter())
