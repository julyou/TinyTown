from pygame_functions import *
from utils import Cache, astar
from event import Event
from mask_loader import MaskLoader
import random

VELOCITY = 1

class Person:
    def __init__(self, name, path, num_div, width, height):
        self.sprite = makeSprite(path, num_div)
        #self.x, self.y = random.randint(0, width-20), random.randint(0, height-40)
        self.x, self.y = width / 3, height / 2
        self.truex = self.x + 20
        self.truey = self.y + 70
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
        self.walking = False
        self.target = None

        # time to live for message
        self.ttl = 0
        # current message being transmitted
        self.message = ""
        
        # short term memory
        self.cache = Cache()

        # long term memory
        #   - dictionary of events
        #   - keeps track of up to N events
        #   - directed acyclic graph
        self.conversations = {}

    def update_pos(self, mask):
        if self.target:
            self.walk_to_target(mask, self.target)
        if self.counter > 0:
            self.counter -= 50
            if self.direction == 0:
                if mask.pix[self.truex + VELOCITY, self.truey] != (0, 0, 0, 255):
                    self.x += VELOCITY
                    self.truex += VELOCITY
                changeSpriteImage(self.sprite, 0*6 + self.frame)
            elif self.direction == 1:
                if mask.pix[self.truex, self.truey - VELOCITY] != (0, 0, 0, 255):
                    self.y -= VELOCITY
                    self.truey -= VELOCITY
                changeSpriteImage(self.sprite, 1*6 + self.frame)
            elif self.direction == 2:
                if mask.pix[self.truex - VELOCITY, self.truey] != (0, 0, 0, 255):
                    self.x -= VELOCITY
                    self.truex -= VELOCITY
                changeSpriteImage(self.sprite, 2*6 + self.frame)
            elif self.direction == 3:
                if mask.pix[self.truex, self.truey + VELOCITY] != (0, 0, 0, 255):
                    self.y += VELOCITY
                    self.truey += VELOCITY
                changeSpriteImage(self.sprite, 3*6 + self.frame)
        else:
            self.counter = random.randint(500, 1500)
            self.direction = random.randint(0, 4)
            changeSpriteImage(self.sprite, 0*6 + self.frame)

    def walk_to_target(self, mask, target):
        path = astar(mask, (self.truex, self.truey), (target.truex, target.truey))
        print(path)
        return path

    # returns empty string when time limit expires
    #   - constructs an event and adds it to target's ltm and stm
    #   - also adds the message into the target's long term memory
    def talk_to_target(self, target, time, messages):
        if not self.talking:
            message = self.get_message(messages)
            self.talking = True
            target.talking = True
            self.message = message
            self.ttl = random.randint(750, 1500)

            # event constructed with target as self-parent and self as other-parent
            event = Event(time, message, target, self)
            # each event's id is its time of creation
            target.conversations[time] = event
            target.cache.read(event, clock())
            print(message)
            print(target.conversations)
            return message
        return ""

    def get_message(self, messages):
        randint = random.randint(0, 100)

        if not self.cache.heap or randint < 50:
            index = random.randint(0, len(messages)-1)
            # 50% chance to generate a new event, or generate if there is nothing
            # stored in cache
            return messages[index]
        # 50% chance to retrieve an old event from stm
        index = random.randint(0, min(self.cache.num_occupied-1, self.cache.size-1))
        return self.cache.heap[index][1].message