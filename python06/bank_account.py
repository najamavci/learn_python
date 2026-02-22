class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Not enough money")

    def balance(self):
        return self.__balance

    def apply_interest(self, rate):
        self.__balance += self.__balance * rate

    def can_pay(self, amount):
        return amount <= self.__balance


#unit tests
account = BankAccount(100)

account.deposit(50)
print(account.balance())  # 150

account.withdraw(20)
print(account.balance())  # 130

account.apply_interest(0.10)
print(account.balance())  # 143

print(account.can_pay(50))   # True
print(account.can_pay(500))  # False