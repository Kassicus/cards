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

        self.meditationPoints = 1

        self.redManaCounter = ui.ManaCounter(903, 508, 'red')
        self.blueManaCounter = ui.ManaCounter(948, 508, 'blue')
        self.greenManaCounter = ui.ManaCounter(925, 410, 'green')

        self.meditationCounter = ui.MeditationCounter(923, 608)

        self.deck = [
        cards.GreenMana(),
        cards.GreenMana(),
        cards.Turtle()
        ]

        self.hand = [

        ]

        self.board = [

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

        for x in range(len(self.board)):
            card = self.board[x]
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
                    cardManager.removeCardFromHand(x, self)

                if card.move == 'board':
                    cardManager.moveCardToBoard(x, self)
            except:
                pass

        for x in range(len(self.board)):
            try:
                card = self.board[x]
                card.update()
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
