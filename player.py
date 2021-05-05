#Copyright (c) 2021 Kason Suchow

import ui
import cards
import data

class PlayerOne:
    def __init__(self):
        self.deck = [
        cards.library['001'],
        cards.library['002'],
        cards.library['003']
        ]

        self.hand = []
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

        for card in range(len(self.deck)):
            self.deck[card].x = 18
            self.deck[card].y = 670

    def draw(self, surface):
        self.greenManaCounter.draw(surface)
        self.redManaCounter.draw(surface)
        self.blueManaCounter.draw(surface)

        self.meditationCounter.draw(surface)

        for card in range(len(self.deck)):
            self.deck[card].draw(surface)

        for card in range(len(self.hand)):
            self.hand[card].draw(surface)

        for card in range(len(self.graveyard)):
            self.graveyard[card].draw(surface)

    def update(self):
        self.redMana = data.playerOneRedMana
        self.blueMana = data.playerOneBlueMana
        self.greenMana = data.playerOneGreenMana
        self.meditationPoints = data.playerOneMP

        self.greenManaCounter.update(self.greenMana, 'green')
        self.redManaCounter.update(self.redMana, 'red')
        self.blueManaCounter.update(self.blueMana, 'blue')

        self.meditationCounter.update(self.meditationPoints)

        for card in range(len(self.deck)):
            self.deck[card].update()

        for card in range(len(self.hand)):
            try:
                self.hand[card].update()

                if self.hand[card].remove:
                    self.graveyard.append(self.hand[card])
                    self.hand.pop(card)

                    for card in range(len(self.graveyard)):
                        self.graveyard[card].x = 801
            except:
                pass

        for card in range(len(self.graveyard)):
            self.graveyard[card].update()

    def drawCard(self):
        if len(self.deck) > 0:
            self.hand.append(self.deck[0])
            self.deck.pop(0)

        for card in range(len(self.hand)):
            self.hand[card].x = int(120 + (card * 90))
            self.hand[card].faceUp = True

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
