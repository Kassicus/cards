#Copyright (c) 2021 Kason Suchow

import random
import ui
import cards
import data

class PlayerOne:
    def __init__(self):
        self.deck = [
        cards.library['001'],
        cards.library['002'],
        cards.library['003'],
        cards.library['004']
        ]

        self.hand = []
        self.attackers = []
        self.defenders = []
        self.graveyard = []
        self.discard = []

        self.redMana = data.playerOneRedMana
        self.blueMana = data.playerOneBlueMana
        self.greenMana = data.playerOneGreenMana
        self.meditationPoints = data.playerOneMP

        self.greenManaCounter = ui.ManaCounter(925, 410)
        self.redManaCounter = ui.ManaCounter(903, 508)
        self.blueManaCounter = ui.ManaCounter(948, 508)

        self.meditationCounter = ui.MeditationCounter(923, 608)

        for c in range(len(self.deck)):
            card = self.deck[c]
            card.x = 18
            card.y = 670

        self.shuffleDeck()

    def draw(self, surface):
        self.greenManaCounter.draw(surface)
        self.redManaCounter.draw(surface)
        self.blueManaCounter.draw(surface)

        self.meditationCounter.draw(surface)

        for c in range(len(self.deck)):
            card = self.deck[c]
            card.draw(surface)

        for c in range(len(self.hand)):
            card = self.hand[c]
            card.draw(surface)

        for c in range(len(self.graveyard)):
            card = self.graveyard[c]
            card.draw(surface)

        for c in range(len(self.defenders)):
            card = self.defenders[c]
            card.draw(surface)

    def update(self):
        self.redMana = data.playerOneRedMana
        self.blueMana = data.playerOneBlueMana
        self.greenMana = data.playerOneGreenMana
        self.meditationPoints = data.playerOneMP

        self.greenManaCounter.update(self.greenMana, 'green')
        self.redManaCounter.update(self.redMana, 'red')
        self.blueManaCounter.update(self.blueMana, 'blue')

        self.meditationCounter.update(self.meditationPoints)

        for c in range(len(self.deck)):
            card = self.deck[c]
            card.update()

        for c in range(len(self.hand)):
            try:
                card = self.hand[c]
                card.update()
                card.checkPlayed()

                if card.played:
                    if card.type == 'defender':
                        self.defenders.append(card)
                        self.hand.pop(c)

                        self.reorderHand()
                        self.reorderDefenders()

                if card.remove:
                    self.graveyard.append(card)
                    self.hand.pop(c)

                    for c in range(len(self.graveyard)):
                        card = self.graveyard[c]
                        card.x = 801

                    self.reorderHand()
            except:
                pass

        for c in range(len(self.graveyard)):
            card = self.graveyard[c]
            card.update()

    def drawCard(self):
        if len(self.deck) > 0:
            self.hand.append(self.deck[0])
            self.deck.pop(0)

            self.reorderHand()

    def reorderDefenders(self):
        for c in range(len(self.defenders)):
            card = self.defenders[c]
            card.x = int(17 + (c * 90))
            card.y = 550
            card.faceUp = True

    def reorderHand(self):
        for c in range(len(self.hand)):
            card = self.hand[c]
            card.x = int(120 + (c * 90))
            card.faceUp = True

    def shuffleDeck(self):
        random.shuffle(self.deck)

class PlayerTwo:
    def __init__(self):
        self.deck = {

        }

        self.hand = {

        }

        self.discard = {

        }

        self.redMana = 0
        self.blueMana = 0
        self.greenMana = 0

        self.meditationPoints = 0

        self.greenManaCounter = ui.ManaCounter(35, 150)
        self.redManaCounter = ui.ManaCounter(13, 248)
        self.blueManaCounter = ui.ManaCounter(58, 248)

        self.meditationCounter = ui.MeditationCounter(33, 348)

    def draw(self, surface):
        self.greenManaCounter.draw(surface)
        self.redManaCounter.draw(surface)
        self.blueManaCounter.draw(surface)

        self.meditationCounter.draw(surface)

    def update(self):
        self.greenManaCounter.update(self.greenMana, 'green')
        self.redManaCounter.update(self.redMana, 'red')
        self.blueManaCounter.update(self.blueMana, 'blue')

        self.meditationCounter.update(self.meditationPoints)
