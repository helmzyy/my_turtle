import turtle


#thx fortune for the savior function


my_turtle = turtle.Turtle()


#square
def square():
    my_turtle.forward(100)

    my_turtle.left(90)

    my_turtle.forward(100)

    my_turtle.left(90)

    my_turtle.forward(100)

    my_turtle.left(90)

    my_turtle.forward(100)

    my_turtle.right(90)

    my_turtle.forward(100)

    my_turtle.right(90)

    my_turtle.forward(100)

    my_turtle.right(90)

    my_turtle.forward(100)

    my_turtle.right(90)

    my_turtle.forward(200)

    my_turtle.right(90)

    my_turtle.forward(100)

    my_turtle.right(90)

    my_turtle.forward(100)

    my_turtle.right(90)

    my_turtle.forward(200)

    my_turtle.right(90)

    my_turtle.forward(100)

    my_turtle.right(90)

    my_turtle.forward(100)

def diamond():

    my_turtle.right(45)

    my_turtle.forward(141)

    my_turtle.right(90)

    my_turtle.forward(141)

    my_turtle.right(90)

    my_turtle.forward(141)

    my_turtle.right(90)

    my_turtle.forward(141)


def one():
    square()
    diamond()
    my_turtle.left(225)
    my_turtle.forward(100)
 

def octagon(): 

  my_turtle.forward(100)
  my_turtle.left(50) 
  my_turtle.forward(100) 
  my_turtle.left(40) 
  my_turtle.forward(100) 
  my_turtle.left(50) 
  my_turtle.forward(100) 
  my_turtle.left(40) 
  my_turtle.forward(100) 
  my_turtle.left(50) 
  my_turtle.forward(100) 
  my_turtle.left(39) 
  my_turtle.forward(100) 
  my_turtle.left(50) 
  my_turtle.forward(100)
    


for octogon in range(9):
        
    octagon() 
    
one()

#By: Helmzyy
