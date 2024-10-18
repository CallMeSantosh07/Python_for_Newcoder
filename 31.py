import time

for seconds in range(5, 0, -1):
    print(seconds)
    time.sleep(1)

print("Happy birthday")

# Nested Loop in Python 

row = int(input("Enter a number: "))
colum = int(input("Enter a Numbe: "))
symbol = input("Enter which symbol do you want to use: ")

for i in range(row):
    for j in range(colum):
        print(symbol, end="")
    print()