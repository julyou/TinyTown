import pygame
from sys import exit
from pygame_functions import *
pygame.init()

# constants
WIDTH = 650
HEIGHT = 300
ADAM_STARTING_X = WIDTH * 0.5
ADAM_STARTING_Y = HEIGHT * 0.5
SCROLL = 5
VELOCITY = 1

screenSize(WIDTH, HEIGHT)
setBackgroundImage('graphics/lake.png')

adamSprite = makeSprite('adam/Adam_run_16x16.png', 24)
moveSprite(adamSprite, WIDTH * 0.5, HEIGHT * 0.5, True)
showSprite(adamSprite)

nextFrame = clock()
frame = 0

last_position = 0
curr_x = ADAM_STARTING_X
curr_y = ADAM_STARTING_Y
bkg = 1 # 1 for lake, 2 for stardew

while True:
    if clock() > nextFrame:
        frame = (frame + 1) % 6
        nextFrame += 60

    if keyPressed("right"):
        curr_x += VELOCITY
        changeSpriteImage(adamSprite, 0*6 + frame)
        last_position = 0
        if (curr_x >= WIDTH and bkg == 1):
            setBackgroundImage('graphics/StarDew-Screenshot.webp')
            curr_x = 0
            bkg = 2
        elif (curr_x >= WIDTH and bkg == 2):
            print("got here")
            curr_x = WIDTH
    elif keyPressed("up"):
        curr_y -= VELOCITY
        changeSpriteImage(adamSprite, 1*6 + frame)
        last_position = 1
        # if (curr_y < 0):
        #     setBackgroundImage('graphics/StarDew-Screenshot.webp')
        #     curr_y = HEIGHT 
    elif keyPressed("left"):
        curr_x -= VELOCITY
        changeSpriteImage(adamSprite, 2*6 + frame)
        last_position = 2
        if (curr_x < 0):
            setBackgroundImage('graphics/lake.png')
            curr_x = WIDTH 
    elif keyPressed("down"):
        curr_y += VELOCITY
        changeSpriteImage(adamSprite, 3*6 + frame)
        last_position = 3
        # if (curr_y > HEIGHT):
        #     setBackgroundImage('graphics/lake.png')
        #     curr_y = 0
    if keyPressed("space"): # jump
        moveSprite(adamSprite, curr_x, curr_y-10)
        pause(150)
        moveSprite(adamSprite, curr_x, curr_y)
    else:
        changeSpriteImage(adamSprite,last_position *6 + 2)
    
    moveSprite(adamSprite, curr_x, curr_y)
    tick(120)

endWait()