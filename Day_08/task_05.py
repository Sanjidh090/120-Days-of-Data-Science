def string_builder(n):
    chars = []
    for i in range(n):
        chars.append("c")
        if i % 1000 == 0:
            print(f"Iteration {i}, list ID: {id(chars)}")
    s = "".join(chars)      
    print("Final string ID:", id(s))
    return s
if __name__ == "__main__": 
    s = string_builder(10000)
    print(f"Final string length: {len(s)}")
    print(f"First 50 characters: {s[:50]}...")
