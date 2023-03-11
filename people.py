from sprite_loader import SpriteLoader
from person import Person

class People:
    def __init__(self, path, screen):
        self.people = []
        self.screen = screen
        self.load_sprite(path)

    def load_sprite(self, path):
        """Creates person:
            - load sprite from sprite sheet
            - creates person object
        """
        adam = SpriteLoader(path)
    
        adam_rect = (10, 10, 10, 10)
        adam_image = adam.image_at(adam_rect)
        adam = Person(adam_image, self.screen)
        self.people.append(adam)
    