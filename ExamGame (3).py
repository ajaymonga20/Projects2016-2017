#!/usr/bin/python
import pygame
import random
import time
import sys
#from gi.repository import Gtk

class ExamGame:

    def __init__(self,title):
        self.x = 300
        self.y = 300
        self.caption = title 

    def write_file(self, file_path):
        pass

    def read_file(self, file_path):
        pass

    def run(self):

        def randcol():
            r = random.randint(0,255) 
            g = random.randint(0,255)
            b = random.randint(0,255)
            screen.fill((r,g,b))

        asurf = pygame.image.load('ball.png')
        ball = asurf.get_rect()

        try:
            sound1 = pygame.mixer.Sound("boing.wav")
        except:
            print ("cannot find sound file")
            sys.exit()

        pygame.key.set_repeat(25,25)

        keepgoing = True
        running = True
      
        pygame.display.set_caption(self.caption)
        screen = pygame.display.get_surface()
        score = 0
        while keepgoing:
            msg2 = "Welcome To My Exam Game, Click To Continue"
            font2 = pygame.font.Font(None, 48)
            text2 = font2.render(msg2, True, (0,0,0))
            screen.fill((255,255,255))
            screen.blit(text2,(375,400))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    keepgoing = False
        while running:

            screen.fill((255,255,255))
#           while Gtk.events_pending():
#              Gtk.main_iteration()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.VIDEORESIZE:
                    pygame.display.set_mode(event.size, pygame.RESIZABLE)
                elif event.type == pygame.KEYDOWN:
                    screen.fill((255,255,255))
#                    randcol()
                    if event.key == pygame.K_LEFT:
                        self.x -= 10
                        score = score + 1
                    elif event.key == pygame.K_RIGHT:
                        self.x += 10
                        score = score + 1
                    elif event.key == pygame.K_DOWN:
                        self.y += 10
                        score = score + 1
                    elif event.key == pygame.K_UP:
                        self.y -= 10
                        score = score + 1
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.x,self.y = pygame.mouse.get_pos()
                    screen.fill((255,255,255))
#                    randcol()
            if self.x >= 1372:
                self.x -= 40
                sound1.play()
                score = 0
            elif self.x <= 0:
                self.x += 40
                sound1.play()
                score = 0
            elif self.y >= 835:
                self.y -= 40
                sound1.play()
                score = 0
            elif self.y <= 0:
                self.y += 40
                sound1.play()
                score = 0
            msg = "Move The Ball With Arrow Keys"
            font = pygame.font.Font(None, 48)
            text = font.render(msg, True, (0,0,0))
            msg3 = "Score: " + str(score)
            text3 = font.render(msg3, True, (0,0,0))
            asurf = pygame.image.load('ball.png')
            ball = asurf.get_rect()
            screen.blit(asurf, (self.x,self.y))
            screen.blit(text,(475,100))
            screen.blit(text3,(475,150))
#            pygame.draw.circle(screen, (255,0,0), (self.x, self.y), 30)
            pygame.display.flip()

def main():
    pygame.init()
    pygame.display.set_mode((0, 0), pygame.RESIZABLE)
    game = ExamGame("My Exam Game")
    game.run()

if __name__ == '__main__':
    main()
