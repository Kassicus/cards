#Copyright (c) 2021 Kason Suchow

import pygame
import imageManager
import data
import playerManager
import ui
import cardManager

pygame.init()

class Game:
    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.title = title

        self.screen = pygame.display.set_mode([self.width, self.height])
        pygame.display.set_caption(self.title)
        pygame.display.set_icon(imageManager.icon)

        self.running = True
        self.clock = pygame.time.Clock()
        data.events = pygame.event.get()

        self.playerOne = playerManager.PlayerOne()
        self.playerTwo = playerManager.PlayerTwo()

    def start(self):
        for x in range(5):
            cardManager.drawCard(self.playerOne)
            cardManager.drawCard(self.playerTwo)

        while self.running:
            data.events = pygame.event.get()

            for event in data.events:
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.playerOne.meditationPoints += 1

                    if event.key == pygame.K_RETURN:
                        cardManager.drawCard(self.playerTwo)

            self.draw()

            self.update()

    def draw(self):
        self.screen.fill(data.color.BACKGROUND)

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
