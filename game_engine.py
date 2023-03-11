import pygame
from people import People
from pygame_functions import *

WIDTH = 700
HEIGHT = 500
ADAM_STARTING_X = WIDTH * 0.5
ADAM_STARTING_Y = HEIGHT * 0.5
SCROLL = 5
VELOCITY = 1

class GameEngine:
    def __init__(self, name, width, height):
        pygame.init()
        screenSize(width, height)
        self.next_frame = clock()
        self.loop = True

    def run(self):
        town = People()
        town.add_person("adam", "sprites/Adam_run_16x16.png", 24)

        for person in town.people.values():
            moveSprite(person.sprite, WIDTH * 0.5, HEIGHT * 0.5, True)
            showSprite(person.sprite)

        while self.loop:
            if clock() > self.next_frame:
                for person in town.people.values():
                    person.frame = (person.frame + 1) % 6
                    self.next_frame += 60

                    if keyPressed("right"):
                        person.x += VELOCITY
                        changeSpriteImage(person.sprite, 0*6 + person.frame)
                        person.last_position = 0
                        if (person.x >= WIDTH and bkg == 1):
                            person.x = 0
                            bkg = 2
                    elif keyPressed("up"):
                        person.y -= VELOCITY
                        changeSpriteImage(person.sprite, 1*6 + person.frame)
                        person.last_position = 1
                    elif keyPressed("left"):
                        person.x -= VELOCITY
                        changeSpriteImage(person.sprite, 2*6 + person.frame)
                        person.last_position = 2
                    elif keyPressed("down"):
                        person.y += VELOCITY
                        changeSpriteImage(person.sprite, 3*6 + person.frame)
                        person.last_position = 3
                    
                    moveSprite(person.sprite, person.x, person.y)
            tick(120)

        endWait()

if __name__ == '__main__':
    game = GameEngine("Acorn Hill", 700, 500)
    game.run()