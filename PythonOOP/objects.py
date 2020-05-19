#OOP

class PlayerCharacter:
    membership = True # Class Object Attribute
    def __init__(self, name, age):
        self.name = name #attributes
        self.age = age #attributes

    def run(self):
        print('Am apelat metoda run!')


player1 = PlayerCharacter('Jack', 14)
player2 = PlayerCharacter('John', 15)
player1.attack = 50 #property

print(player1.name)
print(player1.age)
print(player2.name)
player2.run()
print(player1.attack)

#help(player1) #object blueprint

player1.membership = False
print(player1.membership)
print(player2.membership)

