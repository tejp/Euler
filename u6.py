limit = 100
sums = limit * (limit + 1) / 2
sumOfSquares = (2 * limit + 1) * (limit + 1) * limit / 6
print(int(sums**2 - sumOfSquares))
