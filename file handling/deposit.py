
n = int(input("Enter number of transactions: "))

with open("transaction.txt", "w") as file:
    for i in range(n):
        type = input("Enter Deposit or Withdrawal: ")
        amount = int(input("Enter amount: "))

        file.write(type + "," + str(amount) + "\n")


deposit = 0
withdrawal = 0
largest = 0

with open("transaction.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")

        type = data[0]
        amount = int(data[1])

        if type.lower() == "deposit":
            deposit += amount
        else:
            withdrawal += amount

        if amount > largest:
            largest = amount

balance = deposit - withdrawal

print("\nTotal Deposits:", deposit)
print("Total Withdrawals:", withdrawal)
print("Final Balance:", balance)
print("Largest Transaction:", largest)