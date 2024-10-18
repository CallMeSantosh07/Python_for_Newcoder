# Shopping Cart Program of Wal Mart

foods = []
prices = []
Total = 0

while True:
    food = input('Enter food (Exit for quit): ').capitalize()
    if food == "Exit":
        break
    
    else:
        price = float(input(f"Enter the price of {food}: $"))
        foods.append(food)
        prices.append(price)

print("............your Cart...........")

for food in foods:
    print(food, end=" ")
    
for price in prices:
    print(price)
    Total += price
    
print()
print(f"Total amount of the foods is: ${Total}")