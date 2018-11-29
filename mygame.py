# My game.py 




import pygame 
from Hero import Hero 

# functions NDA 

# main code 
pygame.init() 
pygame.display.set_mode((600,400)) 

screen = pygame.display.get_surface() 

hockey = Hero(200,200,"Hockey.png") 
cricket = Hero(400,300, "Cricket.png") 
baseball = Hero(100,100, "Baseball.png") 

drawlist = [hockey,cricket,baseball] 

for hero in drawlist:
	screen.blit(pygame.image.load(hero.imgname),(hero.xcoord,hero.ycoord)) 

hockey.eatFood 
print(hockey.health)
 
pygame.display.flip() 

keepgoing = True 
while keepgoing: 

	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: 
			keepgoing = False 






