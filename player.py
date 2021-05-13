import pygame

RED = (255, 0, 0)
ORANGE = (255, 140, 0)
GOLD = (255, 165, 0)

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

        # Player lives
        self.lives = 3

    def draw(self):

        # OBJECTIVE: Draw ship on screen
        
        # Draw ship's dimensions
        spriteSpecs = pygame.Rect(self.xPosition, self.yPosition, self.LENGTH, self.HEIGHT)

        # Change ship's color based on how many lives are left
        if self.lives == 3:
            shipColor = GOLD
        elif self.lives == 2:
            shipColor = ORANGE
        else:
            shipColor = RED

        # Draw ship on the screen
        pygame.draw.rect(self.game.screen, shipColor, spriteSpecs)

    def moveLeft(self):

        # While ship is still on the screen, it can be move to the left
        if not self.xPosition < 5:
            self.xPosition -= 5

    def moveRight(self):

        # While ship is still on the screen, it can be move to the right
        if not self.xPosition > SCREEN_LENGTH - 25:
            self.xPosition += 5

    def detectCollision(self):

        # OBJECTIVE: Check if ship got hit by alien bullets

        for firedBullet in self.game.alienBulletsList:

            if (firedBullet.xPosition > self.xPosition and
                firedBullet.xPosition < self.xPosition + self.LENGTH and
                firedBullet.yPosition > self.yPosition and
                firedBullet.yPosition < self.yPosition + self.HEIGHT):

                # Remove alien bullet
                self.game.alienBulletsList.remove(firedBullet)

                # Remove one life from player
                self.lives -= 1

    def livesLeft(self):

        # OBJECTIVE: Check if player has enough life to continue playing

        if self.lives == 0:
            return False

        return True