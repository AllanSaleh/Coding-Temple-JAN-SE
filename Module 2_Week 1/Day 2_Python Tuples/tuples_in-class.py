'''
Tuples: 
    - https://www.w3schools.com/python/python_ref_list.asp vs https://www.w3schools.com/python/python_ref_tuple.asp
    - Ordered so we can use indices
    - Immutable so we can't add, remove, or edit items inside
    - Can have multiple data types
    - USES PARENTHESES
    - Good for keeping data together and prevent accidental adjustment

'''

# Can create a tuple using the constructor
my_tuple = tuple()
print(type(my_tuple))

# Can create one with premade values
my_made_tuple = (1, 2, 3)
print(type(my_made_tuple))

# Can make one with a single value BUT you need to have that comma in there
my_single_tuple = (1,)
print(type(my_single_tuple))

# Can also do it with an empty parentheses. 
my_empty_tuple = ()
print(type(my_empty_tuple))

# library = ("Red Rising", "Pierce Brown", "Hardcover", "2020-12-12")
# You can also have other nested data structures inside of a tuple. 
library = (["Red Rising", "Golden Son"], "Pierce Brown", "Hardcover", "2020-12-12")
print(library)

# You can loop through a tuple
for i in range(len(library)):\
#       But you can't overwrite a value in the tuple 
    print(library[i])
#     library[i] = "Golden Son"
# IF YOU HAVE A LIST INSIDE OF A TUPLE, YOU CAN EDIT THE LIST. THE QUESTIONS IS WHY? SHOULD YOU BE USING TUPLES IF YOU NEED TO EDIT SOMETHING? 
# library[0][1] = "Morning Star"
# print(library)

# Similar to list slicing, you can also do tuple slicing. The result will be a tuple.
# print(type(library[0:2]))

# You can also do Tuple unpacking. MAKE SURE YOU HAVE ENOUGH VARIABLES TO MATCH WITH THE VALUES IN THE TUPLE
library = ("Red Rising", "Pierce Brown", "Hardcover", "2020-12-12")
book, author, cover, release_date = library
print(type(book))
print(type(author))
print(type(cover))
print(type(release_date))

# If there is a value you don't need, You can use a _ placeholder
library = ("Red Rising", "Pierce Brown", "Hardcover", "2020-12-12")
book, author, _, release_date = library
print(book)
print(author)
print(release_date)

# You can unpack multiple values into a single variable if youuse the * ex: *<var>. This can be placed in the beginning, middle, or end. PLACEMENT MATTERS
library = ("Red Rising", "Pierce Brown", "Hardcover", "2020-12-12")
book, *cover, release_date = library
# print(book)
# print(cover)
# print(release_date)

# You can also return a Tuple from a function. If you do that, you'll need to unpack it if you need to use the variables. 
def get_book():
    return "Atomic Habits", "James Clear", "Hardcover", "2020-12-12"

# Using this format, you can also declare a tuple
example_tuple = 'Atomic Habits', 'James Clear', 'James Clear', 'Hardcover', '2020-12-12'
print(type(example_tuple))

my_book = get_book()
print(my_book, type(my_book))
book, author, cover, release_date = get_book()
print(book)
print(author)
print(cover)
print(release_date)

# These are the two methods available to Tuples. Index and count. 
# .index() will find the index location of the value passed in
print(example_tuple.index('Hardcover'))
# .count() the count will determine how many of a certain value appear in a tuple. 
print(example_tuple.count('James Clear'))
