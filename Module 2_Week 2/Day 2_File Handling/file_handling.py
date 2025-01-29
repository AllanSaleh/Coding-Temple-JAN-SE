import re
# file = open('new_file.txt', 'w')
# file.write('Atomic Habits\n')
# file.write("Red Rising")
# file.close()

# a => append
# w => write
# r => read

# .read()
# .readlines()

# with open('new_file.txt', 'r') as file:
#     # print(file.readlines())
#     for line in file.readlines():
#         print(line.strip())
    # print(type(file)

with open('new_file.txt', 'a') as file:
    file.write('Project Hail Mary\n')

with open('new_file.txt', 'w') as file:
    file.write("Expeditionary Force\n")
    file.write("Spec Ops\n")

library = [
    "Red Rising",
    "Dungeon Crawler Carl",
    "Expeditionary Force",
    "Hail Mary",
    "Lord of the Rings",
    "Atomic Habits"
]

# with open('library.txt', 'a') as file:
#     for book in library:
#         file.write(f"{book}\n")

# with open('library.txt', 'r') as file:
#     for line in file:
#         print(line.strip())

read_library = []

with open('library.txt', 'r') as file:
    for line in file:
        read_library.append(line.strip())

print(read_library)

library_dict = {
    "Pierce Brown": "Red Rising",
    "Matt Dinniman": "Dungeon Crawler Carl",
    "Craig Alanson": "Expeditionary Force",
    "Andy Weir": "Hail Mary",
    "Tolkein": "Lord of the Rings",
    "James Clear": "Atomic Habits",
}

with open('library.txt', 'w') as file:
    for author, book in library_dict.items():
        file.write(f"{author} | {book}\n")

library_dict = {}

with open('library.txt', 'r') as file:
    for line in file:
        my_author = line.strip().split("|")
        # print(my_author, type(my_author))
        library_dict[my_author[0].strip()] = my_author[1].strip()
        # {key: value}
        # print(f"{my_author[0].strip()} {my_author[1].strip()}")
# print(library_dict)

library_nested_dict = {
    "Pierce Brown":{"Red Rising": 350},
    "Matt Dinniman": {"Dungeon Crawler Carl": 400},
    "Craig Alanson": {"Expeditionary Force": 400},
    "Andy Weir": {"Hail Mary": 290},
    "Tolkein": {"Lord of the Rings": 500},
    "James Clear": {"Atomic Habits": 200}
}

with open('library.txt', 'w') as file:
    for author, book in library_nested_dict.items():
        for book_name, pages in book.items():
            file.write(f"{author} | {book_name} | {pages}\n")

library_dict = {}

with open('library.txt', 'r') as file:
    for line in file:
        my_author = line.split(" | ")
        # print(my_author[2])
        library_dict[my_author[0]] = {my_author[1]: my_author[2].strip()}
# print(library_dict)

with open('library.txt', 'r') as file:
    contents = file.read()
    names = re.findall(r'[0-9]+', contents)
    print(names)
    # print(contents)