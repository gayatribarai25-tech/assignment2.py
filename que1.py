# 1. Myntra Shopping Discount Cart

item1 = float(input("Enter price of item 1: ₹"))
item2 = float(input("Enter price of item 2: ₹"))

subtotal = item1 + item2
discount = subtotal * 15 / 100
after_discount = subtotal - discount
delivery_fee = 99
total = after_discount + delivery_fee

print("\n----- Myntra Bill -----")
print("Item 1: ₹", item1)
print("Item 2: ₹", item2)
print("Subtotal: ₹", subtotal)
print("15% Discount: ₹", discount)
print("Delivery Fee: ₹", delivery_fee)
print("Final Total: ₹", total)