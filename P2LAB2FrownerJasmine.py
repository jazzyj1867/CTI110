#FrownerJasmine
#04/12/2024
#PLAB2
#write code that uses a dictionary to store user input and displays output to the user

#Dictonary
cars = {'Camaro': 1821, 'Prius': 52.36, 'Model S': 110, 'Silverado': 26,}
#get keys from dict
cars_keys = cars.keys()
print(cars_keys)

print(*cars_keys, sep = ", ")

#enter car
car_name = input("Enter a car:")

#Get MGP
car_mpg = cars[car_name]
print(f"The {car_name} gets {car_mpg} miles per gallon")

#get miles from user
miles_driven = float(input(f"How many miles will you drive the {car_name}?"))

#calcuate
gallons_needed = miles_driven/car_mpg

#display with F
print(f"{gallons_needed:.2f} gallons of gas are needed {car_name} {miles_driven}")