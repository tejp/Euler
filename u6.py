def difference(limit=100):
    squareOfSums = limit * (limit + 1) / 2
    sumOfSquares = (2 * limit + 1) * (limit + 1) * limit / 6
    return int(squareOfSums**2 - sumOfSquares)

print(difference())
