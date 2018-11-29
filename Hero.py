# Hero.py Class template for my hero 



class Hero: 

	def __init__(self,x,y,img): 
		self.xcoord = x
		self.ycoord = y 
		self.imgname = img 
		self.health = 100 

	def eatFood(self): 
		self.health = self.health + 10 

