#Copyright (c) 2021 Kason Suchow

import pygame

boardImage = pygame.image.load('assets/ui/board2.png')

def drawBoard(surface):
    surface.blit(boardImage, (0, 0))

class ManaCounter:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.pos = (self.x, self.y)

        self.images = {
        'zero': pygame.transform.scale(pygame.image.load('assets/ui/mana_crystal.png'), (38, 106)),
        'red_1': pygame.transform.scale(pygame.image.load('assets/ui/red/red_mana_1.png'), (38, 106)),
        'red_2': pygame.transform.scale(pygame.image.load('assets/ui/red/red_mana_2.png'), (38, 106)),
        'red_3': pygame.transform.scale(pygame.image.load('assets/ui/red/red_mana_3.png'), (38, 106)),
        'red_4': pygame.transform.scale(pygame.image.load('assets/ui/red/red_mana_4.png'), (38, 106)),
        'red_5': pygame.transform.scale(pygame.image.load('assets/ui/red/red_mana_5.png'), (38, 106)),
        'red_6': pygame.transform.scale(pygame.image.load('assets/ui/red/red_mana_6.png'), (38, 106)),
        'red_7': pygame.transform.scale(pygame.image.load('assets/ui/red/red_mana_7.png'), (38, 106)),
        'red_8': pygame.transform.scale(pygame.image.load('assets/ui/red/red_mana_8.png'), (38, 106)),
        'red_9': pygame.transform.scale(pygame.image.load('assets/ui/red/red_mana_9.png'), (38, 106)),
        'red_10': pygame.transform.scale(pygame.image.load('assets/ui/red/red_mana_10.png'), (38, 106)),
        'blue_1': pygame.transform.scale(pygame.image.load('assets/ui/blue/blue_mana_1.png'), (38, 106)),
        'blue_2': pygame.transform.scale(pygame.image.load('assets/ui/blue/blue_mana_2.png'), (38, 106)),
        'blue_3': pygame.transform.scale(pygame.image.load('assets/ui/blue/blue_mana_3.png'), (38, 106)),
        'blue_4': pygame.transform.scale(pygame.image.load('assets/ui/blue/blue_mana_4.png'), (38, 106)),
        'blue_5': pygame.transform.scale(pygame.image.load('assets/ui/blue/blue_mana_5.png'), (38, 106)),
        'blue_6': pygame.transform.scale(pygame.image.load('assets/ui/blue/blue_mana_6.png'), (38, 106)),
        'blue_7': pygame.transform.scale(pygame.image.load('assets/ui/blue/blue_mana_7.png'), (38, 106)),
        'blue_8': pygame.transform.scale(pygame.image.load('assets/ui/blue/blue_mana_8.png'), (38, 106)),
        'blue_9': pygame.transform.scale(pygame.image.load('assets/ui/blue/blue_mana_9.png'), (38, 106)),
        'blue_10': pygame.transform.scale(pygame.image.load('assets/ui/blue/blue_mana_10.png'), (38, 106)),
        'green_1': pygame.transform.scale(pygame.image.load('assets/ui/green/green_mana_1.png'), (38, 106)),
        'green_2': pygame.transform.scale(pygame.image.load('assets/ui/green/green_mana_2.png'), (38, 106)),
        'green_3': pygame.transform.scale(pygame.image.load('assets/ui/green/green_mana_3.png'), (38, 106)),
        'green_4': pygame.transform.scale(pygame.image.load('assets/ui/green/green_mana_4.png'), (38, 106)),
        'green_5': pygame.transform.scale(pygame.image.load('assets/ui/green/green_mana_5.png'), (38, 106)),
        'green_6': pygame.transform.scale(pygame.image.load('assets/ui/green/green_mana_6.png'), (38, 106)),
        'green_7': pygame.transform.scale(pygame.image.load('assets/ui/green/green_mana_7.png'), (38, 106)),
        'green_8': pygame.transform.scale(pygame.image.load('assets/ui/green/green_mana_8.png'), (38, 106)),
        'green_9': pygame.transform.scale(pygame.image.load('assets/ui/green/green_mana_9.png'), (38, 106)),
        'green_10': pygame.transform.scale(pygame.image.load('assets/ui/green/green_mana_10.png'), (38, 106)),
        }

        self.image = self.images['zero']

    def draw(self, surface):
        surface.blit(self.image, self.pos)

    def update(self, mana, key):
        if key == 'red':
            if mana == 1:
                self.image = self.images['red_1']
            if mana == 2:
                self.image = self.images['red_2']
            if mana == 3:
                self.image = self.images['red_3']
            if mana == 4:
                self.image = self.images['red_4']
            if mana == 5:
                self.image = self.images['red_5']
            if mana == 6:
                self.image = self.images['red_6']
            if mana == 7:
                self.image = self.images['red_7']
            if mana == 8:
                self.image = self.images['red_8']
            if mana == 9:
                self.image = self.images['red_9']
            if mana == 10:
                self.image = self.images['red_10']
        if key == 'blue':
            if mana == 1:
                self.image = self.images['blue_1']
            if mana == 2:
                self.image = self.images['blue_2']
            if mana == 3:
                self.image = self.images['blue_3']
            if mana == 4:
                self.image = self.images['blue_4']
            if mana == 5:
                self.image = self.images['blue_5']
            if mana == 6:
                self.image = self.images['blue_6']
            if mana == 7:
                self.image = self.images['blue_7']
            if mana == 8:
                self.image = self.images['blue_8']
            if mana == 9:
                self.image = self.images['blue_9']
            if mana == 10:
                self.image = self.images['blue_10']
        if key == 'green':
            if mana == 1:
                self.image = self.images['green_1']
            if mana == 2:
                self.image = self.images['green_2']
            if mana == 3:
                self.image = self.images['green_3']
            if mana == 4:
                self.image = self.images['green_4']
            if mana == 5:
                self.image = self.images['green_5']
            if mana == 6:
                self.image = self.images['green_6']
            if mana == 7:
                self.image = self.images['green_7']
            if mana == 8:
                self.image = self.images['green_8']
            if mana == 9:
                self.image = self.images['green_9']
            if mana == 10:
                self.image = self.images['green_10']

