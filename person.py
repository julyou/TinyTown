from pygame_functions import *
from utils import Cache, astar
from event import Event
from mask_loader import MaskLoader
from people import People
import random

VELOCITY = 1

class Person:
    def __init__(self, name, path, num_div, width, height):
        self.sprite = makeSprite(path, num_div)
        self.x, self.y = random.randint(0, width-20), random.randint(0, height-40)
        # self.x, self.y = random.randint(0, 1000), random.randint(0, 50)

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

    def walk_to_target(self, pix, target):
        path = astar(pix, (self.x, self.y), (target.x, target.y))
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


mask = MaskLoader("masks/background_mask.png")

town = People()
town.add_person("adam", "sprites/Adam_run_16x16.png", 24, 700, 500)
town.add_person("amelia", "sprites/Amelia_run_16x16.png", 24, 700, 500)
print(town["adam"].walk_to_target(mask.pix, town["amelia"]))