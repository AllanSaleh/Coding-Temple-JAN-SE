'''
Dictionaries: 
- Keys must be unique
- Keys must be immutable
- Values can be anything
- Dictionaries maintain insertion order
- Dictinoaries are mutable

'''
import pprint
# Creating a dictionary
empty_library = {}
other_library = dict()
library = {
    "Pierce Brown": "Red Rising",
    123456789: "Atomic Habits",
    123456789: "Atomic Habits 2: The return of the habits",
    ('Brandon', 'Sanderson'): "Way of Kings",
    # ['Matt', 'Dinniman']: "Dungeon Crawler Carl"
    # {'Matt', 'Dinniman'}: "Dungeon Crawler Carl"
    # {"Matt": "Dinniman"}: "Dungone Crawler Carl"
}
print(type(empty_library))
print(type(other_library))
print(type(library))
print(library)
# Accessing a value in a dictionary
print(library[123456789])

# Using the .get() to access a key/value in a dictionary
# print(library["Pierce Brow"])
print(library.get("Pierce Brow", "Key doesn't exist. Check spelling"))

# Adding, Modifying, and removing elements in a dictionary
    # Using .pop()
# library.update({"Craig Alanson": "ExFor"})
# library["Pierce Brown"] = "Exfor"
library["Craig Alanson"] = "Exfor"

print(library)
# del library["Craig Alanson"]
value = library.pop("Craig Alanson")
print(value)

# .keys(), .values(), .items()

print(library.keys())
print(library.values())
print(type(library.items()))

for author, book in library.items():
    print(author, book)

# Looping through dictionaries
    # Only looping through Keys
    # Only looping through values
    # Looping through key-value pairs

# Dictionaries within Dictionaries
library = {
    'Pierce Brown': {
        'Red Rising': 300,
        'Golden Son': 350,
        'Morning Star': 400
    },
    'Matt Dinniman': {
        "Dungeon Crawler Carl": 400,
        "Carl's Doomsday Scenario": 450
    }
}
print(library)
# pprint.pp(library)

# Accessing Nested Dictionaries
print(library["Pierce Brown"]["Red Rising"])
for books, pages in library["Pierce Brown"].items():
    print(books, pages)

# Modifying Nested Dictionaries
library["Pierce Brown"]["Red Rising"] = 800
print(library)
# Adding Nested Elements
# library["Craig Alanson"]["Exfor"] = 375 # Will throw error
library["Craig Alanson"] = {"Exfor": {"Pages": 200}}
print(library)

# Looping through nested dictionaries
for books, pages in library["Pierce Brown"].items():
    print(books, pages)
# List of Dictionaries
library = [{"Pierce Brown": "Red Rising"}, {"Matt Dinniman": "Dungeon Crawler Carl"}]
print(library[0]["Pierce Brown"])
# Lists in dictionaries
library = {
    "Pierce Brown": [
        "Red Rising",
        "Golden Son",
        "Morning Star"
        ]
    }
print(library)
# Looping through lists inside a dictionary
for books in library["Pierce Brown"]:
    print(books)