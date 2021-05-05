import pygame
import colors
import cards
import ui

pygame.init()

class Game:
    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.title = title

        self.screen = pygame.display.set_mode([self.width, self.height])
        pygame.display.set_caption(self.title)

        self.running = True
        self.clock = pygame.time.Clock()
        self.events = pygame.event.get()

        self.cards = {
        'back': cards.Card(100, 100, pygame.image.load('assets/back.png')),
        'red': cards.Card(200, 100, pygame.image.load('assets/red_example.png'))
        }

        self.greenManaCounter = ui.ManaCounter(910, 530)
        self.redManaCounter = ui.ManaCounter(887, 628)
        self.blueManaCounter = ui.ManaCounter(933, 628)

        self.meditatioCounter = ui.MeditationCounter(908, 728)

    def start(self):
        while self.running:
            self.events = pygame.event.get()

            for event in self.events:
                if event.type == pygame.QUIT:
                    self.running = False

            self.draw()

            self.update()

    def draw(self):
        self.screen.fill(colors.BACKGROUND)

        for card in self.cards:
            self.cards[card].draw(self.screen)

        self.greenManaCounter.draw(self.screen)
        self.redManaCounter.draw(self.screen)
        self.blueManaCounter.draw(self.screen)

        self.meditatioCounter.draw(self.screen)

    def update(self):
        for card in self.cards:
            self.cards[card].update()

        self.greenManaCounter.update()
        self.redManaCounter.update()
        self.blueManaCounter.update()

        self.meditatioCounter.update()

        pygame.display.update()
        self.clock.tick(30)

game = Game(1000, 800, "Untitled Card Game")
game.start()

pygame.quit()
