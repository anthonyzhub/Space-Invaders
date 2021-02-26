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