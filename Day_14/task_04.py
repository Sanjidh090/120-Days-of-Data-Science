unl = [1, [2, [3, 4]]]
def flatten(mylist):
    for i in mylist:
        if type(i) == list:
            yield from flatten(i)
        else:
            yield i
flat_list = list(flatten(unl))
print(flat_list)
