#modules
import random
import time

# comments!! Where you can write some notes!!

'''
multiline comments
Im still in the comments
'''

# Loosely typed - python figures out what kind of value it is
welcome_message = 'Welcome everyone!'
min_number = 1
max_number = 10
is_correct = False
secret_number = random.randint(min_number, max_number)


# is_correct = True
# print(secret_number)
# print(is_correct)
# print("Updated is_correct variable ",is_correct)

# num = int('6')
# print('type of num', type(num))



print(welcome_message)
print(f"Please guess the secret number between {min_number} and {max_number}")

guess = int(input("Go ahead and guess the secret number: "))
print("The user guessed ", guess)

# print(type(guess)) # '5' -> 5

# 1st Guess
if guess == secret_number:
    print("Wow! You guessed the number on your first try! Good job!")
    is_correct = True
elif guess < secret_number:
    print("Too low! Try again!")
else:
    print("Too high! Try again!")

# 2nd Guess
if not is_correct:
    guess = int(input("Go ahead and guess the secret number: "))

    if guess == secret_number:
        print("Wow! You guessed the number on your first try! Good job!")
        is_correct = True
    elif guess < secret_number:
        print("Too low! Try again!")
    else:
        print("Too high! Try again!")

# Last Guess
if not is_correct:
    guess = int(input("Go ahead and guess the secret number: "))

    if guess == secret_number:
        print("Wow! How did you survive! Awesome work!")
        is_correct = True
    else:
        print(f"Incorrect! The number was: {secret_number}")
        print("Your time is up!")
        time.sleep(1)
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("🔥🔥🔥")


if is_correct:
    print("You must've cheated! Good job anyways!")
else:
    print("Good luck next time!")