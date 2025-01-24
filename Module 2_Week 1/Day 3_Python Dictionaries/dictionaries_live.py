'''
Dictionaries: 
- Keys must be unique
- Keys must be immutable
- Values can be anything
- Dictionaries maintain insertion order
- Dictionaries are mutable
{key: value}

'''
import pprint
empty_dictionary = {}
my_dictionary = dict()
library = {
    "Pierce Brown": ["Red Rising", "Golden Son"],
    123456789: "Hail Mary",
    ("Brandon", "Sanderson"): "Way of Kings",
    # ["Matt", "Dinniman"] : "Dungeon Crawler Carl"
    # {"Matt", "Dinniman"}: "Dungeon Crawler Carl"
}

# print(type(empty_dictionary))
# print(type(my_dictionary))




# print(library["Pierce Brow"])

# .get()
# print(library.get("Pierce Brow", "Check your string"))

# 1. Manual
# Add to dictionary
library["Matt Dinniman"] = "Dungeon Crawler Carl"
# Update key/value in dictionary
# library["Pierce Brown"] = "Red Rising"
# Delete from Dictionary
# del library["Pierce Brown"]

# 2. Methods
# print(library)
# library.update({"Matt Dinniman": "Dungeon Crawler Carl"})
# library.update({"Pierce Brown": 'Red Rising'})
# print(library)
# value = library.pop('Matt Dinniman')
# print(value)

# if you just loop through a dictionary, it will provide you the keys. 
# .keys() will allow you access to all of the keys in the dictionary
# .values() will get you access to all of the values in the dictionary
# .items() will get you access to both the keys & values in the dictionary
# for k, v in library.items():
#     print(k, v)

# print(library.items())

library = {
    'Pierce Brown': {
        "Red Rising": 300,
        "Golden Son": 350,
        "Morning Star": {
            'location in series': '3rd book'
        }
    }, 
    'Matt Dinniman': {
        "Dungeon Crawler Carl": 400,
        "Carl's Doomsday Scenario": 450,
        "Iron Tangle": 500
    }
}

# print(library)
# pprint.pp(library)
# print(library["Pierce Brown"]["Morning Star"]['location in series'])

# for location, book in library['Pierce Brown']["Morning Star"].items():
#     print(location, book)

# List of Dictionaries
library = [{"Pierce Brown": "Red Rising"}, {"Matt Dinniman": "Dungeon Crawler Carl"}]
# print(type(library))
# for x in library:
#     print(x)
#     if "Pierce Brown" in x:
#         print(x["Pierce Brown"])
    # for author, book in dictionary.items():
    #     print(f"Author: {author}, Book: {book}")

# print(library[0]["Pierce Brown"])

library = {
    'Pierce Brown': {
        "Red Rising": [{"red": "Darrow"}, {"gold": ["Cassius", "Mustang", "Sevro"]}],
        "Golden Son": [1, 2, 3, 4, 5, 6, 7, 8],
        "Morning Star": {
            'location in series': '3rd book'
        }
    }, 
    'Matt Dinniman': {
        "Dungeon Crawler Carl": ["Carl", "Donut", "Mordecai"],
        "Carl's Doomsday Scenario": 450,
        "Iron Tangle": 500
    }
}

pprint.pp(library)
# print(library["Pierce Brown"]["Red Rising"][1]["gold"][1])

for character in library["Pierce Brown"]["Red Rising"][1]["gold"]:
    if character == "Mustang":
        print("GOLD")

library = 'Hello there, General Kenobi!'

list_comp = [x for x in library]
for x in library:
    list_comp.append(x)
print(list_comp)

vowels = 'aeiou'
example_sentence = 'This is an example sentence that I just made up on the fly.'
vowels_map = {vowel: example_sentence.lower().count(vowel) for vowel in vowels}
print(vowels_map)

my_str = 'asdfwqeroiughl;jxzcvb,anylretijye'
hashy = {}
most_dupes = 0
for letter in my_str:
    if letter in hashy:
        hashy[letter] += 1
        most_dupes = hashy[letter]
    else:
        hashy[letter] = 1
print(hashy)
print(most_dupes)