import pygame

GREEN = (0, 255, 00)

class Alien:

    def __init__(self, game, xPosition, yPosition):

        # Declare variables
        self.game = game
        self.xPosition = xPosition
        self.yPosition = yPosition

    def draw(self):

        # OBJECTIVE: Draw alien on screen
        spriteSpecs = pygame.Rect(self.xPosition, self.yPosition, 30, 30)
        pygame.draw.rect(self.game.screen, GREEN, spriteSpecs)