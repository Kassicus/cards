#Copyright (c) 2021 Kason Suchow

import pygame
import imageManager
import data

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
        self.hovered = False
        self.clicked = True
        self.selected = False
        self.move = ''
        self.tapped = False

        self.image = self.back

    def draw(self, surface):
        if self.tapped:
            surface.blit(pygame.transform.rotate(self.image, 90), self.pos)
        else:
            surface.blit(self.image, self.pos)

        if self.selected:
            self.drawOutline(surface)

    def drawOutline(self, surface):
        if self.tapped:
            surface.blit(pygame.transform.rotate(imageManager.highlightCard, 90), (self.x - 2, self.y - 2))
        else:
            surface.blit(imageManager.highlightCard, (self.x - 2, self.y - 2))

    def update(self):
        self.pos = (self.x, self.y)

        if self.faceUp:
            self.image = self.face
        else:
            self.image = self.back

        self.checkHovered()

        if self.selected:
            self.checkInput()

    def checkHovered(self):
        mousePos = pygame.mouse.get_pos()

        if self.x <= mousePos[0] <= self.x + 80:
            if self.y <= mousePos[1] <= self.y + 112:
                self.hovered = True
            else:
                self.hovered = False
        else:
            self.hovered = False

    def checkClicked(self, player):
        for event in data.events:
            if self.hovered and event.type == pygame.MOUSEBUTTONDOWN:
                self.clicked = True
                self.doTask(player)
            else:
                self.clicked = False

    def checkSelected(self):
        for event in data.events:
            if self.hovered and event.type == pygame.MOUSEBUTTONDOWN:
                self.selected = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.selected = False

    def checkInput(self):
        for event in data.events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_k:
                    self.selected = False
                    self.move = 'graveyard'
                if event.key == pygame.K_t:
                    if self.tapped:
                        self.tapped = False
                    else:
                        self.tapped = True
                if event.key == pygame.K_b:
                    self.move = 'hand'

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

    def doTask(self, player):
        if player.meditationPoints >= self.cost:
            player.redMana += 3
            player.meditationPoints -= 1
            self.move = 'graveyard'

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

        self.face = imageManager.cardBlueMana

    def doTask(self, player):
        if player.meditationPoints >= self.cost:
            player.blueMana += 3
            player.meditationPoints -= 1
            self.move = 'graveyard'

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

        self.face = imageManager.cardGreenMana

    def doTask(self, player):
        if player.meditationPoints >= self.cost:
            player.greenMana += 3
            player.meditationPoints -= 1
            self.move = 'graveyard'

class Turtle(BaseCard):
    def __init__(self):
        super().__init__()

        self.color = 'green'

        self.name = 'Turtle'
        self.description = 'Beefy Turtle defender boi'

        self.attack = 1
        self.defense = 4
        self.cost = 2

        self.type = 'defender'

        self.face = imageManager.cardTurtle

    def doTask(self, player):
        if player.greenMana >= self.cost:
            player.greenMana -= self.cost
            self.move = 'defenders'

class SeaWall(BaseCard):
    def __init__(self):
        super().__init__()

        self.color = 'green'

        self.name = 'Sea Wall'
        self.description = 'An old stone wall on the shore'

        self.attack = 0
        self.defense = 3
        self.cost = 1

        self.type = 'defender'

        self.face = imageManager.cardSeaWall

    def doTask(self, player):
        if player.greenMana >= self.cost:
            player.greenMana -= self.cost
            self.move = 'defenders'

class Souls(BaseCard):
    def __init__(self):
        super().__init__()

        self.color = 'red'

        self.name = 'Souls'
        self.description = 'Soul Sand?'

        self.attack = 2
        self.defense = 1
        self.cost = 1

        self.type = 'attacker'

        self.face = imageManager.cardSouls

    def doTask(self, player):
        if player.redMana >= self.cost:
            player.redMana -= self.cost
            self.move = 'attackers'
