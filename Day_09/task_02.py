import sys
x = [ i for i in range(10**6) ]
print(sys.getsizeof(x))

def gen():
    for i in range(10**6):
        yield i
print(sys.getsizeof(gen()))

# 8448728
# 104
# The prize goes to generator
