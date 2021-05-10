#Copyright (c) 2021 Kason Suchow

import pygame
import imageManager

def drawBoard(surface):
    surface.blit(imageManager.board, (0, 0))

class ManaCounter():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y

        self.pos = (self.x, self.y)

        self.color = color

        self.redImages = [
        imageManager.manaCrystal,
        imageManager.redManaCrystalOne,
        imageManager.redManaCrystalTwo,
        imageManager.redManaCrystalThree,
        imageManager.redManaCrystalFour,
        imageManager.redManaCrystalFive,
        imageManager.redManaCrystalSix,
        imageManager.redManaCrystalSeven,
        imageManager.redManaCrystalEight,
        imageManager.redManaCrystalNine,
        imageManager.redManaCrystalTen
        ]

        self.blueImages = [
        imageManager.manaCrystal,
        imageManager.blueManaCrystalOne,
        imageManager.blueManaCrystalTwo,
        imageManager.blueManaCrystalThree,
        imageManager.blueManaCrystalFour,
        imageManager.blueManaCrystalFive,
        imageManager.blueManaCrystalSix,
        imageManager.blueManaCrystalSeven,
        imageManager.blueManaCrystalEight,
        imageManager.blueManaCrystalNine,
        imageManager.blueManaCrystalTen
        ]

        self.greenImages = [
        imageManager.manaCrystal,
        imageManager.greenManaCrystalOne,
        imageManager.greenManaCrystalTwo,
        imageManager.greenManaCrystalThree,
        imageManager.greenManaCrystalFour,
        imageManager.greenManaCrystalFive,
        imageManager.greenManaCrystalSix,
        imageManager.greenManaCrystalSeven,
        imageManager.greenManaCrystalEight,
        imageManager.greenManaCrystalNine,
        imageManager.greenManaCrystalTen
        ]

        self.image = self.redImages[0]

    def draw(self, surface):
        surface.blit(self.image, self.pos)

    def update(self, mana):
        if self.color == 'red':
            self.image = self.redImages[mana]
        elif self.color == 'blue':
            self.image = self.blueImages[mana]
        elif self.color == 'green':
            self.image = self.greenImages[mana]

class MeditationCounter():
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.pos = (self.x, self.y)

        self.images = [
        imageManager.meditationCounterZero,
        imageManager.meditationCounterOne,
        imageManager.meditationCounterTwo,
        imageManager.meditationCounterThree,
        imageManager.meditationCounterFour,
        imageManager.meditationCounterFive,
        imageManager.meditationCounterSix,
        imageManager.meditationCounterSeven,
        imageManager.meditationCounterEight,
        imageManager.meditationCounterNine,
        imageManager.meditationCounterTen,
        ]

        self.image = self.images[0]

    def draw(self, surface):
        surface.blit(self.image, self.pos)

    def update(self, meditationPoints):
        self.image = self.images[meditationPoints]
