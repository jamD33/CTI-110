#Desarae James
#9/29/2026
#P2HW2
#Assess student number of list

#//Step 1 & 2: Ask user for each module grade individually
grade_mod1 = float(input("Enter grade for Module1:"))
grade_mod2 = float(input("Enter grade for Module2:"))
grade_mod3 = float(input("Enter grade for Module3:"))
grade_mod4 = float(input("Enter grade for module4:"))
grade_mod5 = float(input("Enter grade for module5:"))
grade_mod6 = float(input("Enter grade for module6:"))

# Step 3: Store all six entered grades in a descriptive Python list
module_grades = [
    grade_mod1,
    grade_mod2,
    grade_mod3,
    grade_mod4,
    grade_mod5,
    grade_mod6,
]

# Step 4: Calculate the required results using built-in functions
lowest_grade = min(module_grades)
highest_grade = max(module_grades)
total_sum = sum(module_grades)
average_grade = total_sum / len(module_grades)

#Step 5: Format and Display the results 
# The average is formatted to exactly 2 decimal places using f-strings 
print("\n---------- Results ------------")
print(f"Lowest Grade:   {lowest_grade}")
print(f"Highest Grade:   {highest_grade}")
print(f"Sum of Grades:   {total_sum}")
print(f"Average:         {average_grade:.2f}")
