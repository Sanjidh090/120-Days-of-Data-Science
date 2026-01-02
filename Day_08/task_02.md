# Task 02
This code here is to cover The ```hash lookup``` problem. Python runs ```hash (-5)```,
gets a memory address, and looks directly at that slot. It never scans the other items.
```Complexity: O(1)```. Constant time, regardless of data size.
<br>
Here, the list is converted to a set .
```python
list = [i for i in range(-50000000, 5000000)]
my_set = set(list)
```

then, we run a loop and see if -5  in there ,it it's there,,we get the position by ```time.time()``` method
Here is the code for loop.
```python
for i in range(len(my_set)):
    if -5 in my_set:
        print(f" -5 found in the set")
        break
```
