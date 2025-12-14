x = 3666
hours = x // 3600
minutes = (x % 3600) // 60
seconds = x % 60
print(f"{hours} hours:{minutes} minutes:{seconds} seconds")