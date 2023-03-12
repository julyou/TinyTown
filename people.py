from person import Person
from utils import Cache
import random

class People:
    def __init__(self):
        self.people = {}
        self.num_talking = 0
        self.available_to_talk = []
        self.counter = 0

        self.memory = []

    def add_person(self, name, path, num_div, width, height):
        """Creates person:
            - load sprite from sprite sheet
            - creates person object
        """
        person = Person(name, path, num_div, width, height)
        self.people[name] = person
        self.available_to_talk.append(person)
    
    def initiate_convo(self, curr_time, messages):
        if self.counter <= 0:
            if len(self.available_to_talk) >= 2:
                num_talking = random.randint(0, int(len(self.available_to_talk) / 2))
                for _ in range(num_talking):
                    p1 = self.available_to_talk[random.randint(0, len(self.available_to_talk)-1)]
                    self.available_to_talk.remove(p1)
                    p2 = self.available_to_talk[random.randint(0, len(self.available_to_talk)-1)]
                    while p2 == p1.prev_talked_to:
                        p2 = self.available_to_talk[random.randint(0, len(self.available_to_talk)-1)]
                    self.available_to_talk.remove(p2)
                    p1.prev_talked_to = p2
                    p2.prev_talked_to = p1
                    p1.talk_to_target(p2, curr_time, messages)
                    print(p1.name)
                    print(p2.name)
            self.counter = 1000
        self.counter -= 10
