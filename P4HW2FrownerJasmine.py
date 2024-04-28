'''
Asks the user employee name
Enter user pay rate and hours worked
Calculate overpay and regular pay. Store these values in variables, at the end of the program you will display overtime total, regular pay total, gross pay total, and number of employees entered
Ask user to enter another employee's name to calculate salary for or "Done" to terminate program. Note we are using sentinels here.
When user chooses to stop entering employee information , display results as shown in image below.
THE PROGRAM ONLY TERMINATES IF THE USER ENTERS "Done" for employee name.
'''


total_employees = 0
total_overtime_pay = 0.0
total_regular_pay = 0.0
total_gross_pay = 0.0
user_entry = True


#Create loop to enter employee info
while user_entry:
    name = input("Enter employee's name or \"Done\" to terminate: ")
    print()
    if name.lower() == "done":
        break
    
    hours_worked = float(input(f"How many hours did {name} work? "))
    pay_rate = float(input(f"What is {name}'s pay rate? "))

#Calculate overtime employee pay
    overtime_hours = max(hours_worked - 40, 0)
    regular_hours = hours_worked - overtime_hours
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    regular_pay = regular_hours * pay_rate
    gross_pay = regular_pay + overtime_pay

#Update totals employees pay
    total_employees = total_employees + 1
    total_overtime_pay = total_overtime_pay + overtime_pay
    total_regular_pay = total_regular_pay + regular_pay
    total_gross_pay = total_gross_pay + gross_pay

#Output individual employee's pay information
    print(f"\nEmployee name: {name}")
    print()
    print(f"{'Hours Worked':<15}{'Pay Rate':<15}{'OverTime':<15}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<15}")
    print(f"{hours_worked:<15.2f}{pay_rate:<15.2f}{overtime_hours:<15.2f}{overtime_pay:<15.2f}{regular_pay:<15.2f}{gross_pay:<15.2f}")
    print()

#Output total information
print("Total number of employees entered:", total_employees)
print("Total amount paid for overtime:", total_overtime_pay)
print("Total amount paid for regular hours:", total_regular_pay)
print("Total amount paid in gross:", total_gross_pay)

