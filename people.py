from person import Person
import random

class People:
    def __init__(self):
        self.people = {}
        self.num_talking = 0
        self.available_to_talk = []
        self.counter = 0

    def add_person(self, name, path, num_div, width, height):
        """Creates person:
            - load sprite from sprite sheet
            - creates person object
        """
        person = Person(name, path, num_div, width, height)
        self.people[name] = person
        if person.name != "mc":
            self.available_to_talk.append(person)
    
    def initiate_convo(self, curr_time, messages):
        event = None
        if self.counter <= 0:
            if len(self.available_to_talk) >= 2:
                num_talking = random.randint(0, int(len(self.available_to_talk) / 2))
                print(num_talking)
                for _ in range(num_talking):
                    p1 = self.available_to_talk[random.randint(0, len(self.available_to_talk)-1)]
                    self.available_to_talk.remove(p1)
                    p1.walking = True
                    p2 = self.available_to_talk[random.randint(0, len(self.available_to_talk)-1)]
                    while p2 == p1.prev_talked_to:
                        p2 = self.available_to_talk[random.randint(0, len(self.available_to_talk)-1)]
                    self.available_to_talk.remove(p2)
                    p1.target = p2
                    p1.prev_talked_to = p2
                    p2.prev_talked_to = p1
                    event = p1.talk_to_target(p2, curr_time, messages)
                    print(p1.name)
                    print(p2.name)
            self.counter = 500
            for person in self.people.values():
                if not person.talking and person not in self.available_to_talk:
                    self.available_to_talk.append(person)
                if person.talking:
                    if person.ttl > 0:
                        person.ttl -= 100
                    else:
                        print(person.target)
                        person.talking = False
                        person.walking = False
                        person.target = None
        self.counter -= 10
        return event
