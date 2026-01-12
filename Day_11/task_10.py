# Original list of tuples
data = (1, 2 , 3, 4 ,5 , 6 )
print("Original:", data)
data = tuple(map(lambda t: t+2, data))
print("Modified:",data)
