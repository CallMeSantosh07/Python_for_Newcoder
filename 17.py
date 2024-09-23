
def CalculateGmean(a, b):
 mean =(a*b)/(a+b)
 print(mean) 
 
a= int(input("Enter a Number  :"))
b=int(input("Enter a number  :"))
CalculateGmean(a, b)

def average(a, b, c=1):
   print("The average is ", (a + b + c) / 2)