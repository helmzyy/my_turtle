import turtle


my_turtle = turtle.Turtle()
my_turtle.speed(0)

def square():
    for lines in range(3):
        my_turtle.forward(100)

        my_turtle.left(90)

    for lines in range(4):

        my_turtle.forward(100)

        my_turtle.right(90)
    
   
    my_turtle.forward(200)

    for lines in range(2):

        my_turtle.right(90)

        my_turtle.forward(100)

    my_turtle.right(90)

    my_turtle.forward(200)

    for lines in range(2):

        my_turtle.right(90)

        my_turtle.forward(100)


def diamond():

    my_turtle.right(45)

    for lines in range(3):

        my_turtle.forward(141)

        my_turtle.right(90)

    my_turtle.forward(141)


def one():
    square()
    diamond()
    my_turtle.left(225)
    my_turtle.forward(100)
 

def octagon(): 
    for octs in range(7):
      my_turtle.forward(100)
      my_turtle.left(45) 
   
    my_turtle.forward(100)
    my_turtle.right(45/2)  


for octogon in range(16):
        
    octagon() 

one()
arrow = turtle.Turtle()

d = arrow.right
a = arrow.left
w = arrow.forward

arrow.speed(0)

def square(angle,agle,leng):
    w(leng)
    a(agle)
    w(leng)
    a(agle)
    w(leng)
    a(agle)
    w(leng)
    a(angle)

for i in range(360):
    square(89,90,100)
#By: Helmzyy
