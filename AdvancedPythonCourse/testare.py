class BankAccount:

    def __init__(self, bank_name, account_number, balance):
        self.account_number = account_number
        self.bank_name = bank_name
        self.balance = balance

    def withdraw(self, account_number, amount):
        if not self.account_number == account_number:
            raise Exception('Invalid account!')
        else:
            if not self.balance > amount:
                raise Exception('Insuficient funds!')
            else:
                self.balance -= amount

    def deposit(self, account_number, amount):
        if self.account_number == account_number:
            self.balance += amount


class Employee:

    def __init__(self, person_name, salary=0):
        self.person_name = person_name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, value):
        self.__salary = value

    salary = property(get_salary, set_salary)

    def receive_salary(self, name, account_number, __salary):
        account = BankAccount(name, account_number, 10)
        account.deposit(account_number, __salary)
        return account.balance



if __name__ == '__main__':
    # ing_ba = BankAccount('ING', '1234', 5400)
    # print(ing_ba.bank_name, ing_ba.account_number, ing_ba.balance)
    # account_nr = '1234'
    # ing_ba.withdraw('1234', 1000)
    # print(ing_ba.balance)
    # ing_ba.withdraw('1234', 1000)
    # print(ing_ba.balance)
    # ing_ba.deposit('1234', 70000)
    # ing_ba.withdraw('1234', 4000)
    # print(ing_ba.balance)

    # employee_1 = Employee('Andrei', 7000)
    # print(employee_1.person_name)
    # print(employee_1.person_name, employee_1.balance, employee_1.salary)
    # employee_1.set_salary(1000)
    # employee_1.get_salary()
    # print(employee_1.salary)

    employee_1 = Employee('Andrei', 1)
    print(employee_1.receive_salary('ING', '1234', 1000))

