import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

SCREEN_LENGTH = 840
SCREEN_HEIGHT = 720

class Player(pygame.sprite.Sprite):

    LENGTH = 25
    HEIGHT = 10

    def __init__(self, game, xPosition, yPosition):

        # Initialize parent class
        super().__init__()

        # Declare variables
        self.game = game
        self.xPosition = xPosition
        self.yPosition = yPosition

    def draw(self):

        # OBJECTIVE: Draw ship on screen
        
        spriteSpecs = pygame.Rect(self.xPosition, self.yPosition, self.LENGTH, self.HEIGHT)
        pygame.draw.rect(self.game.screen, RED, spriteSpecs)

    def moveLeft(self):

        # While ship is still on the screen, it can be move to the left
        if not self.xPosition < 5:
            self.xPosition -= 5

    def moveRight(self):

        # While ship is still on the screen, it can be move to the right
        if not self.xPosition > SCREEN_LENGTH - 25:
            self.xPosition += 5

# class Bullet:

#     def __init__(self, game, xPosition, yPosition):

#         # Declare variables
#         self.game = game
#         self.xPosition = xPosition
#         self.yPosition = yPosition

#     def draw(self):

#         # Draw bullet on screen
#         spriteSpec = pygame.Rect(self.xPosition, self.yPosition, 2, 4)
#         pygame.draw.rect(self.game.screen, WHITE, spriteSpec)

#         # Adjust speed
#         self.yPosition -= 2