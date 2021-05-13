import pygame

BLUE = (0, 0, 255)
PURPLE = (190, 9, 255)
RED = (255, 0, 0)

class Barrier:

    # Regular dimensions
    LENGTH = 100
    HEIGHT = 15

    def __init__(self, game, xPosition, yPosition):

        self.game = game
        
        # Set X & Y position
        self.xPosition = xPosition
        self.yPosition = yPosition

        # How many hits it can take without disappearing
        self.lives = 3

    def draw(self):
        
        # OBJECTIVE: Depending on how many lives are left, draw barrier with a specific color

        if self.lives == 3:

            # Draw dimensions and sprite
            spriteSpecs = pygame.Rect(self.xPosition, self.yPosition, self.LENGTH, self.HEIGHT)
            pygame.draw.rect(self.game.screen, BLUE, spriteSpecs)

        elif self.lives == 2:

            # Draw dimensions and sprite
            spriteSpecs = pygame.Rect(self.xPosition, self.yPosition, self.LENGTH - 25, self.HEIGHT)
            pygame.draw.rect(self.game.screen, PURPLE, spriteSpecs)

        else:

            # Draw dimensions and sprite
            spriteSpecs = pygame.Rect(self.xPosition, self.yPosition, self.LENGTH - 50, self.HEIGHT)
            pygame.draw.rect(self.game.screen, RED, spriteSpecs)

    def detectCollision(self):

        # OBJECTIVE: Detect collision between barrier and aliens' bullets

        # Declare variable for length for future use
        currLength = self.LENGTH

        # Update currLength based on number of lives left
        if self.lives == 2:
            currLength = self.LENGTH - 25
        elif self.lives == 1:
            currLength = self.LENGTH - 50

        # Go through each bullet that was fired by aliens
        for firedBullet in self.game.alienBulletsList:

            if (firedBullet.xPosition > self.xPosition and
                firedBullet.xPosition < self.xPosition + currLength and
                firedBullet.yPosition > self.yPosition and
                firedBullet.yPosition < self.yPosition + self.HEIGHT):

                # print("{} hit {}".format(firedBullet, self))

                # Remove bullet
                self.game.alienBulletsList.remove(firedBullet)

                # Update barrier's life
                self.lives -= 1

    def livesLeft(self):

        # OBJECTIVE: Return False, if the barrier doesn't have enough lives left

        if self.lives == 0:
            return False

        return True

class Generator:

    def __init__(self, game):

        # OBJECTIVE: Draw 3 barriers at the lower half of the screen

        # Middle barrier
        game.barriersList.append(Barrier(game, (game.width // 2) - (Barrier.LENGTH // 2), game.height - 100))

        # Left barrier
        game.barriersList.append(Barrier(game, 50, game.height - 100))

        # Right barrier
        game.barriersList.append(Barrier(game, game.width - 150, game.height - 100))