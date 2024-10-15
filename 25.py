usd_value = float(input("Enter currency in USD :"))
def currency(usd_value):
    nep_value = usd_value * 134.42
    print(usd_value,"USD = ",nep_value,"NPR")
    
currency(usd_value)