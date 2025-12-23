import time
list = [i for i in range(-5000000, 5000000)]   
start = time.perf_counter()
for i in range(len(list)):
    if list[i] == -5:
        print(f" -5 found at index {i}")
        break
end = time.perf_counter()
elapsed = end - start
print(f"Execution time for search elapsed: {elapsed:.4f} seconds")