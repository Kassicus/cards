#Copyright (c) 2021 Kason Suchow

import pygame
import imageHandler

def drawBoard(surface):
    surface.blit(imageHandler.board, (0, 0))

class ManaCounter():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y

        self.pos = (self.x, self.y)

        self.color = color

        self.redImages = [
        imageHandler.manaCrystal,
        imageHandler.redManaCrystalOne,
        imageHandler.redManaCrystalTwo,
        imageHandler.redManaCrystalThree,
        imageHandler.redManaCrystalFour,
        imageHandler.redManaCrystalFive,
        imageHandler.redManaCrystalSix,
        imageHandler.redManaCrystalSeven,
        imageHandler.redManaCrystalEight,
        imageHandler.redManaCrystalNine,
        imageHandler.redManaCrystalTen
        ]

        self.blueImages = [
        imageHandler.manaCrystal,
        imageHandler.blueManaCrystalOne,
        imageHandler.blueManaCrystalTwo,
        imageHandler.blueManaCrystalThree,
        imageHandler.blueManaCrystalFour,
        imageHandler.blueManaCrystalFive,
        imageHandler.blueManaCrystalSix,
        imageHandler.blueManaCrystalSeven,
        imageHandler.blueManaCrystalEight,
        imageHandler.blueManaCrystalNine,
        imageHandler.blueManaCrystalTen
        ]

        self.greenImages = [
        imageHandler.manaCrystal,
        imageHandler.greenManaCrystalOne,
        imageHandler.greenManaCrystalTwo,
        imageHandler.greenManaCrystalThree,
        imageHandler.greenManaCrystalFour,
        imageHandler.greenManaCrystalFive,
        imageHandler.greenManaCrystalSix,
        imageHandler.greenManaCrystalSeven,
        imageHandler.greenManaCrystalEight,
        imageHandler.greenManaCrystalNine,
        imageHandler.greenManaCrystalTen
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
