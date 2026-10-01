# Deposits and Withdrawals

def calculate_transactions():

    total_deposits = 0
    total_withdrawals = 0
    largest_transaction = 0

    with open("transactions.txt", "r") as file:
        for line in file:
            transaction, amount = line.strip().split(",")
            amount = float(amount)

            if amount > largest_transaction:
                largest_transaction = amount

            if transaction == "Deposit":
                total_deposits += amount

            elif transaction == "Withdrawal":
                total_withdrawals += amount

    final_balance = total_deposits - total_withdrawals

    print("Total Deposits:", total_deposits)
    print("Total Withdrawals:", total_withdrawals)
    print("Final Balance:", final_balance)
    print("Largest Transaction:", largest_transaction)


# Create file
with open("transactions.txt", "w") as file:
    file.write("Deposit,10000\n")
    file.write("Withdrawal,2500\n")
    file.write("Deposit,5000\n")
    file.write("Withdrawal,1500\n")
    file.write("Deposit,8000\n")

calculate_transactions()