class MeditationCounter:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.pos = (self.x, self.y)

        self.images = {
        'zero': pygame.transform.scale(pygame.image.load('assets/ui/mc/mc_zero.png'), (42, 42)),
        'one': pygame.transform.scale(pygame.image.load('assets/ui/mc/mc_one.png'), (42, 42)),
        'two': pygame.transform.scale(pygame.image.load('assets/ui/mc/mc_two.png'), (42, 42)),
        'three': pygame.transform.scale(pygame.image.load('assets/ui/mc/mc_three.png'), (42, 42)),
        'four': pygame.transform.scale(pygame.image.load('assets/ui/mc/mc_four.png'), (42, 42)),
        'five': pygame.transform.scale(pygame.image.load('assets/ui/mc/mc_five.png'), (42, 42)),
        'six': pygame.transform.scale(pygame.image.load('assets/ui/mc/mc_six.png'), (42, 42)),
        'seven': pygame.transform.scale(pygame.image.load('assets/ui/mc/mc_seven.png'), (42, 42)),
        'eight': pygame.transform.scale(pygame.image.load('assets/ui/mc/mc_eight.png'), (42, 42)),
        'nine': pygame.transform.scale(pygame.image.load('assets/ui/mc/mc_nine.png'), (42, 42)),
        'ten': pygame.transform.scale(pygame.image.load('assets/ui/mc/mc_ten.png'), (42, 42)),
        }

        self.image = self.images['zero']

    def draw(self, surface):
        surface.blit(self.image, self.pos)

    def update(self, mps):
        if mps == 0:
            self.image = self.images['zero']
        if mps == 1:
            self.image = self.images['one']
        if mps == 2:
            self.image = self.images['two']
        if mps == 3:
            self.image = self.images['three']
        if mps == 4:
            self.image = self.images['four']
        if mps == 5:
            self.image = self.images['five']
        if mps == 6:
            self.image = self.images['six']
        if mps == 7:
            self.image = self.images['seven']
        if mps == 8:
            self.image = self.images['eight']
        if mps == 9:
            self.image = self.images['nine']
        if mps == 10:
            self.image = self.images['ten']
