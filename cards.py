#Copyright (c) 2021 Kason Suchow

import pygame
import data

class BaseCard(object):
    def __init__(self):
        self.x = -500
        self.y = -500

        self.pos = (self.x, self.y)

        self.color = None

        self.name = ''
        self.description = ''

        self.attack = 0
        self.defense = 0
        self.cost = 0

        self.type = ''

        self.remove = False
        self.hovered = False
        self.faceUp = False

        self.face = None
        self.back = pygame.transform.scale(pygame.image.load('assets/cards/back.png'), (80, 112))

        self.image = self.back

    def draw(self, surface):
        surface.blit(self.image, self.pos)

    def update(self):
        self.pos = (self.x, self.y)

        if self.faceUp:
            self.image = self.face
            self.checkHover()
        else:
            self.image = self.back

        self.checkClicked()

    def checkHover(self):
        pos = pygame.mouse.get_pos()

        if self.x <= pos[0] <= self.x + 80:
            if self.y <= pos[1] <= self.y + 112:
                self.hovered = True
            else:
                self.hovered = False
        else:
            self.hovered = False

    def checkClicked(self):
        for event in data.events:
            if self.type == 'mana' and self.faceUp and self.hovered and event.type == pygame.MOUSEBUTTONDOWN:
                if data.playerOneMP >= self.cost:
                    data.playerOneMP -= self.cost

                    if self.color == 'red':
                        data.playerOneRedMana += 3
                    elif self.color == 'green':
                        data.playerOneGreenMana += 3
                    elif self.color == 'blue':
                        data.playerOneBlueMana += 3

                    self.remove = True

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

        self.face = pygame.transform.scale(pygame.image.load('assets/cards/red/mana.png'), (80, 112))

class BlueMana(BaseCard):
    def __init__(self):
        super().__init__()

        self.color = 'blue'

        self.name = 'Blue Mana'
        self.description = 'Adds 3 Blue Mana'

        self.attack = 0
        self.defense = 0
        self.cost = 1

        self.type = 'mana'

        self.face = pygame.transform.scale(pygame.image.load('assets/cards/blue/mana.png'), (80, 112))

class GreenMana(BaseCard):
    def __init__(self):
        super().__init__()

        self.color = 'green'

        self.name = 'Green Mana'
        self.description = 'Adds 3 Green Mana'

        self.attack = 0
        self.defense = 0
        self.cost = 1

        self.type = 'mana'

        self.face = pygame.transform.scale(pygame.image.load('assets/cards/green/mana.png'), (80, 112))

library = {
'001': RedMana(),
'002': BlueMana(),
'003': GreenMana(),
'004': RedMana(),
}
