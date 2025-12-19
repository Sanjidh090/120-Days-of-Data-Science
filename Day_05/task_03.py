
letter_dict = {}
text = "Banana"
for i in text:
    if i in letter_dict:
        letter_dict[i] += 1
    else:
        letter_dict[i] = 1
print(letter_dict)