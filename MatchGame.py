#!/usr/bin/python
import pygame
import os
import random
from Photo import Photo
#from gi.repository import Gtk

class MatchGame:

	def write_file(self, file_path):
		pass

	def read_file(self, file_path):
		pass

	def getRandomHand(self):
		disklocation = "students"
		answer = random.choice(os.listdir(disklocation))
		other = random.choice(os.listdir(disklocation))
		another = random.choice(os.listdir(disklocation))
		photo1 = Photo(os.path.abspath(disklocation + "/" + answer),answer[:-4],True)
		photo2 = Photo(os.path.abspath(disklocation + "/" + other),answer[:-4],False)
		photo3 = Photo(os.path.abspath(disklocation + "/" + another),answer[:-4],False)
		returnlist = [photo1,photo2,photo3]
		shuffledList = sorted(returnlist, key=lambda k: random.random())
		return shuffledList

	def run(self):
		msg = ""
		font = pygame.font.Font(None, 75)
		text = font.render(msg, True, (250, 250, 250))
		textRect = text.get_rect()
		textRect.x = 150 
		textRect.y = 50

		screen = pygame.display.get_surface()

		keepgoing = True
		while (keepgoing == True):

#			while Gtk.events_pending():
#				Gtk.main_iteration()

			screen.fill((0,0,0))

			photoX = 50
			photoY = 200
			photos = self.getRandomHand()
			clickRect = [50,250]
			for photo in photos:
				if (photo.answer == True):
					msg = photo.photoname
					clickRect = [photoX,photoX+250]
				try:
					newimg = pygame.image.load(photo.imgname)
					screen.blit(newimg,(photoX,photoY))
					photoX = photoX + 250
				except:
					print("Can not find image " + photo.imgname)

			text = font.render(msg, True, (250, 250, 250))
			screen.blit(text,(textRect.x,textRect.y))
			pygame.display.flip()

			keepwaiting = True
			while (keepwaiting):

#				while Gtk.events_pending():
#					Gtk.main_iteration()

				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						return
					elif (event.type == pygame.MOUSEBUTTONDOWN):
						if pygame.mouse.get_pos()[0] >= clickRect[0] and pygame.mouse.get_pos()[0] < clickRect[1]:
							keepwaiting = False
						


def main():
	pygame.init()
	pygame.display.set_mode((0,0),pygame.RESIZABLE)
	game = MatchGame()
	game.run()

if __name__ == '__main__':
	main()
