from pygame_functions import *
import random

VELOCITY = 1

class Person:
    def __init__(self, name, path, num_div, width, height):
        self.sprite = makeSprite(path, num_div)
        self.x, self.y = random.randint(0, width-20), random.randint(0, height-40)
        # can be 0="right", 1="up", 2="left", 3="down"
        self.last_position = 0
        # the index of the current sprite
        self.counter = 0
        # can be 0="right", 1="up", 2="left", 3="down"
        self.direction = 0
        self.frame = 0
        self.name = name
        # previously talked to
        self.prev_talked_to = None
        # how much longer they have to talk
        self.talking = 1000

    def update_pos(self):
        if self.counter > 0:
            self.counter -= 50
            if self.direction == 0:
                self.x += VELOCITY
                changeSpriteImage(self.sprite, 0*6 + self.frame)
            elif self.direction == 1:
                self.y -= VELOCITY
                changeSpriteImage(self.sprite, 1*6 + self.frame)
            elif self.direction == 2:
                self.x -= VELOCITY
                changeSpriteImage(self.sprite, 2*6 + self.frame)
            elif self.direction == 3:
                self.y += VELOCITY
                changeSpriteImage(self.sprite, 3*6 + self.frame)
        else:
            self.counter = random.randint(500, 1500)
            self.direction = random.randint(0, 4)
            changeSpriteImage(self.sprite, 0*6 + self.frame)

    def walk_to_target(self, target):
        print("yay")