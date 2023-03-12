from pygame_functions import *
from utils import Cache
import random

VELOCITY = 1

class Person:
    def __init__(self, name, path, num_div, width, height):
        self.sprite = makeSprite(path, num_div)
        self.x, self.y = random.randint(0, width-20), random.randint(0, height-40)
        self.width, self.height = width, height
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
        
        # point system
        self.motivation = random.randint(0, 100)
        self.happy = random.randint(0, 100)
        self.sad = random.randint(0, 100)
        self.talking = False
        self.time_to_talk = 0
        
        # short term memory
        self.cache = Cache()

        # long term memory
        #   - dictionary of events
        #   - keeps track of up to N events
        #   - directed acyclic graph
        conversations = {}


    def update_pos(self):
        if self.counter > 0:
            self.counter -= 50
            if self.direction == 0:
                if self.x < self.width-20:
                    self.x += VELOCITY
                changeSpriteImage(self.sprite, 0*6 + self.frame)
            elif self.direction == 1:
                if self.y > 0:
                    self.y -= VELOCITY
                changeSpriteImage(self.sprite, 1*6 + self.frame)
            elif self.direction == 2:
                if self.x > 0:
                    self.x -= VELOCITY
                changeSpriteImage(self.sprite, 2*6 + self.frame)
            elif self.direction == 3:
                if self.y < self.height-40:
                    self.y += VELOCITY
                changeSpriteImage(self.sprite, 3*6 + self.frame)
        else:
            self.counter = random.randint(500, 1500)
            self.direction = random.randint(0, 4)
            changeSpriteImage(self.sprite, 0*6 + self.frame)

    def walk_to_target(self, target):
        #TODO
        print("yay")

    def talk_to_target(self, target):
        if not self.talking:
            message = self.get_message()
        else:
            self.talking = True

    def get_message(self):
        randint = random.randint(0, 100)
        if randint < 25:
            # 25% chance to generate a new event
            return "" # TODO
        # 75% chance to retrieve an old event from stm
        index = random.randint(0, self.cache.size-1)
        return self.cache.heap[index]

