import time
list = [i for i in range(-50000000, 5000000)]
def insertion_trap(position,element):
    start = time.time()
    list.insert(position, element)
    end = time.time()
    time_list = end - start
    print(f"Timw taken {time_list:.6f} seconds for insert")

    start = time.time()
    list.append(element)
    end = time.time()
    time_append = end - start
    print(f"Time taken {time_append:.6f} seconds for append")

insertion_trap(0, -5)
