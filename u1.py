def rek(n=999):
    return n if n == 3 else n + rek(n - 1) if (n % 5 == 0 or n % 3 == 0) else rek(n - 1)


def summa(a, n=999):
    p = n / a
    return a * (p * (p + 1)) / 2

print(int(summa(a=3) + summa(a=5) - summa(a=15)))
