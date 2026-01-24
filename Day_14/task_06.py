x = [1,2,3,4,5,6,6,7,1,8,9,9,10]
y = []
for v in x:
    if v not in y:
        y.append(v)   
print(y)
