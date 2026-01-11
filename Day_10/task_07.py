def cache(func):
    dict = {4:16}
    def wrap(n):
        if n in dict:
            return dict[n]
        dict[n] = func(n)
        return dict[n]
    return wrap

@cache
def square(n):
    print("Calculating...")
    return n*n

print(square(4))
