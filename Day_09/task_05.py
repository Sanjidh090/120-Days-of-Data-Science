def gen():
    for i in range(2):
        yield i + 2
g = gen()
for _ in range(2):
    print(next(g))

# if we given 3 in range then it will produce stopiteration
