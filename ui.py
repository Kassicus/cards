import pygame

class ManaCounter:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.pos = (self.x, self.y)

        self.images = {
        'base': pygame.image.load('assets/ui/mana_crystal.png')
        }

        self.image = pygame.transform.scale(self.images['base'], (38, 106))

    def draw(self, surface):
        surface.blit(self.image, self.pos)

    def update(self):
        pass

class MeditationCounter:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.pos = (self.x, self.y)

        self.images = {
        'zero': pygame.image.load('assets/ui/mc_zero.png')
        }

        self.image = pygame.transform.scale(self.images['zero'], (42, 42))

    def draw(self, surface):
        surface.blit(self.image, self.pos)

    def update(self):
        pass
