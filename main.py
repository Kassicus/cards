#Copyright (c) 2021 Kason Suchow

import pygame
import colors
import cards
import ui
import player

pygame.init()

iconImage = pygame.image.load('assets/window/icon.png')

class Game:
    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.title = title

        self.screen = pygame.display.set_mode([self.width, self.height])
        pygame.display.set_caption(self.title)
        pygame.display.set_icon(iconImage)

        self.running = True
        self.clock = pygame.time.Clock()
        self.events = pygame.event.get()

        self.playerOne = player.PlayerOne()
        self.playerTwo = player.PlayerTwo()

    def start(self):
        while self.running:
            self.events = pygame.event.get()

            for event in self.events:
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    self.playerOne.drawCard()

            self.draw()

            self.update()

    def draw(self):
        self.screen.fill(colors.BACKGROUND)

        ui.drawBoard(self.screen)

        self.playerOne.draw(self.screen)
        self.playerTwo.draw(self.screen)

    def update(self):
        self.playerOne.update()
        self.playerTwo.update()

        pygame.display.update()
        self.clock.tick(30)

game = Game(1000, 800, "Untitled Card Game")
game.start()

pygame.quit()
