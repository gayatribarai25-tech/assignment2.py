# Café Outing Split-Bill Calculator

bill = float(input("Enter total bill amount: ₹"))
friends = int(input("Enter number of friends: "))

tip = bill * 10 / 100
total_bill = bill + tip
each_person = total_bill / friends

print("\n----- Café Bill -----")
print("Original Bill: ₹", bill)
print("10% Tip: ₹", tip)
print("Total Bill: ₹", total_bill)
print("Each Person Pays: ₹", each_person)
