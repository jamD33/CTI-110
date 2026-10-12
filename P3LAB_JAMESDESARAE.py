# Desarae James
# P3 LAB
# 10/11/2026
# Writing code that displays information to users

# Instruct the user to enter the amount of money as a float
amount = float(input("Enter the amount of money: "))

# Convert the dollar amount to cents as an integer to avoid floating point errors
# round()
amount_cents = int (round(amount * 100))

# If total amount is 0, print "No change"
if amount_cents == 0:
    print("No change")
else:
    # Calculate the number of each currency using floor division (//) and the modulus operator (%)
    dollars = amount_cents // 100
    amount_cents %= 100
    quarters = amount_cents // 25
    amount_cents %= 25
    dimes = amount_cents // 10
    amount_cents %= 10
    nickels = amount_cents // 5
    amount_cents %= 5
    pennies = amount_cents

    # Display the number of each currency
    print("----Change Breakdown----")
    if dollars == 1:
        print(f"{dollars} Dollar")
    else:
        print(f"{dollars} Dollars")
    if quarters > 0: 

        if quarters == 1:
            print (f"{quarters} Quarter")
    else: 
        print(f"{quarters} Quarters")
    if dimes > 0:
        if dimes == 1:

            print(f"{dimes} Dime")
        else:
            print (f"{dimes} Dimes")

    if nickels > 0:
        if nickels == 1:
            print(f"{nickels} Nickel")
        else:
            print(f"{nickels} Nickels")
    else:
        print(f"{nickels} Nickels")

    if pennies > 0:
        if pennies == 1: 
            print(f"{pennies} Penny")
        else: 
            print(f"{pennies} Pennies")

