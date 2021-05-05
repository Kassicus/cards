#Copyright (c) 2021 Kason Suchow

import pygame

class Card:
    def __init__(self, image, color, name, description, attack, defense, cost):
        self.x = -500
        self.y = -500

        self.pos = (self.x, self.y)

        self.name = name
        self.description = description

        self.attack = attack
        self.defense = defense
        self.cost = cost

        self.image = pygame.transform.scale(image, (80, 112))

    def draw(self, surface):
        surface.blit(self.image, self.pos)

    def update(self):
        pass

library = {
'001': Card(pygame.image.load('assets/back.png'), 'red', "Test Card", "This is a card for table testing", 2, 1, 3)
}
