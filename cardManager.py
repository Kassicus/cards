#Copyright (c) 2021 Kason Suchow

import pygame
import random

def placeDeck(player):
    for x in range(len(player.deck)):
        card = player.deck[x]
        card.x = 18
        card.y = 670

def drawCard(player):
    if len(player.deck) > 0:
        player.hand.append(player.deck[0])
        player.deck.pop(0)

        reorderHand(player)

def reorderHand(player):
    for x in range(len(player.hand)):
        card = player.hand[x]
        card.x = int(120 + (x * 90))
        card.faceUp = True

def shuffleDeck(player):
    random.shuffle(player.deck)

def removeCardFromHand(index, player):
    player.graveyard.append(player.hand[index])
    player.hand.pop(index)

    reorderGraveyard(player)

    reorderHand(player)

def reorderGraveyard(player):
    for x in range(len(player.graveyard)):
        card = player.graveyard[x]
        card.x = 801
        card.y = 670

def moveCardToBoard(index, player):
    player.board.append(player.hand[index])
    player.hand.pop(index)

    reorderBoard(player)

    reorderHand(player)

def reorderBoard(player):
    for x in range(len(player.board)):
        card = player.board[x]
        card.x = int(18 + (x * 90))
        card.y = 535
