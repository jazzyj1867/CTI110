#FrownerJasmine
#04/28/2024
#P4LAB2
#Use while loop and for loop together

'''
Get integer from user
determine if the integer is positive or negetive
if number is positive, idsplay mulitlication table
if number is negative, tell user program cannot accept it
Ask user to run again?
if yes, run program
if no, end program
'''

run_again= 'yes'

while run_again != 'no':

    user_num = int(input("Enter an integer: "))

    if user_num > 0:
        #display multiplication for that value and range(1-12)
        for item in range(1, 13):
            print(f"{user_num}* {item} = {user_num * item}")
    else:
        print("This program does not handle negative numbers")

    run_again = input("Would you like to run the program again? ")
#Loop has broken. User entered 'no'
print("Program is ending...")
