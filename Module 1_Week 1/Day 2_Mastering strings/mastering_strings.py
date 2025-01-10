# Strings are immutable - they don't change

# Creating strings with single and double quotes
single_quote = 'Single quotes are great'
double_quote = "SO are double quotes"
print(single_quote)
print(double_quote)


# Multi-line string using triple quotes
multi_line = '''This is a 
string that
spans multiple
lines'''

print(multi_line)


# String indexing
word = "Coding Temple"
print(word[0])
print(word[1])
print(word[7])
print(word[-1])
print(word[-2])


# Concatenation of strings
greeting = "Hello"
name = "George"
full_greeting = greeting + ", " + name + "!"
print(full_greeting)

full_greeting2 = f'{greeting}, {name}!'
print(full_greeting2)


# Repeat strings with *
laugh = "Ha" * 3 + "!" * 4
print(laugh)

print("-" * 30)


# Finding the length of a string
phrase = 'I\'m not lazy. i am on energy saving mode.'
length_of_phase = len(phrase)
print(length_of_phase)
print(phrase)


# String slicing (substrings)
string = "I'm not lazy. i am on energy saving mode."
print(string[0:13])
print(string[:-6])
print(string[14:])
print(string[-5:])


# Convert to uppercase and lowercase
message = "Hello, Python!"
print(message.upper())
print(message.lower())


# Remove whitespace from start and end of a string
# check out lstrip and rstrip if you want!
whitespace_string = "        Trim this!              "
print(whitespace_string.strip())
print(whitespace_string.lstrip())
print(whitespace_string.rstrip())


# Replace part of a string
text = "I love JavaScript!"
new_text = text.replace("JavaScript", "Python")
print(text)
print(new_text)


# Split and join
sentence = "Python rocks our world!"
sentence_without_exclam = sentence[:-1]
print(sentence_without_exclam)
words = sentence_without_exclam.split()
print(words)
print(words[0])
print(words[3])

joined_sentence = "-".join(words)
print(joined_sentence)


# Check if a string starts or ends with a specific substring
fileName = "super_secret_file.txt"
print(fileName.startswith("my"))
print(fileName.startswith("super"))
print(fileName.endswith(".txt"))


# String formatting with .format()
name = "Fred"
age = 99
print("My name is {} and I am {} years old.".format(name, age))


# String formatting with f-strings
print(f"My name is {name} and I am {age} years old.")


# More string methods: finding a substring and counting occurrences
long_text = "Python is powerful. Python is versatile. Python is everywhere!"
print(long_text.find("Python"))
print(long_text.count("Python"))


# Using slicing and immutability demonstration
original_text = "Jython"
fixed_text = "P" + original_text[1:]
print("Original text", original_text)
print("Fixed Text", fixed_text)

fixed_text2 = original_text.replace('J','P')
print("Fixed Text2", fixed_text2)


# title and capitalize
text = 'hello world'
print(text.capitalize())
print(text.title())


# isdigit - Check if a string consists only of digits, 
text = '12345'
print(text.isdigit())