#classmethod

class PlayerCharacter:
    membership = True # Class Object Attribute
    def __init__(self, name, age):
        self.name = name #attributes
        self.age = age #attributes

    def shout(self):
        print(f'my name is {self.name}!')

    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Bill', num1 + num2)

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2

# player1 = PlayerCharacter('Jack', 20)
# print(PlayerCharacter.adding_things(2,3))


player3 = PlayerCharacter.adding_things(2, 3)

print(player3.name)
player4 = PlayerCharacter.adding_things2(2, 3)



