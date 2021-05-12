#Copyright (c) 2021 Kason Suchow

import pygame
import random

def placeDeck(player):
    for x in range(len(player.deck)):
        card = player.deck[x]
        card.x = player.deckpos[0]
        card.y = player.deckpos[1]

def drawCard(player):
    if len(player.deck) > 0:
        player.hand.append(player.deck[0])
        player.deck.pop(0)

        reorderHand(player)

def reorderHand(player):
    for x in range(len(player.hand)):
        card = player.hand[x]
        card.x = int(player.handpos[0] + (x * 90))
        card.y = player.handpos[1]
        card.faceUp = True

def shuffleDeck(player):
    random.shuffle(player.deck)

def removeCardFromLibrary(lib, index, player):
    player.graveyard.append(lib[index])
    lib.pop(index)

    reorderGraveyard(player)

    reorderHand(player)
    reorderAttackers(player)
    reorderDefenders(player)

def reorderGraveyard(player):
    for x in range(len(player.graveyard)):
        card = player.graveyard[x]
        card.tapped = False
        card.x = player.graveyardpos[0]
        card.y = player.graveyardpos[1]

def moveCardToAttackers(index, player):
    player.attackers.append(player.hand[index])
    player.hand.pop(index)

    reorderAttackers(player)

    reorderHand(player)

def reorderAttackers(player):
    for x in range(len(player.attackers)):
        card = player.attackers[x]
        card.x = int(player.attackerspos[0] + (x * 90))
        card.y = player.attackerspos[1]

def moveCardToDefenders(index, player):
    player.defenders.append(player.hand[index])
    player.hand.pop(index)

    reorderDefenders(player)

    reorderHand(player)

def reorderDefenders(player):
    for x in range(len(player.defenders)):
        card = player.defenders[x]
        card.x = int(player.defenderspos[0] + (x * 90))
        card.y = player.defenderspos[1]

def bounceCardToHand(lib, index, player):
    lib[index].selected = False
    lib[index].tapped = False
    player.hand.append(lib[index])
    lib.pop(index)

    reorderAttackers(player)
    reorderDefenders(player)
    reorderHand(player)
