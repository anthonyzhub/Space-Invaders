#! /usr/bin/python3

# Reference: https://itnext.io/creating-space-invaders-clone-in-pygame-ea0f5336c677
# Reference: https://github.com/janjilecek/pygame-invaders/blob/master/main.py

import pygame
from player import Player
from alien import Alien
from alien import Generator

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

class Game:

    screen = None
    aliensList = list()

    def __init__(self, width, height):

        # Initialize pygame
        pygame.init()

        # Get screen dimensions
        self.width = width
        self.height = height

        # Create a window
        self.screen = pygame.display.set_mode((self.width, self.height))

        # Initialize pygame's clock for FPS
        self.clock = pygame.time.Clock()

        # Boolean variable to start/stop game
        self.continueGame = True

    def updateScreen(self, player):

        # OBJECTIVE: Update all changes made on screen

        # Color screen's background
        self.screen.fill(BLACK)

        # Draw all sprites
        player.draw()
        for alien in self.aliensList:
            alien.draw()

        # Update screen
        pygame.display.flip()

        # Set FPS
        self.clock.tick(60)

    def mainLoop(self):

        # OBJECTIVE: Main function that controls the game

        # Create player
        player = Player(self, self.width // 2, self.height - 20)

        # Create alien
        alien = Alien(self, 30, 30)

        # Create alien generator
        generator = Generator(self)

        while self.continueGame:

            # Check if window was closed
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.continueGame = False

            # Update screen
            self.updateScreen(player)

        # Stop pygame
        pygame.quit()

if __name__ == "__main__":

    game = Game(840, 720)
    game.mainLoop()