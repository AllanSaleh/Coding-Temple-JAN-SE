'''
OOP => Object Oriented Programming. 

'''


class Enemy:
    def __init__(self, name, health, damage, voiceline, attack_name):
        # instance attribute
        if isinstance(name, str):
            self.name = name
        else:
            print("Name is of wrong type. Please fix and reinstantiate")

        self.health = health
        self.damage = damage
        self.voiceline = voiceline
        self.attack_name = attack_name

    def use_voiceline(self, enemy_name):
        print(f'The {self.name} calls out "{self.voiceline}" at {enemy_name}')

    def take_damage(self, enemy):
        self.health -= enemy.damage
        if self.health <= 0:
            print("This is a method call from another method: ", self.total_health())
            print(f"{self.name} has his {self.total_health()} health. They have PERISHED")
        else:
            print(f"Our {self.name} took {enemy.damage} damage and now has {self.health} health")

    def total_health(self):
        return self.health
    


Elite = Enemy(12, 100, 5, "Its the DEMON", 'Fire')
Grunt = Enemy("Grunt", 50, 2, "CHARGE", 'Shoot')

# instantiate, instance, object
# instantiate => When I create an instance/object of the class

# Elite.use_voiceline("Master Chief")

Grunt.take_damage(Elite)
Grunt.take_damage(Elite)
Grunt.take_damage(Elite)
Grunt.take_damage(Elite)
Grunt.take_damage(Elite)
Grunt.take_damage(Elite)
Grunt.take_damage(Elite)
Grunt.take_damage(Elite)
Grunt.take_damage(Elite)
Grunt.take_damage(Elite)
print(Grunt.total_health())
# print(Elite.health)
# print(Elite.damage)
# print(Elite.voiceline)
# print(Elite.attack_name)

# print(Elite2.health)
# print(Elite2.damage)
# print(Elite2.voiceline)
# print(Elite2.attack_name)
