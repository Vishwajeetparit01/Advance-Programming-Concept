account = {"balance": 0, "history": []}

def deposit(amount):
    account["balance"] += amount
    account["history"].append("Deposited " + str(amount))

def withdraw(amount):
    if amount <= account["balance"]:
        account["balance"] -= amount
        account["history"].append("Withdrawn " + str(amount))
    else:
        print("Insufficient balance")

deposit(int(input("Enter deposit: ")))
withdraw(int(input("Enter withdrawal: ")))

print("Balance:", account["balance"])
print("History:", account["history"])