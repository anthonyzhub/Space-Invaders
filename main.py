#! /usr/bin/python3

# Reference: https://itnext.io/creating-space-invaders-clone-in-pygame-ea0f5336c677
# Reference: https://github.com/janjilecek/pygame-invaders/blob/master/main.py

import pygame
from player import Player
from player import Bullet
from alien import Alien
from alien import Generator

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

class Game:

    screen = None
    aliensList = list()
    bulletList = list()

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

        for bullet in self.bulletList:
            bullet.draw()

        # Update screen
        pygame.display.flip()

        # Set FPS
        self.clock.tick(60)

    def deleteBullets(self):

        # OBJECTIVE: Delete bullets from list once they leave the screen

        # Exit if list is empty
        if len(self.bulletList) == 0:
            return None

        # Iterate list and check if a bullet left the screen
        for firedBullet in self.bulletList:

            if firedBullet.yPosition <= 0:
                print("Deleting {}".format(firedBullet))

                # Remove bullet from list
                self.bulletList.remove(firedBullet)

                # Delete bullet
                # del firedBullet

    def fireBullets(self, player):

        # OBJECTIVE: Fire at most 3 bullets when space bar is pressed

        # Exit if more than 3 bullets were fired
        if len(self.bulletList) >= 3:
            print("3 bullets were already fired")
            return None

        # Create and add new bullet to list
        self.bulletList.append(Bullet(self, player.xPosition, player.yPosition))

    def alienCollision(self):

        # OBJECTIVE: Check if an alien got hit by a bullet

        for alien in self.aliensList:
            alien.detectCollision()

    def mainLoop(self):

        # OBJECTIVE: Main function that controls the game

        # Create player
        player = Player(self, self.width // 2, self.height - 20)

        # Create alien
        alien = Alien(self, 30, 30)

        # Create alien generator
        generator = Generator(self)

        while self.continueGame:

            # Look for events from the user
            for event in pygame.event.get():

                # When "close window" button is pressed
                if event.type == pygame.QUIT:
                    self.continueGame = False

                # When spacebar is pressed, fire bullets
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        self.fireBullets(player)

            # Get keys pressed
            keysPressed = pygame.key.get_pressed()

            # When arrow buttons are pressed, move player
            if keysPressed[pygame.K_LEFT]:
                player.moveLeft()

            if keysPressed[pygame.K_RIGHT]:
                player.moveRight()

            # Delete aliens that were hit by bullets
            self.alienCollision()

            # Delete fired bullets that left the screen
            self.deleteBullets()

            # Update screen
            self.updateScreen(player)

        # Stop pygame
        pygame.quit()

if __name__ == "__main__":

    game = Game(840, 720)
    game.mainLoop()