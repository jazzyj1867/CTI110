#FrownerJasmine
#04/21/2024
#P3HW@
#formatting strings to make them display nicely.


#Asks the user to enter name of employee
employee_name = input("Enter employee's name: ")


#Ask user to enter number of hours the employee worked this week
hours_worked = float(input("Enter number of hours worked: "))
                          
#Ask user to enter employee's pay rate
pay_rate=float(input("Enter employee's pay rate: "))

print("---------------------------------------------")
print(f"Employee name:     {employee_name}")



                          
#Evaluate if employee has worked overtime (more than 40 hours)
if hours_worked > 40:
    print("The employee has worked overtime.")
    
#Calculate regular hours worked (up to 40 hours)
regular_hours = 40
    
#Calculate overtime hours
overtime_hours = hours_worked - 40
#Calculate the amount owed for regular hours worked
regular_pay = regular_hours * pay_rate
    
#Calculate the amount owed for overtime hours
overtime_rate = 1.5 * pay_rate  # Assuming time and a half for overtime
overtime_pay = overtime_hours * overtime_rate
    
#Calculate gross pay (total amount that should be paid to the employee)
gross_pay = regular_pay + overtime_pay

print(f"The amount owed to the employee for regular hours worked is: ${regular_pay:.2f}")
    
#Display the amount owed for overtime hours
print(f"The amount owed to the employee for overtime hours is: ${overtime_pay:.2f}")
    
#Display the gross pay
print(f"The gross pay (total amount that should be paid to the employee) is: ${gross_pay:.2f}")
else:
    print("The employee has not worked overtime.")
    
# Calculate the amount owed for regular hours worked
regular_pay = hours_worked * pay_rate
    
# Display the amount owed for regular hours worked
print(f"The amount owed to the employee for regular hours worked is: ${regular_pay:.2f}")
