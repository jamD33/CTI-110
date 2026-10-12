# Desarae James
# 10/11/2026
# P3HW2
# Employee Information

# Request employee information from user
employee_name = input("Enter employee name: ")
hours_worked = float(input("Enter number of hours worked:"))
pay_rate = float(input("Enter employee pay rate: "))

# Evaluate overtime pay if hours worked is greater than 40
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    # Calculate overtime pay
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    # Calculate regular pay for 40 hours
    regular_pay = 40 * pay_rate
    # Calculate total pay including overtime
    gross_pay = regular_pay + overtime_pay
else:
    overtime_pay = 0
    overtime_hours = 0
    regular_pay = hours_worked * pay_rate
    gross_pay = regular_pay


# Display employee information and calculated pay
print("\n----------------------------------------")
print(f"Employee Name: {employee_name}")
print(f"Hours Worked: {hours_worked:<15}{"Pay rate": <12}{"OverTime Pay": <12}{"Regular Pay": <15}{"Gross Pay": <15}")
print("------------------------------------------------------------------")
print(f"{hours_worked:<18} {pay_rate:<18f} {overtime_pay:<18f} {regular_pay:<18f} {gross_pay:<18f}")
