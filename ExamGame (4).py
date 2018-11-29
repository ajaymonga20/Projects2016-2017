#!/usr/bin/python
import pygame
#from gi.repository import Gtk

class ExamGame:

    def __init__(self):
        self.x = 300
        self.y = 300

    def write_file(self, file_path):
        pass

    def read_file(self, file_path):
        pass

    def run(self):
        running = True
        screen = pygame.display.get_surface()

        while running:
           # while Gtk.events_pending():
               # Gtk.main_iteration()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.VIDEORESIZE:
                    pygame.display.set_mode(event.size, pygame.RESIZABLE)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.x -= 5

            pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), 30)
            pygame.display.flip()

def main():
    pygame.init()
    pygame.display.set_mode((0, 0), pygame.RESIZABLE)
    game = ExamGame()
    game.run()

if __name__ == '__main__':
    main()
