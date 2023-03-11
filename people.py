from sprite_loader import SpriteLoader
from person import Person

class People:
    def __init__(self):
        self.people = {}

    def add_person(self, name, path, num_div):
        """Creates person:
            - load sprite from sprite sheet
            - creates person object
        """
        person = Person(name, path, num_div)
        self.people[name] = person
    