import time
list = [i for i in range(-50000000, 5000000)]
my_set = set(list)
start = time.perf_counter()
for i in range(len(my_set)):
    if -5 in my_set:
        print(f" -5 found in the set")
        break
end = time.perf_counter()
elapsed = end - start   
print(f"Execution time for a set : {elapsed:.6f} seconds")