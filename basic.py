'''
A?
'''

#imports
import pygame

#functions

#main code
pygame.init() #e
pygame.display.set_mode((600,400)) #F?
screen = pygame.display.get_surface() #G

#H?
ballX = 200
ballY = 200

keeprunning = True #I
while keeprunning: #J

	#k
	for event in pygame.event.get():
		if event.type == pygame.QUIT: #L
			keeprunning = False #m
		elif event.type == pygame.KEYDOWN: #n
			if event.key == pygame.K_LEFT: #O
				ballX = ballX - 10 # P
			elif event.key == pygame.K_RIGHT: 
				ballX = ballX + 10 # P
			elif event.key == pygame.K_DOWN:
				ballY = ballY + 10 
			elif event.key == pygame.K_UP:
				ballY = ballY - 10    



	pygame.draw.circle(screen, (255,0,0), (ballX, ballY), 30) #q
	pygame.display.flip() #r

