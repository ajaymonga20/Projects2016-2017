

#import gtk
import pygame
import math
import sys
from pygame.locals import *
from random import *
#from gettext import gettext as _

class TestGame: 

	def __init__(self):
		#starting variables
		#self.rect = self.image.get_rect()
		self.hole = 0
		self.birdX = 100
		self.birdY = 200
		self.flag = 0	
		self.keyinit = 0
		self.keytest = 0
		
	def run(self):
		#sound loads
		self.angle = 0
		self.center_x = 0
		self.center_y = 0
		self.sound = True
		self.clock = pygame.time.Clock()	
		self.speed2 = 0
		self.speed = 0
		gravity = 0.1
		
		bird = pygame.image.load("flaps.png")
		bird2 = pygame.transform.scale(bird, (30,30))
		gameDisplay = pygame.display.set_mode((600,400))
			
		try:
			pygame.mixer.init()
		except err:
			self.sound = False
			print ('error with sound') 

		self.info = pygame.display.Info()

		self.screen = pygame.display.get_surface()
		
		pygame.display.set_caption("Flappy Golf")
		
		#self.move = pygame.mixer.Sound(" ")
		#self.die = pygame.mixer.Sound(" ")
		#self.win = pygame.mixer.Sound(" ")
		#self.background = pygame.mixer.Sound(" ")
		keeprunning = True
		
		while keeprunning:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					keeprunning = False
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LEFT:
						self.birdX *= 0.9
						self.birdY -= 60
						self.birdY = self.birdY - self.speed 
						score = score + 1

						#self.bird = self.birdY + speed
						#speed = speed + gravity
						#if self.birdY > 400:
							#speed = speed * - 1
					elif event.key == pygame.K_RIGHT:
						self.birdX *= 1.10
						self.birdY -= 100
						score = score + 1

			self.screen.fill((255,255,255))
			gameDisplay.blit(bird2, (self.birdX, self.birdY))
			self.birdY = self.birdY + self.speed
			self.speed = self.speed + gravity
			if self.birdY > 350:
				self.speed = 0
			pygame.display.update()
			self.clock.tick(40)

	#def update(self):
      # Calculate a new x, y
		#self.rect.x = self.radius * math.sin(self.angle) + self.center_x
		#self.rect.y = self.radius * math.cos(self.angle) + self.center_y
 
        # Increase the angle in prep for the next round.
		#self.angle += self.speed

myfont = pygame.font.SysFont("arial", 15)



score = 0
scoretext = myfont.render("Score: " + str(score), True, (250, 250, 250))
scoreRect = scoretext.get_rect()
scoreRect.x = 50
scoreRect.y = 500
#label = myfont.render("Some text!", 1, (255,255,0))
#screen.blit(label, (100, 100))

#score = score + 1

def main():
	pygame.init()
	game = TestGame()
	game.run()

if __name__ == '__main__':
	main()
