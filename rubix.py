# rubix.py
# Ajay - December 2 - Com Sci Test

# imports 
import turtle 
import random 

# functions
def shape(myturtle,length,sides,angles): 
	myturtle.color(getRGB())
	myturtle.pencolor(255, 255, 255)  
	for i in range(sides): 
		myturtle.forward(length) 
		myturtle.right(angles) 

def row(myturtle,numshapes): 
	for i in range(8): 
		joe.begin_fill()
		shape(joe,30,4,90)
		turtle.pencolor(255, 250, 250) 
		joe.penup()  
		joe.right(90) 
		joe.forward(30) 
		joe.left(90) 
		joe.pendown()
		joe.end_fill()
def getRGB(): 
	r = random.randint(0,255) 
	g = random.randint(0,255) 
	b = random.randint(0,255) 
	return (r,g,b) 
# main code 
joe = turtle.Turtle() 
joe.left(90) 
turtle.colormode(255)
for i in range(8): 
	row(joe,3) 
	joe.penup()
	joe.left(90) 
	joe.forward(8*30) 
	joe.right(90) 
	joe.forward(30) 
	joe.pendown() 

joe.forward(30) 
joe.right(90) 
joe.pendown() 
joe.pencolor(0,0,0) 
joe.forward(30*9)
joe.right(90)  
joe.forward(30*10) 
joe.right (90) 
joe.forward(30*10)
joe.right(90) 
joe.forward(30*10) 
joe.right(90)
joe.forward(30*10) 
turtle.done()






 
 
