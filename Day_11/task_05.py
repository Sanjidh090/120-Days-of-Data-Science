nist = ["100px" , "20px" , "3px"]
sorted_nist = sorted(nist, key=lambda x: int(x[:-2]))
print(sorted_nist)