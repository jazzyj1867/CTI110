#FrownerJasmine
#04/09/2024
#P1HW2
#create a program that does some basic math on numbers that are entered

print("Enter Budget:")
budget = int(input())
print("Enter Travel Destination:")
destination = input()
print("How much do you think you will spend on gas?")
gas = int(input())
print("Approximately how much will you need for accommodation/hotel?")
accommodation = int(input())
print("Last, How much do you need for food?")
food = int(input())
print()
print("------------Travel Expenses------------")
print()
print("Location:", destination)
print("Initial Budget:", budget)
print()
print("Fuel:", gas)
print("Accommodation:", accommodation)
print("Food:", food)
print()
remaining_balance = budget - (gas + accommodation + food)
print("Remaining Balance:", remaining_balance)