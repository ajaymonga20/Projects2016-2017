import pygame 

class TestGame: 

	def __init__ (self, title): 
		self.ballX = 200 
		self.ballY = 200
		self.caption = title 

	def run(self): 
		self.running = True 
		
		pygame.display.set_caption(self.caption) 
		screen = pygame.display.get_surface() 

		while self.running: 
			for event in pygame.event.get(): 
				if event.type == pygame
