import random, time
s = [random.randint(1, 100) for x in range(100000)]

start = time.time()
lc = [x for x in s if x % 3 == 0]
end = time.time()
print(f"List comprehension took {end - start:.6f} seconds.")
start = time.time()
lm = map(lambda x: x if x % 3 == 0 else None, s)
end = time.time()
print(f"Map with lambda took {end - start:.6f} seconds.")