def running_average():
    total = 0
    count = 0
    avg = 0
    while True:
        new_value = yield avg
        
        if new_value is None:
            continue
            
        total += new_value
        count += 1
        avg = total / count
        print(f"Added {new_value}: Running Average = {avg}")

c = running_average()
next(c)      # Returns 0 (initial avg)
print(f"Result: {c.send(10)}")  # Returns 10.0
print(f"Result: {c.send(20)}")  # Returns 15.0
print(f"Result: {c.send(30)}")  # Returns 20.0
print(f"Result: {c.send(40)}")  # Returns 25.0
print(f"Result: {c.send(50)}")  # Returns 30.0
print(f"Result: {c.send(None)}")  # Returns 30.0 (no change)
