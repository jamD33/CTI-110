# Desarae James
# 10/27/2026
# P4HW2
# Employee Information with loops

# Create accumulator variables for overtime pay, regular pay, gross pay and employee count
overtimepay_total = 0
regularpay_total = 0
grosspay_total = 0
employee_count = 0

# Request employee information from user
employee_name = input("Enter employee name or done to finish: ")

while employee_name.lower() != 'done':
    # Ask for employee info
    hours_worked = float(input(f"How many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name}'s hourly pay rate? "))

    # Add employee count plus one
    employee_count += 1

    # Evaluate overtime
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * (pay_rate * 1.5)
        regular_pay = 40 * pay_rate
        gross_pay = regular_pay + overtime_pay
    else:
        overtime_hours = 0
        overtime_pay = 0
        regular_pay = hours_worked * pay_rate
        gross_pay = regular_pay

    # Add to accumulator totals
    overtimepay_total += overtime_pay
    regularpay_total += regular_pay
    grosspay_total += gross_pay

    # Display employee information and calculated pay
    print("\n----------------------------------------")
    print(f"Employee Name: {employee_name}")
    print(f"Hours Worked: {hours_worked:<15} Pay Rate: {pay_rate:<12} Overtime Pay: {overtime_pay:<12} Regular Pay: {regular_pay:<15} Gross Pay: {gross_pay:<15}")
    print("------------------------------------------------------------------")
    print(f"{hours_worked:<18} {pay_rate:<18.2f} {overtime_pay:<18.2f} {regular_pay:<18.2f} {gross_pay:<18.2f}")

    # Get next employee name
    employee_name = input("Enter employee name or done to finish: ")

print(f"Total number of employees entered: {employee_count}")
print(f"Total amount paid for overtime: ${overtimepay_total:,.2f}")
print(f"Total amount paid for regular time: ${regularpay_total:,.2f}")
print(f"Total amount paid in gross: ${grosspay_total:,.2f}")
