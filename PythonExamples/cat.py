class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Instantiate the cat object with 3 cats
tom = Cat('Tom', 2)
felix = Cat('Felix', 3)
alma = Cat('Alma', 5)

# Find the oldest cat
def find_oldest(*args):
    return max(args)

# Output
print(f'The oldest cat is {find_oldest(tom.age, felix.age, alma.age)} years old.')






