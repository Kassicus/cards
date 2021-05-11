#Copyright (c) 2021 Kason Suchow

import pygame
import ui
import data
import cards
import cardManager

class PlayerOne():
    def __init__(self):
        self.redMana = 0
        self.blueMana = 0
        self.greenMana = 0

        self.meditationPoints = 3

        self.redManaCounter = ui.ManaCounter(903, 508, 'red')
        self.blueManaCounter = ui.ManaCounter(948, 508, 'blue')
        self.greenManaCounter = ui.ManaCounter(925, 410, 'green')

        self.meditationCounter = ui.MeditationCounter(923, 608)

        self.deck = [
        cards.GreenMana(),
        cards.GreenMana(),
        cards.RedMana(),
        cards.Turtle(),
        cards.Turtle(),
        cards.Souls(),
        cards.Souls()
        ]

        self.hand = [

        ]

        self.defenders = [

        ]

        self.attackers = [

        ]

        self.graveyard = [

        ]

        cardManager.placeDeck(self)

    def draw(self, surface):
        self.drawCounters(surface)

        self.drawCards(surface)

    def update(self):
        self.updateCounters()

        self.updateCards()

        self.testDraw()

    def drawCounters(self, surface):
        self.redManaCounter.draw(surface)
        self.blueManaCounter.draw(surface)
        self.greenManaCounter.draw(surface)

        self.meditationCounter.draw(surface)

    def drawCards(self, surface):
        for x in range(len(self.deck)):
            card = self.deck[x]
            card.draw(surface)

        for x in range(len(self.hand)):
            card = self.hand[x]
            card.draw(surface)

        for x in range(len(self.defenders)):
            card = self.defenders[x]
            card.draw(surface)

        for x in range(len(self.attackers)):
            card = self.attackers[x]
            card.draw(surface)

        for x in range(len(self.graveyard)):
            card = self.graveyard[x]
            card.draw(surface)

    def updateCounters(self):
        self.redManaCounter.update(self.redMana)
        self.blueManaCounter.update(self.blueMana)
        self.greenManaCounter.update(self.greenMana)

        self.meditationCounter.update(self.meditationPoints)

    def updateCards(self):
        for x in range(len(self.deck)):
            try:
                card = self.deck[x]
                card.update()
            except:
                pass

        for x in range(len(self.hand)):
            try:
                card = self.hand[x]
                card.update()
                card.checkClicked(self)

                if card.move == 'graveyard':
                    cardManager.removeCardFromLibrary(self.hand, x, self)

                if card.move == 'defenders':
                    cardManager.moveCardToDefenders(x, self)

                if card.move == 'attackers':
                    cardManager.moveCardToAttackers(x, self)
            except:
                pass

        for x in range(len(self.defenders)):
            try:
                card = self.defenders[x]
                card.update()
                card.checkSelected()

                if card.move == 'graveyard':
                    cardManager.removeCardFromLibrary(self.defenders, x, self)
            except:
                pass

        for x in range(len(self.attackers)):
            try:
                card = self.attackers[x]
                card.update()
                card.checkSelected()

                if card.move == 'graveyard':
                    cardManager.removeCardFromLibrary(self.attackers, x, self)
            except:
                pass

        for x in range(len(self.graveyard)):
            try:
                card = self.graveyard[x]
                card.update()
            except:
                pass

    def testDraw(self):
        for event in data.events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    cardManager.drawCard(self)
