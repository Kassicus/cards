#Copyright (c) 2021 Kason Suchow

import ui

class PlayerOne():
    def __init__(self):
        self.redMana = 0
        self.blueMana = 0
        self.greenMana = 0

        self.redManaCounter = ui.ManaCounter(903, 508, 'red')
        self.blueManaCounter = ui.ManaCounter(948, 508, 'blue')
        self.greenManaCounter = ui.ManaCounter(925, 410, 'green')

    def draw(self, surface):
        self.drawManaCounters(surface)

    def update(self):
        self.updateManaCounters()

    def updateManaCounters(self):
        self.redManaCounter.update(self.redMana)
        self.blueManaCounter.update(self.blueMana)
        self.greenManaCounter.update(self.greenMana)

    def drawManaCounters(self, surface):
        self.redManaCounter.draw(surface)
        self.blueManaCounter.draw(surface)
        self.greenManaCounter.draw(surface)
