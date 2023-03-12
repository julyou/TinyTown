import pygame
from people import People
from pygame_functions import *

WIDTH = 700
HEIGHT = 500
ADAM_STARTING_X = WIDTH * 0.5
ADAM_STARTING_Y = HEIGHT * 0.5
SCROLL = 5
VELOCITY = 5

class GameEngine:
    def __init__(self, name, width, height):
        pygame.init()
        screenSize(width, height)
        self.next_frame = clock()
        self.loop = True
        self.messages = self.read_file("conversations.txt")
        setBackgroundImage("graphics/junkyard2.png")

        speech = makeLabel("hi", 40, 0, 0, fontColour='white', font='TTF/dogicabold.ttf', background="clear")
        showLabel(speech)

        text_box = makeTextBox(WIDTH*0.2, HEIGHT * 0.8, WIDTH * 0.6)
        textBoxInput(text_box)
        showTextBox(text_box)

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

        for person in town.people.values():
            moveSprite(person.sprite, person.x, person.y, True)
            showSprite(person.sprite)


        while self.loop:
            if clock() > self.next_frame:
                for person in town.people.values():
                    person.frame = (person.frame + 1) % 6
                    moveSprite(person.sprite, person.x, person.y)
                    self.next_frame += 10
                    person.update_pos()
                town.initiate_convo(clock(), self.messages)

                if keyPressed("right"):
                    scrollBackground(-10, 0)
                    for person in town.people.values():
                        if person.x < WIDTH-20:
                            person.x += VELOCITY
                        changeSpriteImage(person.sprite, 0*6 + person.frame)
                        person.last_position = 0
                elif keyPressed("up"):
                    scrollBackground(0, 10)
                    for person in town.people.values():
                        if person.y > 0:
                            person.y -= VELOCITY
                        changeSpriteImage(person.sprite, 1*6 + person.frame)
                        person.last_position = 1
                elif keyPressed("left"):
                    scrollBackground(10, 0)
                    for person in town.people.values():
                        if person.x > 0:
                            person.x -= VELOCITY
                        changeSpriteImage(person.sprite, 2*6 + person.frame)
                        person.last_position = 2
                elif keyPressed("down"):
                    scrollBackground(0, -10)
                    for person in town.people.values():
                        if person.y < HEIGHT-40:
                            person.y += VELOCITY
                        changeSpriteImage(person.sprite, 3*6 + person.frame)
                        person.last_position = 3
            tick(120)

        endWait()

if __name__ == '__main__':
    game = GameEngine("Acorn Hill", 700, 500)
    game.run()