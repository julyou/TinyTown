class Person:
    def __init__(self, image, game):
        self.image = image
        self.screen = game.screen

        self.x, self.y = 0.0, 0.0

    def blitme(self):
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y
        self.screen.blit(self.image, self.rect)