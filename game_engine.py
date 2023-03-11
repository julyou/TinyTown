import pygame
from people import People

class GameEngine:
    def __init__(self, name, size):
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()
        self.loop = True
        self.adam = People('sprites/Adam_16x16.png', self.screen)
        pygame.display.set_caption(name)

    def run(self):
        while self.loop:
            self.check_events()
            self.update_screen()
            # ------- Game logic --------

            # ------- Rendering --------
            self.clock.tick(60)
        pygame.quit()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.loop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.loop = False

    def update_screen(self):
        self.screen.fill((0, 0, 0))

        self.adam.people[0].blitme()
        pygame.display.flip()

if __name__ == '__main__':
    game = GameEngine("Acorn Hill", (700, 500))
    game.run()