import turtle


arrow = turtle.Turtle()
arrow.speed(0)

def square():
    for lines in range(3):
        arrow.forward(100)

        arrow.left(90)

    for lines in range(4):

        arrow.forward(100)

        arrow.right(90)
    
   
    arrow.forward(200)

    for lines in range(2):

        arrow.right(90)

        arrow.forward(100)

    arrow.right(90)

    arrow.forward(200)

    for lines in range(2):

        arrow.right(90)

        arrow.forward(100)


def diamond():

    arrow.right(45)

    for lines in range(3):

        arrow.forward(141)

        arrow.right(90)

    arrow.forward(141)


def one():
    square()
    diamond()
    arrow.left(225)
    arrow.forward(100)
 

def octagon(): 
    for octs in range(7):
      arrow.forward(100)
      arrow.left(45) 
   
    arrow.forward(100)
    arrow.right(45/2)  


for octogon in range(16):
        
    octagon() 

one()

d = arrow.right
a = arrow.left
w = arrow.forward

def eye(angle,agle,leng):
    for lines in range(3):
        w(leng)
        a(agle)    
    w(leng)
    a(angle)

for i in range(360):
    eye(89,90,100)
#By: Helmzyy
