#FrownerJasmine
#04/26/2024
#P4LAB1
#Triangle and Square

#FrownerJasmine
#04/21/2024
#P4LAB1
#Turtle graphics program that draws a triangle and a square

#import the library
import turtle

#create the turtle window and drawing object
win = turtle.Screen()
pen = turtle.Turtle()   

#set turtle Options
pen.pensize(5)
pen.pencolor("purple")
pen.shape("arrow")

#Code to draw the shapes
'''pen.forward(200)
pen.left(90)
pen.forward(100)
pen.left(90)
pen.forward(200)
pen.left(90)
pen.forward(100)
'''

for side in range(4):
    pen.forward(100)
    pen.left(90)

#While loop that excutes 3 times
sides = 3

'''
while sides > 0:
    print(sides)
    sides = sides -1

'''
while sides > 0:
    pen.forward(100)
    pen.left(120)
    sides = sides -1
    
#wait for user to close window
win.mainloop()
