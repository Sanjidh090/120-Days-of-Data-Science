x = 10
def change_x():
    global x  # This will print 10
    x = 20
change_x()
print(x)  # This will print 20