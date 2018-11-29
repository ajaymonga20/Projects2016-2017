import turtle
import random  

def hex(length,sides,angle): 
	turtle.color(getRGB()) 
	turtle.begin_fill()
	for i in range(sides): 
		turtle.forward(length)
		turtle.left(angle)
	turtle.end_fill() 

def row(numshapes): 
	for i in range(numshapes): 
		hex(50,6,60)
		turtle.penup()
		turtle.forward(2 * 50) 
		turtle.pendown()

def getRGB(): 
	r = random.randint(0,255) 
	g = random.randint(0,255) 
	b = random.randint(0,255) 
	return (r,g,b) 






joe = turtle.Turtle() 
turtle.colormode(255)
for i in range(4): 
	row(4) 
	turtle.penup()
	turtle.back(400) 
	turtle.left(90)
	turtle.forward(86.60254) 
	turtle.right(90)
	turtle.pendown()

turtle.done 




