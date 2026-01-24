x = [1,2,3,4,5,6,7,8,9,10,11,12,14,15,16,17,18,19]
y = len(x) + 1
sums = (y)*(y + 1)//2
rest = sums - sum(x)
print(rest)