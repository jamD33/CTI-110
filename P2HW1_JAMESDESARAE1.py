# Desarae James
# P2HW1
# Calculating travel expenses using string method 

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
print("-----Travel Expenses-----")


#with align character:
print(f'Trip location: {trip_location:<20s}')
print(f"Initial Budget: ${budget:<20.2f}")
print(f"Gasoline: ${gasoline:<20.2f}")
print(f"Accommodations: ${accommodations:<20.2f}")
print(f"Food: ${food:<20.2f}")
print(f"Total Expenses: ${total_expenses:<20.2f}")
print(f"{'-' * 20}")
print(f"Remaining Budget: ${remaining_budget:<20.2f}")

