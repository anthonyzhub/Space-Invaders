import pygame

GREEN = (0, 255, 00)
LENGTH = 30
HEIGHT = 30

class Alien:

    def __init__(self, game, xPosition, yPosition):

        # Declare variables
        self.game = game
        self.xPosition = xPosition
        self.yPosition = yPosition

    def draw(self):

        # OBJECTIVE: Draw alien on screen

        # Draw alien
        spriteSpecs = pygame.Rect(self.xPosition, self.yPosition, LENGTH, HEIGHT)
        pygame.draw.rect(self.game.screen, GREEN, spriteSpecs)

        # Adjust alien speed
        self.yPosition += .05

    def detectCollision(self):

        # OBJECTIVE: Delete alien if a bullet hits it

        for firedBullet in self.game.bulletList:

            if (firedBullet.xPosition > self.xPosition and
                firedBullet.xPosition < self.xPosition + LENGTH and
                firedBullet.yPosition > self.yPosition and
                firedBullet.yPosition < self.yPosition + HEIGHT):

                    print("Alien, {}, got hit".format(self))

                    # Remove and delete bullet from list
                    self.game.bulletList.remove(firedBullet)
                    # del firedBullet # NOTE <= del and remove() both remove x element

                    # Remove and delete alien from list
                    self.game.aliensList.remove(self)
                    # del self

class Generator:

    def __init__(self, game):

        # Alien's personal bubble
        margin = 30
        width = 50

        # NOTE: Aliens are created from top to bottom, then moves on to next column
        # Create more aliens
        for xAxis in range(margin, game.width - margin, width): # range(start, stop, jump)
            for yAxis in range(margin, game.height // 2, width):
                
                # Create a new instance of alien and add it to game's list
                game.aliensList.append(Alien(game, xAxis, yAxis))