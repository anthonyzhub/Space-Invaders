import pygame

GREEN = (0, 255, 00)

class Alien:

    LENGTH = 30
    HEIGHT = 30
    # SPEED = .05

    def __init__(self, game, xPosition, yPosition):

        # Declare variables
        self.game = game
        self.xPosition = xPosition
        self.yPosition = yPosition

        # Keep track ship of movements
        self.timesMovedRight = 0
        self.timesMovedLeft = 0
        self.goRight = True # NOTE: Start game by having aliens move right first
        self.goLeft = False

    def moveDown(self):
        self.yPosition += 1

    def moveRight(self):
        
        # OBJECTIVE: Move alien limited times to the right

        # Update xPosition and counter variable
        self.xPosition += 1
        self.timesMovedRight += 1

        if self.timesMovedRight == 15:

            # Reset counter
            self.timesMovedRight = 0

            # Update boolean variables
            self.goRight = False
            self.goLeft = True

            # Move alien down
            self.moveDown()

    def moveLeft(self):
        
        # OBJECTIVE: Move alien limited times to the left

        # Update xPosition and counter variable
        self.xPosition -= 1
        self.timesMovedLeft += 1

        if self.timesMovedLeft == 15:

            # Reset counter
            self.timesMovedLeft = 0

            # Update boolean variables
            self.goLeft = False
            self.goRight = True

            # Move alien down
            self.moveDown()

    def draw(self):

        # OBJECTIVE: Draw alien on screen

        # Draw alien
        spriteSpecs = pygame.Rect(self.xPosition, self.yPosition, self.LENGTH, self.HEIGHT)
        pygame.draw.rect(self.game.screen, GREEN, spriteSpecs)
            
        # Move alien side-by-side
        if self.goRight == True:
            self.moveRight()
        elif self.goLeft == True:
            self.moveLeft()

        # Adjust alien speed
        # self.yPosition += .05

    def detectCollision(self):

        # OBJECTIVE: Delete alien if a bullet hits it

        for firedBullet in self.game.heroBulletsList:

            if (firedBullet.xPosition > self.xPosition and
                firedBullet.xPosition < self.xPosition + self.LENGTH and
                firedBullet.yPosition > self.yPosition and
                firedBullet.yPosition < self.yPosition + self.HEIGHT):

                    print("Alien, {}, got hit".format(self))

                    # Remove and delete bullet from list
                    self.game.heroBulletsList.remove(firedBullet)
                    # del firedBullet # NOTE <= del and remove() both remove x element

                    # Remove and delete alien from list
                    self.game.aliensList.remove(self)
                    # del self

class Generator:

    def __init__(self, game):

        # Alien's personal bubble
        margin = 30
        width = 50 # NOTE: Affects how many alien ships can fit in one row

        # NOTE: Aliens are created from top to bottom, then moves on to next column
        # Create more aliens
        for xAxis in range(margin, game.width - margin, width): # range(start, stop, jump)
            for yAxis in range(margin, game.height // 2, width):
                
                # Create a new instance of alien and add it to game's list
                game.aliensList.append(Alien(game, xAxis, yAxis))