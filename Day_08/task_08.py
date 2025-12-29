import random
a = [random.randint(0, 100) for _ in range(51)]
b = [random.randint(0, 100) for _ in range(51)]

def match_lists(a =[], b = []):
    match = []
    count = 0
    for i in range(len(a)):
        for j in range(len(b)):
            count += 1
            if a[i] == b[j]:
                match.append(a[i])
    print(match)   
    print(set(match))         
    print(f"Number of matching elements: {len(match)}") 
    print(f"Total comparisons made: {count}") 

match_lists(a, b)
