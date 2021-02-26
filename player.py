import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

SCREEN_LENGTH = 840
SCREEN_HEIGHT = 720 

class Player(pygame.sprite.Sprite):

    def __init__(self, game, xPosition, yPosition):

        # Initialize parent class
        super().__init__()

        # Declare variables
        self.game = game
        self.xPosition = xPosition
        self.yPosition = yPosition

    def draw(self):

        # OBJECTIVE: Draw ship on screen
        # print("Calling from player.draw()")
        spriteSpecs = pygame.Rect(self.xPosition, self.yPosition, 25, 10)
        pygame.draw.rect(self.game.screen, RED, spriteSpecs)