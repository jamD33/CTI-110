# Desarae James
# P4LAB2
# 10/26/26
# Using loops to display information to users

'''
Get value from user
Determine if integer is positive or negative
if number is positive, display multiplacation table
if number is negative, tell user program cannot accept it 
If yes, run program
If no, end program
'''

run_again = 'yes'

while run_again != "no":

    user_num = int(input("Enter an integer:"))

    if user_num >= 0: 
        #display multiplication for that value and range (1-12)
        for item in range(1, 13) : 
            print(f"{user_num} * {item} = {user_num * item}")
    else: 
        print("This program does not handle negative values")
    
    run_again = input("Would you to run the program again?")


#Loop has broekn. User entered 'no'
print("Program is ending...")