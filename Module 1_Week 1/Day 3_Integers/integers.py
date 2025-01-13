# Floating vs Int using isinstance()
num_int = 42
num_float = 42.52
print(isinstance(num_int, int))
print(isinstance(num_int, float))
print(isinstance(num_float, int))
print(isinstance(num_float, float))

print(type(num_float))
print(type(num_int))


# Basic Arithmetic (+ - / *) and format specifiers
drink_price = 3.25
cups_drunk = 3
total_spent = drink_price * cups_drunk
print(total_spent)

print(5 + int("5"))


''' Different parts of the format specifier
 : - starts the format specifier
 .2 - specifies that two decimal places should be displayed
 f -  tells Python to format the number as a float
'''
print(f"Total spent on drinks today: ${total_spent:.1f}")
print(total_spent)

num = 12.12345587755555
print(f'{num:.2f}')

# Modulus (%) - gives the remainder of two values
num = 21
print(f"The remainder is {num%2}")
if num % 2 == 0:
    print("The num is even")
else:
    print("The num is odd")

wallet = 100
childs_dream = 87.52
left_after_purchase = wallet % childs_dream
print(f"left in wallet after spoiling child: ${left_after_purchase:.2f}")

# Floor Division (//) rounds the answer down
people = 5
slices_of_pizza = 13
slices_per_person = slices_of_pizza // people
print("Slices of pizza for each person", slices_per_person)

print("-" * 30)
# Exponents ** and pow()
caffiene_level = 2 ** 4
print(f"Caffiene level: {caffiene_level}")

big_math = pow(2, 3, 5) # 2 ^ 3 % 5
print(big_math)

print("-" * 30)

# Absolute values
city_1_temp = 30
city_2_temp = 22

# We don't care which one is higher 
# We just want the difference between the two
temp_difference = abs(city_2_temp - city_1_temp)
print(f"The temperature difference is {temp_difference}")

print("-" * 30)

# Rounding with round()
price_of_item1 = 7.456
rounded_price1 = round(price_of_item1)
print(rounded_price1)

price_of_item2 = 7.55
rounded_price2 = round(price_of_item2)
print(rounded_price2)

price_of_item3 = 7.456
rounded_price3 = round(price_of_item3, 2)
print(rounded_price3)

print("-" * 30)

# Converting to Integer - int() and float()
floating_price = 4.99
approx_price = int(floating_price)
print(approx_price)

print("-" * 30)

floating_price = "4.99"
print(isinstance(floating_price, float))
higher_price = float(floating_price) + 1
print(higher_price)

print("-" * 30)

# max() and min()
knight_strength=20
dragon_strength = 50
warrior_strength = 100

print(max(knight_strength, dragon_strength, warrior_strength))
print(max(55,84,100,96,30,1,202))

print("-" * 30)

print(min(knight_strength, dragon_strength, warrior_strength))
print(min(55,84,100,96,30,1,202))