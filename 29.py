
try:
    saving = 10000
    deposit = int(input("Enter the deposit number :"))
    Total_Balance = deposit + saving
    print(Total_Balance)
    
except ValueError as e:
    print(e)
    print("Please Enter Number")