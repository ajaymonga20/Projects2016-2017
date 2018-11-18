# pong: hit the ball with the paddle
#
# use the escape key to exit
#
# on the XO, the escape key is the top lefthand key,
# circle with an x in it.

#import pippy
import pygame
import sys
from pygame.locals import *
from random import *

# always need to init first thing
pygame.init()

# create the window and keep track of the surface
# for drawing into
# HOEL
#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.display.set_mode((800, 600))

# ask for screen's width and height
size = width, height = screen.get_size()

# turn off the cursor - HOEL change
pygame.mouse.set_visible(True)

# turn on key repeating (repeat 40 times per second)
pygame.key.set_repeat(25, 25)

# start the screen all black
bgcolor = (0, 255, 0)
screen.fill(bgcolor)

# paddle constants
paddle_width = 20
paddle_length = 200
paddle_radius = paddle_length / 2
paddle_color = (250, 250, 250)
step = 6  # paddle moves 3 pixels at a go

# ball constants
ball_color = (250, 250, 250)
ball_radius = 25

# game constants
fsize = 48
# HOEL
#msg = 'Press \'g\' to start game'
msg = "click on yoda to start game"

font = pygame.font.Font(None, fsize)
text = font.render(msg, True, (250, 250, 250))
textRect = text.get_rect()

# HOEL - change
textRect.x = 10
textRect.y = 10
#textRect.centerx = screen.get_rect().centerx
#textRect.centery = screen.get_rect().centery

# must use python3 to use .jpg or .png otherwise .bmp for python2.7
# 680x580 pixel image
asurf = pygame.image.load('yoda.png')
imgRect = asurf.get_rect()
imgRect.x = 100
imgRect.y = 100

# HOEL - keep score
score = 0
scoretext = font.render("Score: " + str(score), True, (250, 250, 250))
scoreRect = scoretext.get_rect()
scoreRect.x = 50
scoreRect.y = 500

# HOEL - make a sound
pygame.mixer.music.load("hit.wav")


#while pippy.pygame.next_frame(): - HOEL
while True:

    # display msg
    screen.fill(bgcolor)
    screen.blit(text, textRect)

    # HOEL - blit the image
    screen.blit(asurf,imgRect)

    # draw to screen
    pygame.display.flip()

    # chill until a key is pressed
    for idle_event in pygame.event.get():
        if idle_event.type == QUIT:
            sys.exit()


        # HOEL - check for mousebuttondown event
        # http://www.pygame.org/docs/ref/event.html
        if idle_event.type == MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] > 100 and pygame.mouse.get_pos()[1] > 100:
              
        # HOEL commented out in favour of click
        #if idle_event.type == KEYDOWN:
        #    if idle_event.key == K_ESCAPE:
        #        sys.exit()

        #    if idle_event.key == 103:  # g key

                # play a game!

                # start the paddle in the center
                paddle_location = height / 2

                # number of balls to a game
                balls = 4

                while balls > 0:

                    ball_position = [ball_radius, ball_radius]

                    # HOEL - changed speed from random int between (3,5) to (7,10)
                    ball_mvect = [randint(7, 10), randint(7, 10)]
                    ball_limit = size
                    balls = balls - 1

                    while ball_position[0] + ball_radius < ball_limit[0]:  # in play

                        for event in pygame.event.get():
                            if event.type == QUIT:
                                sys.exit()

                            elif event.type == KEYDOWN:
                                if event.key == K_ESCAPE:
                                    sys.exit()
                                elif event.key == 273 \
                                    or event.key == 265 \
                                    or event.key == 264:  # up
                                    paddle_location = paddle_location - step
                                elif event.key == 274 \
                                    or event.key == 259 \
                                    or event.key == 258:  # down
                                    paddle_location = paddle_location + step

                        # make sure the paddle is in-bounds
                        if paddle_location - paddle_radius < 0:
                            paddle_location = paddle_radius
                        elif paddle_location + paddle_radius >= height:
                            paddle_location = height - 1 - paddle_radius

                        # clear the screen
                        screen.fill(bgcolor)

								# HOEL - draw the score
                        scoretext = font.render("Score: " + str(score), True, (250, 250, 250))
                        screen.blit(scoretext,scoreRect)

                        # draw the paddle on the right side of the screen
                        pygame.draw.line(screen,
                                        paddle_color,
                                        (width - paddle_width, paddle_location -
                                        paddle_radius),
                                        (width - paddle_width,
                                        paddle_location + paddle_radius),
                                        paddle_width)

                        # draw the ball
                        pygame.draw.circle(screen, ball_color, ball_position, ball_radius)

                        # draw the unused balls
                        for i in range(balls):
                            pygame.draw.circle(screen, ball_color,
                                 (int(round(30 + i * ball_radius * 2.4)), 30),
                                 ball_radius)

                        # update the display
                        pygame.display.flip()

                        # update the ball
                        for i in range(2):
                            ball_position[i] = ball_position[i] + ball_mvect[i]

                            # bounce on top and left
                            if ball_position[i] < ball_radius:
                                ball_position[i] = ball_radius
                                ball_mvect[i] = -1 * ball_mvect[i]
                            # bounce on bottom
                            elif i == 1 \
                                and ball_position[i] >= ball_limit[i] - ball_radius:
                                ball_position[i] = ball_limit[i] - ball_radius - 1
                                ball_mvect[i] = -1 * ball_mvect[i]

                            elif i == 0 \
                                and ball_position[i] >= ball_limit[i] - ball_radius - paddle_width \
                                and ball_position[1] > paddle_location - paddle_radius \
                                and ball_position[1] < paddle_location + paddle_radius:
                                ball_position[i] = ball_limit[i] - ball_radius - paddle_width - 1
                                ball_mvect[i] = (-1) * ball_mvect[i]

                                # HOEL
                                score = score + 1
                                pygame.mixer.music.play()
                                
