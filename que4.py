# Monthly Allowance & Savings Planner

pocket_money = float(input("Enter monthly pocket money: ₹"))

canteen = float(input("Enter canteen expense: ₹"))
transport = float(input("Enter transport expense: ₹"))
shopping = float(input("Enter shopping expense: ₹"))

total_expenses = canteen + transport + shopping
remaining_savings = pocket_money - total_expenses

is_budget_safe = remaining_savings >= 0

print("\n----- Monthly Budget Summary -----")
print("Pocket Money: ₹", pocket_money)
print("Canteen Expense: ₹", canteen)
print("Transport Expense: ₹", transport)
print("Shopping Expense: ₹", shopping)
print("Total Expenses: ₹", total_expenses)
print("Remaining Savings: ₹", remaining_savings)
print("Is Budget Safe:", is_budget_safe)