#FrownerJasmine
#04/12/2024
#P2LAB1 
# write code that performs mathematical calculations and displays information to users

#Input Radius
radius = float(input(f"What is the radius of the circle?")) 
#math used to do calucations
import math
circumference = 2 * math.pi* radius
diameter = radius * 2
area = math.pi* radius**2
#Show Results
print(f"The diameter of the circle is {diameter: .1f}")
print(f"The circumference of the circle is {circumference: .2f} ")
print(f"The area of the circle is {area: .3f} ")