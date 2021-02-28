import pygame

WHITE = (255, 255, 255)

class Bullet:

    LENGTH = 2
    HEIGHT = 4

    def __init__(self, game, xPosition, yPosition):

        # Declare variables
        self.game = game
        self.xPosition = xPosition
        self.yPosition = yPosition

    def draw(self):

        # OBJECTIVE: Draw bullet for player

        # Draw bullet on screen
        spriteSpec = pygame.Rect(self.xPosition, self.yPosition, self.LENGTH, self.HEIGHT)
        pygame.draw.rect(self.game.screen, WHITE, spriteSpec)

        # Adjust speed
        self.yPosition -= 2

    def drawForAlien(self):

        # OBJECTIVE: Draw bullet for alien

        # Draw bullet
        spriteSpecs = pygame.Rect(self.xPosition, self.yPosition, self.LENGTH, self.HEIGHT)
        pygame.draw.rect(self.game.screen, WHITE, spriteSpecs)

        # Adjust speed specifically for alien
        self.yPosition += 2