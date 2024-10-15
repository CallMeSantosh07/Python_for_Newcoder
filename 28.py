weight = float(input("Enter weight: "))
unit = input("Enter the unit in kilogram or pound (K or P): ")
 
if unit == "K":
    weight = weight * 2.2
    print(f"Kilogrm to Pound: {weight} pound")
elif unit == "P":
    weight = weight * 0.45
else:
    print(f"you enter a wrong {unit} unit")

print(f"Kilogrm to Pound: {weight} pound")