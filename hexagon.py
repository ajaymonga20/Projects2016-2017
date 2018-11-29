 # Ajay - Nov 26 - Initial Programming  
 # imports 7
import turtle 
import random 
 
 # functions
def shape(myturtle,length,sides,angles): 
	myturtle.color(getRGB()) 
  for i in range(sides): 
       myturtle.forward(length) 
       myturtle.right(angles) 
 
def row(myturtle,numshapes): 
    for i in range(3): 
        shape(joe,50,6,45)
        joe.penup()
        joe.right(90) 
        joe.forward(50) 
        joe.left(90) 
        joe.pendown()
def getRGB(): 
     r = random.randint(0,255) 
     g = random.randint(0,255) 
     b = random.randint(0,255) 
     return (r,g,b) 
 

 # main code 
joe = turtle.Turtle() 
joe.left(90) 
turtle.colormode(255)
 for i in range(3): 
     row(joe,3) 
     joe.penup()
     joe.left(90) 
     joe.forward(3*50) 
     joe.right(90) 
     joe.forward(50) 
     joe.pendown() 
                                                                                                                                                                                                        
  turtle.done()

