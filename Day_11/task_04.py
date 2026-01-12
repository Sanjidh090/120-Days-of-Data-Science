from functools import reduce
numbers = [1, 2, 3, 6]
product = reduce(lambda x, y: x * y, numbers)
print(product)  