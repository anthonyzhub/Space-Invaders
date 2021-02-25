import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SCREEN_LENGTH = 840
SCREEN_HEIGHT = 720 

class Player(pygame.sprite.Sprite):

    def __init__(self, color, width, height):

        # Initialize parent class
        super().__init__()

        # Create ship
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(BLACK)

        # Draw ship on screen
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Get ship's dimensions
        self.rect = self.image.get_rect()

    def moveLeft(self, pixels):

        self.rect.x -= pixels

        if self.rect.x < 0:
            self.rect.x = 0

    def moveRight(self, pixels):

        self.rect.x += pixels

        if self.rect.x > 810:
            self.rect.x = 810