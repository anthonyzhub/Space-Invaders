import pygame

RED = (255, 0, 0)
BLACK = (0, 0, 0)

class Bullet(pygame.sprite.Sprite):

    def __init__(self, width, height):

        # Initialize parent class
        super().__init__()

        # Create builet
        self.image = pygame.Surface([width, height])
        self.image.fill(RED)
        self.image.set_colorkey(BLACK)

        # Draw bullet on screen
        pygame.draw.rect(self.image, RED, [0, 0, width, height])

        # Get bullet's dimensions
        self.rect = self.image.get_rect()

    def moveUp(self, pixels):

        self.rect.y -= pixels