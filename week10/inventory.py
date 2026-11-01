# inventory.py
# Author: Camdyn Schatz
# Module 10 Lab: Inventory list manager

# --- Exercise 1: build a list

print("--- Exercise 1 : build a list ---")

inventory = ["pen","notebook","stapler","tape","marker"]
print(inventory)
print(len(inventory))

# --- Exercise 2: index practice

print(" --- Exercise 2; index practice ---")
print(inventory[0])
print(inventory[-1])

middle = len(inventory) // 2
print(inventory[middle]) 


print(" --- Exercise 3: list slicing ---")

print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

print(" --- Exercise 4: list methods ---")

inventory.append("envelope")
inventory.append("tape")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)

print(" --- Exercise 5: tuple comaparison ---")
coords = [40.7128, -740060]

try:
    coords[0] = 99
except TypeError as error:
    print(f"TypeError caught: {error}")
    print("Tuples protect coordinates from being changed by accident")

print(" --- Exercise 6: list average sales ---")

sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print(f"Total sales: {total}")
print(f"Number of sales: {count}")
print(f"Average sales: {average}")
print(f"Best sale: {max(sales)}")
print(f"Worst sale: {min(sales)}")

best = sales[0]
worst = sales[0]

print(f"Best sale (loop): {best}")
print(f"Worst sale (loop): {worst}")

print(" --- Exercise 7: accumlator pattern ---")

price = [9.99, 14.99, 4.99, 24.99, 1.99]

discounted = []
for price in price:
    discounted.append(round(price * 0.9, 2))

print(price)
print(discounted)

print(" --- Exercise 8: filter ---")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []

for amount in sales:
    if amount > 300:
        high_sales.append(amount)

print(high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: {sum(high_sales) / len(high_sales)}")

# SELF ASSESMENT QUESTIONS