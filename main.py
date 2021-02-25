#! /usr/bin/python3

import pygame
from player import Player

SCREEN_LENGTH = 840
SCREEN_HEIGHT = 720

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def updateScreen(screen, clock, allSpritesList):

    # OBJECTIVE: Update all changes on the screen

    # Make screen's background to black
    screen.fill(BLACK)

    # Draw all sprites on the window
    allSpritesList.draw(screen)

    # Update screen
    pygame.display.flip()

    # Update clock
    clock.tick(60)

def playerMovements(keysPressed, player):

    # OBJECTIVE: Respond to keys pressed

    if keysPressed[pygame.K_LEFT]:
        player.moveLeft(5)

    if keysPressed[pygame.K_RIGHT]:
        player.moveRight(5)

if __name__ == "__main__":

    # Initialize pygame
    pygame.init()

    # Create a window
    screen = pygame.display.set_mode((SCREEN_LENGTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Space Invaders!")

    # Draw sprites
    player = Player(WHITE, 25, 15)
    player.rect.x = SCREEN_LENGTH // 2
    player.rect.y = SCREEN_HEIGHT - 20

    # Add all sprites to list
    allSpritesList = pygame.sprite.Group()
    allSpritesList.add(player)

    # Game's on/off status
    continueGame = True

    # Initialize clock for FPS
    clock = pygame.time.Clock()

    while continueGame:
        
        # Exit game
        for key in pygame.event.get():

            if key.type == pygame.QUIT:
                continueGame = False

        # Get keyboard input
        keysPressed = pygame.key.get_pressed()
        playerMovements(keysPressed, player)

        # Update sprite's positions
        allSpritesList.update()

        # Update screen
        updateScreen(screen, clock, allSpritesList)

    pygame.quit()