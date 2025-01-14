print("The Developer's Day")
print("Can you complete your project and deploy successfully?\n")

health = int(input("Enter your health (0 - 100): "))
energy = int(input("Enter your energy (0 - 100): "))
have_laptop = input("Do you have your laptop with you? (y - n): ")

# Evaluating health and energy
if health > 70:
    print("You're feeling great and ready to crush your coding tasks!")
    if energy > 50:
        print("You have the energy to debug all the issues today.")
    else:
        print("You're a bit tired, but caffeine is your best friend!")
else:
    print("You're feeling under the weather. Debugging might be harder today.")

if have_laptop == 'y':
    print("You have your laptop and all your tools are ready!")
elif have_laptop == 'n':
    print("\nYou forgot your laptop! Things might get complicated!")
else:
    print("Please answer with y for yes or n for no.")


if health > 30 and (have_laptop == 'y' or energy > 40):
    print("You jump in, analyze the logs and deploy the project!")
    health -= 20
else:
    print('''
You try to help, but you're either too tired or lack the tools!
The bug persists, causing delays.
''')
health -= 50

if health > 0:
    print("You survived the debugging session!")
    if health >= 50:
        print("You're still feeling good and can continue!")
    elif health > 20:
        print("\nYou're running on fumes, but the deadline is near!\n")
    else:
        print("You're getting burt out! Rest")

user_choice = input("You need admin access for the deployment. Do you have access? (y or n): ").strip().lower()

have_access = user_choice == 'y'

if have_access and (health > 10 or energy > 30):
    print("\nYou deploy the feature successfully!")
else:
    print("\nYou can't complete the deployment")
    if not have_access:
        print("Without admin access, you can't deploy!")
    else:
        print("You have the access but you're too exhausted.")