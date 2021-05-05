import pygame

class Card:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y

        self.pos = (self.x, self.y)

        self.image = pygame.transform.scale(image, (80, 112))

    def draw(self, surface):
        surface.blit(self.image, self.pos)

    def update(self):
        pass
