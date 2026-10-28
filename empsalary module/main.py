import salary

basic = float(input("Enter basic salary: "))

print("Gross Salary:", salary.gross(basic))
print("Deductions:", salary.deductions(basic))
print("Net Salary:", salary.net(basic))