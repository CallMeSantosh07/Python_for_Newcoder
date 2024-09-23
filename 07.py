#nested if Statement

number=int(input("Enter a Number :"))
if(number<0):
    print("The Number is Negative")
elif(number>0):
    if(number<=10):
        print("The number is between  1-10")
    elif(number>10 and number<=20):
        print("The number is between 10-20")
    else:
        print("The Number is greater than 20")
    
else:
    print("the number is zero")
    