#Copyright (c) 2021 Kason Suchow

import pygame
import data

class Card:
    def __init__(self, x, y, face, color, name, description, attack, defense, cost, type):
        self.x = x
        self.y = y

        self.pos = (self.x, self.y)

        self.color = color

        self.name = name
        self.description = description

        self.attack = attack
        self.defense = defense
        self.cost = cost

        self.type = type

        self.remove = False

        self.hovered = False

        self.faceUp = False

        self.face = pygame.transform.scale(pygame.image.load(face), (80, 112))
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

        if self.type == 'mana':
            if self.faceUp:
                if self.hovered:
                    if pygame.mouse.get_pressed()[0]:
                        print('click!')
                        if data.playerOneMP >= self.cost:
                            data.playerOneMP -= self.cost

                            if self.color == 'red':
                                data.playerOneRedMana += 3
                            elif self.color == 'green':
                                data.playerOneGreenMana += 3
                            elif self.color == 'blue':
                                data.playerOneBlueMana += 3

                            self.remove = True

    def drawCard(self, player):
        pass

    def checkHover(self):
        pos = pygame.mouse.get_pos()

        if self.x <= pos[0] <= self.x + 80:
            if self.y <= pos[1] <= self.y + 112:
                self.hovered = True
            else:
                self.hovered = False
        else:
            self.hovered = False



library = {
'001': Card(-500, -500, 'assets/cards/green/mana.png', 'green', 'test', 'test', 0, 1, 1, 'mana'),
'002': Card(-500, -500, 'assets/cards/blue/mana.png', 'blue', 'test', 'test', 0, 1, 1, 'mana'),
'003': Card(-500, -500, 'assets/cards/red/mana.png', 'red', 'test', 'test', 0, 1, 1, 'mana'),
}
