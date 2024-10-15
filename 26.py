# using loop
num = int(input("Enter a number :"))
while(num>0):
    print(num)
    num = num-1
     
# Using recursive function

def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)
show(10)
