#Copyright (c) 2021 Kason Suchow

import ui
import cards

class PlayerOne:
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

        self.greenManaCounter = ui.ManaCounter(925, 410)
        self.redManaCounter = ui.ManaCounter(903, 508)
        self.blueManaCounter = ui.ManaCounter(948, 508)

        self.meditationCounter = ui.MeditationCounter(923, 608)

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
