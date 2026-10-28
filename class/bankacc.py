class BankAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 2000000

a1 = BankAccount("Akshay")
a2 = BankAccount("Swayam")

print(a1.account_holder, a1.balance)
print(a2.account_holder, a2.balance)