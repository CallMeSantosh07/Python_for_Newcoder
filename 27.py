name = input("Enter your name :").title()

while name == "":
    print("Please enter your name ")
    name = input("Enter your name :").title()
print(f"Hello, {name}")