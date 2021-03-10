#! /usr/bin/python3

# Reference: https://itnext.io/creating-space-invaders-clone-in-pygame-ea0f5336c677
# Reference: https://github.com/janjilecek/pygame-invaders/blob/master/main.py

import pygame
from player import Player
from bullet import Bullet
from alien import Alien
from alien import Generator as aGenerator
from barrier import Barrier
from barrier import Generator as bGenerator

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

class Game:

    screen = None

    # Declare list per sprites
    aliensList = list()
    heroBulletsList = list()
    alienBulletsList = list()
    barriersList = list()

    # Declare variables for aliens for future use
    # NOTE: This is to adjust how many aliens can fire back based on how many aliens have been destroyed
    currAliensDestroyed = 0
    aliensFiringRate = 5
    oldAliensDestroyed = currAliensDestroyed

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

        for heroBullet in self.heroBulletsList:
            heroBullet.draw()

        for alienBullet in self.alienBulletsList:
            alienBullet.drawForAlien()

        for barrier in self.barriersList:
            barrier.draw()

        # Update screen
        pygame.display.flip()

        # Set FPS
        self.clock.tick(60)

    def deleteHerosBullets(self):

        # OBJECTIVE: Delete bullets from list once they leave the screen

        # Exit if list is empty
        if len(self.heroBulletsList) == 0:
            return None

        # Iterate list and check if a bullet left the screen
        for firedBullet in self.heroBulletsList:

            if firedBullet.yPosition <= 0:
                print("Deleting {}".format(firedBullet))

                # Remove bullet from list
                self.heroBulletsList.remove(firedBullet)

    def heroFiresBullet(self, player):

        # OBJECTIVE: Fire at most 3 bullets when space bar is pressed

        # Exit if more than 3 bullets were fired
        if len(self.heroBulletsList) >= 3:
            print("3 bullets were already fired")
            return None

        # Create and add new bullet to list
        self.heroBulletsList.append(Bullet(self, player.xPosition + (player.LENGTH // 2), player.yPosition))

    def deleteAlienBullets(self):

        # OBJECTIVE: Delete bullets fired from aliens if they left the screen

        for alienBullet in self.alienBulletsList:

            if alienBullet.yPosition > self.height:
                self.alienBulletsList.remove(alienBullet)

    def alienFiresBullet(self, player):

        # OBJECTIVE: Let a few aliens fire back

        # Only let aliens fire a certain amount of times
        if len(self.alienBulletsList) > self.aliensFiringRate:
            return None

        # Allow certain aliens to shoot
        margin = 10
        for alien in self.aliensList:
            
            # If alien is within player's x-position, then fire a bullet
            if (alien.xPosition > player.xPosition - margin and
                alien.xPosition < player.xPosition + player.LENGTH + margin):

                    # Exit if certain amount of bullets were already taken.
                    if len(self.alienBulletsList) >= self.aliensFiringRate:
                        break

                    self.alienBulletsList.append(Bullet(self, alien.xPosition + (alien.LENGTH // 2), alien.yPosition))

    def adjustAliensFiringRate(self):

        # OBJECTIVE: Adjust firing rate of bullets based on how many aliens were destroyed

        # If-condition was added to stop increasing firing rate, if "self.aliensDestroyed" was stuck on a multiple of 5
        if self.currAliensDestroyed != self.oldAliensDestroyed:

            # For every 5th alien destoryed, allow 3 more aliens to shoot
            if self.currAliensDestroyed % 5 == 0:

                # Update firing rate
                self.aliensFiringRate += 3

                # Update placeholder
                self.oldAliensDestroyed = self.currAliensDestroyed

    def alienCollision(self):

        # OBJECTIVE: Check if an alien got hit by a bullet

        for alien in self.aliensList:
            alien.detectCollision()

    def heroCollision(self, player):

        # OBJECTIVE: Check if hero got hit by a bullet
        player.detectCollision()

    def barrierCollision(self):

        # OBJECTIVE: Check if any barrier got hit

        for barrier in self.barriersList:
            barrier.detectCollision()

    def barrierLives(self):

        # OBJECTIVE: Delete barrier, if it doesn't have enough lives

        for barrier in self.barriersList:

            if barrier.livesLeft() == False:
                self.barriersList.remove(barrier)

    def playerLives(self, player):

        # OBJECTIVE: Update boolean variable if doesn't have enough lives left

        if player.livesLeft() == False:
            print("Game Over!")
            self.continueGame = False

    def mainLoop(self):

        # OBJECTIVE: Main function that controls the game

        # Create player
        player = Player(self, self.width // 2, self.height - 20)

        # Create alien
        alien = Alien(self, 30, 30)

        # Create alien generator
        alienGenerator = aGenerator(self)

        # Create barriers by using a generator
        barrierGenerator = bGenerator(self)

        while self.continueGame:

            # Look for events from the user
            for event in pygame.event.get():

                # When "close window" button is pressed
                if event.type == pygame.QUIT:
                    self.continueGame = False

                # When spacebar is pressed, fire bullets
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        self.heroFiresBullet(player)

            # Get keys pressed
            keysPressed = pygame.key.get_pressed()

            # When arrow buttons are pressed, move player
            if keysPressed[pygame.K_LEFT]:
                player.moveLeft()

            if keysPressed[pygame.K_RIGHT]:
                player.moveRight()

            # Delete aliens that were hit by bullets
            self.alienCollision()

            # Adjust aliens' firing rate
            self.adjustAliensFiringRate()

            # Let the aliens fireback
            self.alienFiresBullet(player)

            # Check if any barriers got hit by an alien bullet
            self.barrierCollision()

            # Update barriers' life points
            self.barrierLives()

            # Check if hero got hit by a bullet
            self.heroCollision(player)

            # Check if hero has enough lives to continue
            self.playerLives(player)

            # Delete fired bullets that left the screen
            self.deleteHerosBullets()
            self.deleteAlienBullets()

            # Update screen
            self.updateScreen(player)

        # Stop pygame
        pygame.quit()

if __name__ == "__main__":

    game = Game(840, 720)
    game.mainLoop()