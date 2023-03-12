import pygame
from people import People
from pygame_functions import *
from mask_loader import MaskLoader
from PIL import Image

WIDTH = 700 
HEIGHT = 500
SCROLL = 3
VELOCITY = 3

class GameEngine:
    def __init__(self, name, width, height):
        pygame.init()
        screenSize(width, height)
        self.next_frame = clock()
        self.loop = True
        self.messages = self.read_file("conversations.txt")
        setBackgroundImage("graphics/background.png")
        setWindowTitle(name)

        self.width, self.height = width, height
        self.mc_actualx, self.mc_actualy = 0, 0
        self.mask = MaskLoader("masks/background_mask.png")

    def read_file(self, path):
        f = open(path, "r")
        lines = [line[:-1] for line in f]
        f.close()
        return lines

    def run(self):
        town = People()       
        town.add_person("bob", "sprites/Bob_run_16x16.png", 24, self.width, self.height)
        town.add_person("dave", "sprites/Bob_run_16x16.png", 24, self.width, self.height)
        town.add_person("rina", "sprites/Bob_run_16x16.png", 24, self.width, self.height)
        town.add_person("alex", "sprites/Alex_run_16x16.png", 24, self.width, self.height)
        town.add_person("jamie", "sprites/Adam_run_16x16.png", 24, self.width, self.height)
        town.add_person("megan", "sprites/Amelia_run_16x16.png", 24, self.width, self.height)
        town.add_person("sam", "sprites/Bob_run_16x16.png", 24, self.width, self.height)
        town.add_person("conny", "sprites/Bob_run_16x16.png", 24, self.width, self.height)
        town.add_person("jomari", "sprites/Bob_run_16x16.png", 24, self.width, self.height)
        town.add_person("kai", "sprites/Alex_run_16x16.png", 24, self.width, self.height)
        town.add_person("marge", "sprites/Amelia_run_16x16.png", 24, self.width, self.height)
        town.add_person("barb", "sprites/Bob_run_16x16.png", 24, self.width, self.height)
        town.add_person("aisha", "sprites/Bob_run_16x16.png", 24, self.width, self.height)
        town.add_person("noah", "sprites/Bob_run_16x16.png", 24, self.width, self.height)
        town.add_person("avery", "sprites/Alex_run_16x16.png", 24, self.width, self.height)

        town.add_person("mc", "sprites/Amelia_run_16x16.png", 24, self.width, self.height)
        mc = town.people["mc"]
        mc.x, self.mc_actualx = self.width / 3, self.width / 3 + 20
        mc.y, self.mc_actualy = self.height / 2, self.height / 2 + 70           

        for person in town.people.values():
            moveSprite(person.sprite, person.x, person.y, True)
            moveSprite(person.speech, person.x+10, person.y-10, True)
            showSprite(person.sprite)
        
        text_box = makeSprite("graphics/text.png", 1)
        text = None
        name_label = None
        
        while self.loop:
            if clock() > self.next_frame:
                events = []
                for person in town.people.values():
                    person.frame = (person.frame + 1) % 6
                    moveSprite(person.sprite, person.x, person.y)
                    moveSprite(person.speech, person.x+10, person.y+10)
                    if person != mc:
                        person.update_pos(self.mask)
                    if person.talking:
                        showSprite(person.speech)
                    else:
                        hideSprite(person.speech)
                    
                self.next_frame += 40
                event = town.initiate_convo(clock(), self.messages)
                if event is not None:
                    events.append((event.timestamp, event.message, event.other_parent))
                
                if keyPressed("right"):
                    if self.mask.pix[self.mc_actualx + VELOCITY, self.mc_actualy] != (0, 0, 0, 255):                
                        mc.x += VELOCITY
                        self.mc_actualx += VELOCITY
                        if mc.x >= WIDTH / 2:
                            mc.x -= VELOCITY
                            scrollBackground(-SCROLL, 0)
                            for person in town.people.values():
                                if person != mc:                                    
                                    person.x -= VELOCITY 
                        changeSpriteImage(mc.sprite, 0*6 + mc.frame)
                        mc.last_position = 0
                elif keyPressed("up"):   
                    if self.mask.pix[self.mc_actualx, self.mc_actualy - VELOCITY] != (0, 0, 0, 255):
                        mc.y -= VELOCITY
                        self.mc_actualy -= VELOCITY
                        changeSpriteImage(mc.sprite, 1*6 + mc.frame)
                        mc.last_position = 1
                elif keyPressed("left"):
                    if self.mask.pix[self.mc_actualx - VELOCITY, self.mc_actualy] != (0, 0, 0, 255):                
                        mc.x -= VELOCITY
                        self.mc_actualx -= VELOCITY
                        if mc.x <= WIDTH / 2:
                            mc.x += VELOCITY
                            scrollBackground(SCROLL, 0)
                            for person in town.people.values():
                                if person != mc:
                                    person.x += VELOCITY 
                        changeSpriteImage(mc.sprite, 2*6 + mc.frame)
                        mc.last_position = 2
                elif keyPressed("down"):
                    if self.mask.pix[self.mc_actualx, self.mc_actualy + VELOCITY] != (0, 0, 0, 255):                
                        mc.y += VELOCITY
                        self.mc_actualy += VELOCITY
                    if mc.y >= HEIGHT / 2:
                        mc.y -= VELOCITY
                        scrollBackground(0, -SCROLL)
                        for person in town.people.values():
                            if person != mc:
                                person.y -= VELOCITY + SCROLL/2
                                moveSprite(person.sprite, person.x, person.y)
                        changeSpriteImage(mc.sprite, 3*6 + mc.frame)
                        mc.last_position = 3
            
            if events:
                events.sort(reverse=True)
                if text:
                    hideLabel(text)
                if name_label:
                    hideLabel(name_label)
                text = makeLabel(events[0][1], 24, WIDTH * 0.28, HEIGHT * 0.75, "black", "TTF/dogicapixel.ttf", "clear")
                name_label = makeLabel(events[0][2] + " said...", 24, WIDTH * 0.28, HEIGHT * 0.7, "black", "TTF/dogicapixel.ttf", "clear")
                transformSprite(text_box,0,0.3)
                moveSprite(text_box, WIDTH/2, HEIGHT * 0.8, True)
                showSprite(text_box) 
                showLabel(text)
                showLabel(name_label)
            tick(120)
        endWait()

if __name__ == '__main__':
    game = GameEngine("Acorn Hill", WIDTH, HEIGHT)
    game.run()