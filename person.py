from pygame_functions import *

class Person:
    def __init__(self, name, path, num_div):
        self.sprite = makeSprite(path, num_div)
        self.x, self.y = 0.0, 0.0
        # can be 0="right", 1="up", 2="left", 3="down"
        self.last_position = 0
        # the index of the current sprite
        self.frame = 0
        self.name = name

    def update_pos(self, keypressed):
        self.frame = (self.frame + 1) % 6
