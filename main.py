#Copyright (c) 2021 Kason Suchow

import pygame
import imageManager
import data
import playerManager
import ui

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

    def start(self):
        while self.running:
            data.events = pygame.event.get()

            for event in data.events:
                if event.type == pygame.QUIT:
                    self.running = False

            self.draw()

            self.update()

    def draw(self):
        self.screen.fill(data.color.BACKGROUND)

        ui.drawBoard(self.screen)

        self.playerOne.draw(self.screen)

    def update(self):
        self.playerOne.update()

        pygame.display.update()
        self.clock.tick(30)

game = Game(1000, 800, "Untitled Card Game")
game.start()

pygame.quit()
