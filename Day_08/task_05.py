s = ""
chars = "aa"
for i in range(10000):
    s = s.join(chars)
    if i % 1000 == 0:  # Print every 1000 iterations for brevity
        print(f"Iteration {i}, ID {id(s)}")
print(s)
