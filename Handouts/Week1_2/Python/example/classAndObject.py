class Person:

      # 构造函数
    def __init__(self, name):
        self.name = name

      # 定义方法
    def whoami(self):
        return "You are " + self.name


p1 = Person('tom')
print(p1.whoami())
print(p1.name)

p1.name = 'jerry'
print(p1.name)


class BankAccount:

     # 构造函数
    def __init__(self, name, money):
        self.__name = name  # 定义私有数据字段
        self.__balance = money  # 定义私有数据字段

    def deposit(self, money):
        self.__balance += money

    def withdraw(self, money):
        if self.__balance > money:
            self.__balance -= money
            return money
        else:
            return "Insufficient funds"

    def checkbalance(self):
        return self.__balance

b1 = BankAccount('tim', 400)
print(b1.withdraw(500))
b1.deposit(500)
print(b1.checkbalance())
print(b1.withdraw(800))
print(b1.checkbalance())

print(b1.__balance)
