def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line
for i in read_large_file('large_file.txt'):
    print(i)
