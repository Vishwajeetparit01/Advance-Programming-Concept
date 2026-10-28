class BankAccount:
    count = 1000

    def __init__(self, account_holder):
        BankAccount.count += 1
        self.account_holder = account_holder
        self.account_number = BankAccount.count
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def display_balance(self):
        print(self.account_holder, self.balance)

    def transfer(self, amount, other_account):
        if self.balance >= amount:
            self.balance -= amount
            other_account.balance += amount
        else:
            print("Insufficient balance")

a1 = BankAccount("Akshay")
a2 = BankAccount("Rahul")

a1.deposit(1000)
a1.withdraw(200)
a1.transfer(300, a2)

a1.display_balance()
a2.display_balance()