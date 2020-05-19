class Person:
    GENDERS = ('F', 'M')
    MAX_AGE = 130

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    # def get_age(self):
    #     return self.__age
    #
    # def set_age(self, value):
    #     if value > self.MAX_AGE:
    #         raise Exception('Invalid age')
    #     self.__age = value
    #
    # age = property(get_age, set_age)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value > self.MAX_AGE:
            raise Exception('Invalid age')
        self.__age = value

    def _increase_age(self, increment=1):
        self.__age += increment

    def introduce(self):
        self._increase_age(10)
        return f'Hello! I am {self.name}'

    @classmethod
    def print_genders(cls):
        print(f'Allowed genders: {cls.GENDERS}')

    @staticmethod
    def print_message(a, b):
        print('Something general about persons', a, b)


if __name__ == '__main__':
    ana = Person('Ana', 25)
    print(ana.name)
    print(ana.age)

    mihai = Person('Mihai', 50)
    print(mihai.name)
    print(mihai.age)

    print(mihai.introduce())
    print(ana.introduce())

    # print(ana._Person__age)
    ana.introduce()
    print(ana.age)

    ana.age = 20
    print(ana.age)

    Person.print_genders()
    ana.print_genders()

    Person.print_message(1, 2)
    ana.print_message('la', '4')

    ana.age = 200
