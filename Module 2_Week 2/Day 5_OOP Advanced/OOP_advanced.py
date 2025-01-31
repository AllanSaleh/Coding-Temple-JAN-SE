'''
OOP => Object Oriented Programming. 

Encapsulation
- The bundling of data (attributes) and methods within a class while restricting direct access to some components.
- Prevents accidental modification of data and enforces controlled access.
    - public => Freely modifiable
    - private => Hide data. Shouldn't be directly accessed or modified. Can't or shouldn't be inherited by subclasses
    - protected => A mix of both. If you want to discourage change of something, use this. Can be inherited by subclasses

Abstraction
- Simplifies complex systems by exposing only the relevant parts while hiding unnecessary details.
- Let's you use it without needing to know all the complext background processes

Inheritance
- Allows a new subclass to inherit attributes and methods from an existing class

Polymorphism
- Allows methods to do different things based on the object calling them. 
- I can redefine the same method in different subclasses

Abtract classes and @abstract methods
- An Abstract class is a class that is NOT supposed to be instaniated directly. 
- Can only be defined if there is at least one abstract method inside it. 

'''
from abc import ABC, abstractmethod


class Character(ABC):
    def __init__(self, health, name, weapon, voiceline, attack):
        # Protected. Python won't stop us from changing this. There will be no error
        # The goal of this is for the developer. This is saying to the develper or anyone using this that this is a value meant 
        # to only be changed within the class. Not outside of it. BUT there is nothing stopping us from changing it outside of the class.
        self._health = health
        self.name = name
        self.weapon = weapon
        self.voiceline = voiceline
        self.attack = attack
        self.__secret_code = "This is my secret code"

    @abstractmethod
    def attack_move(self):
        print(f"{self.name} used {self.weapon} and did {self.attack} damage")

    def use_voiceline(self):
        print(f"{self.name} yells {self.voiceline}")

    def get_health(self):
        return self._health
    
    def set_health(self, value):
        if isinstance(value, int):
            self._health = value
            return self._health
        else:
            raise TypeError("Incorrect type provided. Please provide a number")


class Brute(Character):
    def __init__(self, armor, **kwargs):
        super().__init__(**kwargs)
        self.armor = armor
        self.__brute_secret_code = "This is my brute's secret code"
    
    def attack_move(self):
        print(f"{self.name} slipped on some ice and dropped his {self.weapon}")
    
    def secret_code_change(self):
        self.__brute_secret_code = "A changed secret code"
        return self.__brute_secret_code

    def get_secret_code(self):
        return self.__brute_secret_code

class Grunt(Character):
    def __init__(self,health, name, weapon, voiceline, attack, secondary):
        super().__init__(health, name, weapon, voiceline, attack)
        self.secondary = secondary

    def attack_move(self):
        super().attack_move()


# my_player = Character(100, "Master Chief", "Battle Rifle", "Monument to your sins", 10)
my_brute = Brute(health=100, name="Titus", weapon="Gravity Hammer", voiceline="ARGHHHHH", attack=10, armor=20)
my_grunt = Grunt(100, "Yap yap", "Plasma Pistol", "ARGHHHHH", 10, "Needler")

# my_player.attack_move()
# my_brute.attack_move()
# my_grunt.attack_move()

# print("Health", my_brute.get_health())
# my_brute.set_health(70)
# print("Health", my_brute.get_health())

# print("Secret code", my_brute.__secret_code)
# print("Brute secret code", my_brute.__brute_secret_code)
# my_brute.__brute_secret_code = "Haha I\"m overwriting your secret code"
# print("Brute secret code", my_brute.__brute_secret_code)
# my_brute._Brute__brute_secret_code = "Changed secret code"
print(my_brute.get_secret_code())
my_brute.secret_code_change()
print(my_brute.get_secret_code())

try:

    my_brute.set_health("12")
except TypeError as te:
    print(f"Unrecognized type: {te}")




    