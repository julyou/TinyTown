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
        town.add_person("adam", "sprites/Adam_run_16x16.png", 24, WIDTH, HEIGHT)
        town.add_person("amelia", "sprites/Amelia_run_16x16.png", 24, WIDTH, HEIGHT)
        town.add_person("eshana", "sprites/Amelia_run_16x16.png", 24, WIDTH, HEIGHT)

        for person in town.people.values():
            moveSprite(person.sprite, person.x, person.y, True)
            showSprite(person.sprite)

        while self.loop:
            if clock() > self.next_frame:
                for person in town.people.values():
                    person.frame = (person.frame + 1) % 6
                    moveSprite(person.sprite, person.x, person.y)
                    self.next_frame += 20
                    person.update_pos()

                if keyPressed("right"):
                    for person in town.people.values():
                        person.x += VELOCITY
                        changeSpriteImage(person.sprite, 0*6 + person.frame)
                        person.last_position = 0
                elif keyPressed("up"):
                    for person in town.people.values():
                        person.y -= VELOCITY
                        changeSpriteImage(person.sprite, 1*6 + person.frame)
                        person.last_position = 1
                elif keyPressed("left"):
                    for person in town.people.values():
                        person.x -= VELOCITY
                        changeSpriteImage(person.sprite, 2*6 + person.frame)
                        person.last_position = 2
                elif keyPressed("down"):
                    for person in town.people.values():
                        person.y += VELOCITY
                        changeSpriteImage(person.sprite, 3*6 + person.frame)
                        person.last_position = 3
            tick(120)

        endWait()

if __name__ == '__main__':
    game = GameEngine("Acorn Hill", 700, 500)
    game.run()