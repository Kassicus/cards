#Copyright (c) 2021 Kason Suchow

import pygame
import imageManager

class BaseCard(object):
    def __init__(self):
        self.x = -500
        self.y = -500

        self.pos = (self.x, self.y)

        self.color = ''

        self.name = ''
        self.description = ''

        self.attack = 0
        self.defense = 0
        self.cost = 0

        self.type = ''

        self.face = None
        self.back = imageManager.cardBack

        self.faceUp = False

        self.image = self.back

    def draw(self, surface):
        surface.blit(self.image, self.pos)

    def update(self):
        self.pos = (self.x, self.y)

        if self.faceUp:
            self.image = self.face
        else:
            self.image = self.back

class RedMana(BaseCard):
    def __init__(self):
        super().__init__()

        self.color = 'red'

        self.name = 'Red Mana'
        self.description = 'Adds 3 Red Mana'

        self.attack = 0
        self.defense = 0
        self.cost = 1

        self.type = 'mana'

        self.face = imageManager.cardRedMana
