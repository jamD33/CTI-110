# Desarae James
# P1HW2
# Calculating travel expenses 

# calculate expenses

print("This program calculates travel expenses.")
print()

budget = float(input("Enter budget: "))
trip_location = input("Enter your travel destination: ")
gasoline = float(input("Enter estimated gasoline expenses: "))
accommodations = float(input("Enter estimated accommodations expenses: "))
food = float(input("Enter estimated food expenses: "))

total_expenses = gasoline + accommodations + food
remaining_budget = budget - total_expenses

print(f"Location: {trip_location}")
print(f"Initial Budget: ${budget:.2f}")
print(f"Total Expenses: ${total_expenses:.2f}")
print(f"Remaining Budget: ${remaining_budget:.2f}")
