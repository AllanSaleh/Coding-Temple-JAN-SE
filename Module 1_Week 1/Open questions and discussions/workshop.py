def introduce(name, hobbie):
    print(f"Hello! My name is {name}! My hobbie is {hobbie}")

introduce("Allan", "Playing basketball")

introduce("Cody", "playing video games")

introduce("Ben", "coding")

user_name = input("Please enter your name: ")
user_hobby = input("Please enter your hobby: ")
introduce(user_name, user_hobby)


# It can take any number of parameters
def add_numbers(*args):
    return sum(args)

sum_of_all_numbers = add_numbers(1,5,5,9,6,7,1,52,4,87,2,4,8)
print(f"Sum of all numbers: {sum_of_all_numbers}")

