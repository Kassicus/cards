#Copyright (c) 2021 Kason Suchow

import pygame

icon = pygame.image.load('assets/window/icon.png')
board = pygame.image.load('assets/ui/board2.png')

manaCrystal = pygame.transform.scale(pygame.image.load('assets/ui/mana_crystal.png'), (38, 106))

redManaCrystalOne = pygame.transform.scale(pygame.image.load('assets/ui/red/red_mana_1.png'), (38, 106))
redManaCrystalTwo = pygame.transform.scale(pygame.image.load('assets/ui/red/red_mana_2.png'), (38, 106))
redManaCrystalThree = pygame.transform.scale(pygame.image.load('assets/ui/red/red_mana_3.png'), (38, 106))
redManaCrystalFour = pygame.transform.scale(pygame.image.load('assets/ui/red/red_mana_4.png'), (38, 106))
redManaCrystalFive = pygame.transform.scale(pygame.image.load('assets/ui/red/red_mana_5.png'), (38, 106))
redManaCrystalSix = pygame.transform.scale(pygame.image.load('assets/ui/red/red_mana_6.png'), (38, 106))
redManaCrystalSeven = pygame.transform.scale(pygame.image.load('assets/ui/red/red_mana_7.png'), (38, 106))
redManaCrystalEight = pygame.transform.scale(pygame.image.load('assets/ui/red/red_mana_8.png'), (38, 106))
redManaCrystalNine = pygame.transform.scale(pygame.image.load('assets/ui/red/red_mana_9.png'), (38, 106))
redManaCrystalTen = pygame.transform.scale(pygame.image.load('assets/ui/red/red_mana_10.png'), (38, 106))

blueManaCrystalOne = pygame.transform.scale(pygame.image.load('assets/ui/blue/blue_mana_1.png'), (38, 106))
blueManaCrystalTwo = pygame.transform.scale(pygame.image.load('assets/ui/blue/blue_mana_2.png'), (38, 106))
blueManaCrystalThree = pygame.transform.scale(pygame.image.load('assets/ui/blue/blue_mana_3.png'), (38, 106))
blueManaCrystalFour = pygame.transform.scale(pygame.image.load('assets/ui/blue/blue_mana_4.png'), (38, 106))
blueManaCrystalFive = pygame.transform.scale(pygame.image.load('assets/ui/blue/blue_mana_5.png'), (38, 106))
blueManaCrystalSix = pygame.transform.scale(pygame.image.load('assets/ui/blue/blue_mana_6.png'), (38, 106))
blueManaCrystalSeven = pygame.transform.scale(pygame.image.load('assets/ui/blue/blue_mana_7.png'), (38, 106))
blueManaCrystalEight = pygame.transform.scale(pygame.image.load('assets/ui/blue/blue_mana_8.png'), (38, 106))
blueManaCrystalNine = pygame.transform.scale(pygame.image.load('assets/ui/blue/blue_mana_9.png'), (38, 106))
blueManaCrystalTen = pygame.transform.scale(pygame.image.load('assets/ui/blue/blue_mana_10.png'), (38, 106))

greenManaCrystalOne = pygame.transform.scale(pygame.image.load('assets/ui/green/green_mana_1.png'), (38, 106))
greenManaCrystalTwo = pygame.transform.scale(pygame.image.load('assets/ui/green/green_mana_2.png'), (38, 106))
greenManaCrystalThree = pygame.transform.scale(pygame.image.load('assets/ui/green/green_mana_3.png'), (38, 106))
greenManaCrystalFour = pygame.transform.scale(pygame.image.load('assets/ui/green/green_mana_4.png'), (38, 106))
greenManaCrystalFive = pygame.transform.scale(pygame.image.load('assets/ui/green/green_mana_5.png'), (38, 106))
greenManaCrystalSix = pygame.transform.scale(pygame.image.load('assets/ui/green/green_mana_6.png'), (38, 106))
greenManaCrystalSeven = pygame.transform.scale(pygame.image.load('assets/ui/green/green_mana_7.png'), (38, 106))
greenManaCrystalEight = pygame.transform.scale(pygame.image.load('assets/ui/green/green_mana_8.png'), (38, 106))
greenManaCrystalNine = pygame.transform.scale(pygame.image.load('assets/ui/green/green_mana_9.png'), (38, 106))
greenManaCrystalTen = pygame.transform.scale(pygame.image.load('assets/ui/green/green_mana_10.png'), (38, 106))

meditationCounterZero = pygame.transform.scale(pygame.image.load('assets/ui/mc/mc_zero.png'), (42, 42))
meditationCounterOne = pygame.transform.scale(pygame.image.load('assets/ui/mc/mc_one.png'), (42, 42))
meditationCounterTwo = pygame.transform.scale(pygame.image.load('assets/ui/mc/mc_two.png'), (42, 42))
meditationCounterThree = pygame.transform.scale(pygame.image.load('assets/ui/mc/mc_three.png'), (42, 42))
meditationCounterFour = pygame.transform.scale(pygame.image.load('assets/ui/mc/mc_four.png'), (42, 42))
meditationCounterFive = pygame.transform.scale(pygame.image.load('assets/ui/mc/mc_five.png'), (42, 42))
meditationCounterSix = pygame.transform.scale(pygame.image.load('assets/ui/mc/mc_six.png'), (42, 42))
meditationCounterSeven = pygame.transform.scale(pygame.image.load('assets/ui/mc/mc_seven.png'), (42, 42))
meditationCounterEight = pygame.transform.scale(pygame.image.load('assets/ui/mc/mc_eight.png'), (42, 42))
meditationCounterNine = pygame.transform.scale(pygame.image.load('assets/ui/mc/mc_nine.png'), (42, 42))
meditationCounterTen = pygame.transform.scale(pygame.image.load('assets/ui/mc/mc_ten.png'), (42, 42))

highlightCard = pygame.transform.scale(pygame.image.load('assets/cards/highlight.png'), (84, 116))

cardBack = pygame.transform.scale(pygame.image.load('assets/cards/back.png'), (80, 112))
cardRedMana = pygame.transform.scale(pygame.image.load('assets/cards/red/mana.png'), (80, 112))
cardBlueMana = pygame.transform.scale(pygame.image.load('assets/cards/blue/mana.png'), (80, 112))
cardGreenMana = pygame.transform.scale(pygame.image.load('assets/cards/green/mana.png'), (80, 112))

cardTurtle = pygame.transform.scale(pygame.image.load('assets/cards/green/turtle.png'), (80, 112))
cardSeaWall = pygame.transform.scale(pygame.image.load('assets/cards/green/seawall.png'), (80, 112))

cardSouls = pygame.transform.scale(pygame.image.load('assets/cards/red/souls.png'), (80, 112))
