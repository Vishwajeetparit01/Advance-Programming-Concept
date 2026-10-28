inventory = {}

n = int(input("Enter number of products: "))

for i in range(n):
    name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    inventory[name] = quantity

name = input("Enter product to update: ")
if name in inventory:
    inventory[name] = int(input("Enter new quantity: "))

print("Inventory:", inventory)

if inventory:
    print("Highest stock:", max(inventory, key=inventory.get))

for name in list(inventory):
    if inventory[name] == 0:
        del inventory[name]

print("Final inventory:", inventory)
print("Total products:", len(inventory))