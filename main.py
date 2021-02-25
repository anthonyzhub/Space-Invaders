#! /usr/bin/python3

import pygame

SCREEN_LENGTH = 840
SCREEN_HEIGHT = 720

if __name__ == "__main__":

    # Initialize pygame
    pygame.init()

    # Create a window
    screen = pygame.display.set_mode((SCREEN_LENGTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Space Invaders!")

    # Game's on/off status
    continueGame = True

    while continueGame:
        
        # Exit game
        for key in pygame.event.get():

            if key.type == pygame.QUIT:
                continueGame = False

    pygame.quit()