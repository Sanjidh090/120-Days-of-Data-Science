def decor(func):
    def inner(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return inner

@decor
def add(a, b):
    return a + b

result = add(3, 4)
print("Result:", result)
