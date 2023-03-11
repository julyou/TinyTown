import pygame

class SpriteLoader:
    def __init__(self, path):
        try:
            self.sheet = pygame.image.load(path).convert()
        except pygame.error as e:
            print("Unable to load spritesheet: " + path)
            raise SystemExit(e)
    
    def image_at(self, rectangle, colorkey = None):
        """Load image rectangle"""
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image

    def images_at(self, rects, colorkey=None):
        """Load a bunch of images and return as list"""
        return [self.image_at(rect, colorkey) for rect in rects]

    def load_strip(self, rect, image_count, colorkey=None):
        """Load a whole strip of images and return as a list"""
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3]) for x in range(image_count)]
        return self.images_at(tups, colorkey)