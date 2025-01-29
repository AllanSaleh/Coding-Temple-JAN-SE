library = []
file_location = 'library.txt'
def read_file(loc, arr):
    with open(loc, 'r') as file:
        for line in file:
            arr.append(line.strip())
    return arr

read_file('library.txt', library)
read_file('new_file.txt', library)
print(library)