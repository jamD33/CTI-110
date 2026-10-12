# Desarae James
# 10/11/2026
# P3HW1
# Debugging


mod_1 = int(input('Enter grade for Module 1: '))
mod_2 = int(input('Enter grade for Module 2: '))
mod_3 = int(input('Enter grade for Module 3: '))
mod_4 = int(input('Enter grade for Module 4: '))
mod_5 = int(input('Enter grade for Module 5: '))
mod_6 = int(input('Enter grade for Module 6: '))

# Add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# Determine lowest, highest, sum, and average for grades
low = min(grades)
high = max(grades)
total = sum(grades)
avg = total / len(grades)

# Determine letter grade for average
if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
    print('Your grade is: B')
elif avg >= 70:
    print('Your grade is: C')
elif avg >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')

#Step 5: Format and Display the results 
# The average is formatted to exactly 2 decimal places using f-strings 
print("\n---------- Results ------------")
print(f"Lowest Grade:   {low}")
print(f"Highest Grade:   {high}")
print(f"Sum of Grades:   {total}")
print(f"Average:         {avg:.2f}")
