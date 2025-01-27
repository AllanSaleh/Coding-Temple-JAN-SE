# Regular Expressions
# import re
import re

# re.search()
# re.match()
# re.find_all()

# regexlib.com

story='''The author Pierce Brown wrote the book Red Rising. You can contact him via email at pierce.brown@library.com or call him at 555-123-4567.
The book Dungeon Crawler Carl was created by Matt Dinniman. His email is matt.dinniman21@library.com, and his phone number is 555-234-5678.
Craig Alanson is the mind behind the book Columbus Day. Reach him at craig.alanson@gmail.com or call 555-345-6789.
James Clear authored the popular book Atomic Habits. You can email him at james.clear@library.com or dial 555-456-7890 to get in touch.
J.R.R. Tolkien, the legendary author of The Hobbit, can be contacted via email at jrr.tolkien@library.com or at his phone number, 555-567-8901.
'''



# re.findall() example
# find all will find all occurences of a pattern in a string and return them as a list. This is good for extracting multiple instances of data that are all
# roughly the same thing. Phone number, emails, other repeated patterns
# re.findall(<pattern>, <text>)
# This [] is known as a set.
lowercase_letters = re.findall(r'[a-c]', story)
# hashy = {letter: lowercase_letters.count(letter) for letter in lowercase_letters}
# print(hashy)
uppercase_letters = re.findall(r'[A-Z]', story)
all_letters = re.findall(r'[A-z]', story)
numbers = re.findall(r'[0-9]', story)
# print(lowercase_letters)
# print(uppercase_letters)
# print(all_letters)
# print(numbers)

find_all_phone_numbers = re.findall(r'[0-9]{3}-[0-9]{3}-[0-9]{3}', story)
print(find_all_phone_numbers)
# find_all_phone_numbers = re.findall(r'\d{3}-\d{3}-\d{3}', story)
# print(find_all_phone_numbers)

# re.search() example
# search looks for the first occurence of a pattern and returns a match object. This is useful if you want to find something specific or just the first occurence
# of something
# re.search(<pattern>, <text>)
lowercase_letters_search = re.search(r'[A-z]+', story)
print(lowercase_letters_search)
print(lowercase_letters_search.group())

# re.match() example
# Best used for a pattern found at the beginning of a string. So if you want to know if something starts with something, so vlaidating some kind of input
# re.match(<pattern>, <text>)
match_test = re.match(r'[A-z]', story)
print(match_test)

specific_word_search = re.findall(r'awful', story)
print(specific_word_search)


# Special Characters: 
# \A Returns a match if the specified characters are at the beginning of the string
"email | name | phone number | address"
special_A = re.findall(r'\AThe', story)
print(special_A)

# \d Returns a match where the string contains digits (numbers from 0-9)

# \D Returns a match where the string DOES NOT contain digits
special_D = re.findall(r'\D', story)
print(special_D)

# \w Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
special_w = re.findall(r'\w', story)
print(special_w)

#  \W Returns a match where the string DOES NOT contain any word characters	
special_W = re.findall(r'\W', story)
print(special_W)

# \b can speficy a boundary. 
# all_phone_numbers = re.findall(r'[0-9]{3}-[0-9]{3}-[0-9]{4}\b', authors)

# Finding an email (There are a million ways to do this)
find_email = re.findall(r'[a-zA-Z0-9.]+@[a-zA-Z0-9.-]+', story)
print(find_email)

# . Any character except a newline character

# * Zero or more occurences

# {} exact specified amount. 

# Other importand concepts. 
# The \ has two uses: 
    # One is to introduce a special sequence. These are all predefined. 
    # One is to escape a special character
# Why use \. or \? over [?] or [.]
#   There are some nuances but both are pretty similar
ex_2 = "How. are. you. doing? today? Donovan?"
finding_question = re.findall(r'[A-z]+\.', ex_2)
print(finding_question)

# Using groups()
# So groups and using .group() can be really nice for organizing the information you are looking for into some kind of clear format. 
# Or if you are looking for multiple things in a string, I 
author = 'The author Pierce Brown wrote the book Red Rising. You can contact him via email at pierce.brown@library.com or call him at 555-123-4567.'
searching = re.search(r'([a-zA-Z0-9.]+@[a-zA-Z0-9.-]+).*([0-9]{3}-[0-9]{3}-[0-9]{4})', author)
print(searching.group(0))

change = re.sub(r'([0-9]{3}-[0-9]{3}-[0-9]{4})', 'REDACTED PHONE NUMBER', author)
print(change)