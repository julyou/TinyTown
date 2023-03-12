import pygame
from people import People
from pygame_functions import *

WIDTH = 700
HEIGHT = 500
ADAM_STARTING_X = WIDTH * 0.5
ADAM_STARTING_Y = HEIGHT * 0.5
SCROLL = 10
VELOCITY = 3

class GameEngine:
    def __init__(self, name, width, height):
        pygame.init()
        screenSize(width, height)
        self.next_frame = clock()
        self.loop = True
        self.messages = self.read_file("conversations.txt")
        setBackgroundImage("graphics/background.png")

        #speech = makeLabel("hi", 40, WIDTH*0.2, HEIGHT * 0.8, fontColour='white', font='TTF/dogicabold.ttf', background="clear")
        #showLabel(speech)

        # text_box = makeTextBox(WIDTH*0.2, HEIGHT * 0.8, WIDTH * 0.6)
        # textBoxInput(text_box)
        # showTextBox(text_box)

    def read_file(self, path):
        f = open(path, "r")
        lines = f.readlines()
        f.close()
        return lines

    def run(self):
        town = People()
        town.add_person("adam", "sprites/Adam_run_16x16.png", 24, WIDTH, HEIGHT)
        town.add_person("amelia", "sprites/Amelia_run_16x16.png", 24, WIDTH, HEIGHT)
        town.add_person("bob", "sprites/Bob_run_16x16.png", 24, WIDTH, HEIGHT)
        town.add_person("dave", "sprites/Bob_run_16x16.png", 24, WIDTH, HEIGHT)
        town.add_person("rina", "sprites/Bob_run_16x16.png", 24, WIDTH, HEIGHT)

        town.add_person("mc", "sprites/Amelia_run_16x16.png", 24, WIDTH, HEIGHT)
        mc = town.people["mc"]

        for person in town.people.values():
            moveSprite(person.sprite, person.x, person.y, True)
            showSprite(person.sprite)

        while self.loop:
            if clock() > self.next_frame:
                for person in town.people.values():
                    person.frame = (person.frame + 1) % 6
                    moveSprite(person.sprite, person.x, person.y)
                    if person != mc:
                        person.update_pos()
                self.next_frame += 40
                town.initiate_convo(clock(), self.messages)

                if keyPressed("right"):
                    if mc.x < WIDTH-20:
                        mc.x += VELOCITY
                    elif mc.x > WIDTH / 2:
                        scrollBackground(-SCROLL, 0)
                        for person in town.people.values():
                            if person != mc:
                                person.x -= SCROLL
                                
                    changeSpriteImage(mc.sprite, 0*6 + mc.frame)
                    mc.last_position = 0
                elif keyPressed("up"):
                    if mc.y > 0:
                        mc.y -= VELOCITY
                    elif mc.y < HEIGHT / 2:
                        scrollBackground(0, SCROLL)
                        for person in town.people.values():
                            if person != mc:
                                person.y += SCROLL
                    changeSpriteImage(mc.sprite, 1*6 + mc.frame)
                    mc.last_position = 1
                elif keyPressed("left"):
                    if mc.x > 0:
                        mc.x -= VELOCITY
                    elif mc.x < WIDTH / 2:
                        scrollBackground(SCROLL, 0)
                        for person in town.people.values():
                            if person != mc:
                                person.x += SCROLL
                    changeSpriteImage(mc.sprite, 2*6 + mc.frame)
                    mc.last_position = 2
                elif keyPressed("down"):
                    if mc.y < HEIGHT-40:
                        mc.y += VELOCITY
                    elif mc.y > HEIGHT / 2:
                        scrollBackground(0, -SCROLL)
                        for person in town.people.values():
                            if person != mc:
                                person.y -= SCROLL
                    changeSpriteImage(mc.sprite, 3*6 + mc.frame)
                    mc.last_position = 3
            tick(120)
        endWait()

if __name__ == '__main__':
    game = GameEngine("Acorn Hill", 700, 500)
    game.run()