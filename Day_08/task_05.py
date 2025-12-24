def stringbuild(n):
    chars = []
    for i in range(n):
        chars.append("c")
        if i % 1000 == 0:
            print(f"Iteration {i}, list ID: {id(chars)}")
    s = "".join(chars)      
    print("Final string ID:", id(s))
    return s
s = stringbuild(10000)
print("Final string:", s)
