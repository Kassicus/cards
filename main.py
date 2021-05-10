#Copyright (c) 2021 Kason Suchow

import pygame
import imageHandler
import data

pygame.init()

class Game:
    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.title = title

        self.screen = pygame.display.set_mode([self.width, self.height])
        pygame.display.set_caption(self.title)
        pygame.display.set_icon(imageHandler.iconImage)

        self.running = True
        self.clock = pygame.time.Clock()
        data.events = pygame.event.get()

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

    def update(self):

        pygame.display.update()
        self.clock.tick(30)

game = Game(1000, 800, "Untitled Card Game")
game.start()

pygame.quit()
