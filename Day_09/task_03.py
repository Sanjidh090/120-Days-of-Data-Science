def fib_infinity(start = 0, acc = 0):
    yield start + acc
    yield from fib_infinity(acc, start + acc)

i = fib_infinity(start = 1, acc = 0)
for x in i:
    print(x, end = ' ')
    if x > 50000:
        break

