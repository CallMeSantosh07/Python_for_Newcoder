def calculategmean(a,b):
    mean = (a*b)/(a+b)
    print("mean =",mean)
    
def isgreater(a,b):
    if(a>b):
        print("The value of a is greater than b")
    else:
        print("The value of b is greater than a")
    
a= int(input("Enter the value of a :"))
b= int(input("Enter the value of b :"))
isgreater(a,b)
calculategmean(a,b)

c= int(input("Enter the value of c :"))
d= int(input("Enter the value of d :"))
isgreater(c,d)
calculategmean(c,d)
    
