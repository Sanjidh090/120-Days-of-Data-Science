def gen():
        yield 6
def gen1():
    yield 7
def combined_gen():
    yield from gen() 
    yield from gen1()

for i in combined_gen():
    print(i)
