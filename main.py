import pygame
import colors
import cards
import ui

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

        self.redMana = 0
        self.blueMana = 0
        self.greenMana = 0

        self.cards = {
        'back': cards.Card(18, 270, pygame.image.load('assets/back.png')),
        'red': cards.Card(200, 100, pygame.image.load('assets/red_example.png'))
        }

        self.greenManaCounter = ui.ManaCounter(925, 530)
        self.redManaCounter = ui.ManaCounter(903, 628)
        self.blueManaCounter = ui.ManaCounter(948, 628)

        self.meditatioCounter = ui.MeditationCounter(923, 728)

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

        ui.drawBoard(self.screen)

        for card in self.cards:
            self.cards[card].draw(self.screen)

        self.greenManaCounter.draw(self.screen)
        self.redManaCounter.draw(self.screen)
        self.blueManaCounter.draw(self.screen)

        self.meditatioCounter.draw(self.screen)

    def update(self):
        for card in self.cards:
            self.cards[card].update()

        self.greenManaCounter.update(self.greenMana, 'green')
        self.redManaCounter.update(self.redMana, 'red')
        self.blueManaCounter.update(self.blueMana, 'blue')

        self.meditatioCounter.update()

        pygame.display.update()
        self.clock.tick(30)

game = Game(1000, 800, "Untitled Card Game")
game.start()

pygame.quit()
