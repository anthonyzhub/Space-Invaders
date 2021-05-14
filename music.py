import pygame

class Music:

    def __init__(self):
        
        # Initialize pygame's mixer()
        pygame.mixer.init()

        # Create music channels for each sound effect and song
        pygame.mixer.set_num_channels(10) # Default is 8

        # Load background music and play it infinitely
        self.backgroundChannel = pygame.mixer.Channel(0)
        self.backgroundMusic = pygame.mixer.Sound("One-Must-Fall-2097-remix.wav")
        self.backgroundChannel.play(self.backgroundMusic, -1) # <= Added -1 to loop infinite times

        # Load explosion sound effect
        self.explosionChannel = pygame.mixer.Channel(1)
        self.explosionSound = pygame.mixer.Sound("Explosion.wav")

    def playExplosion(self):

        # OBJECTIVE: Play an explosion sound effect when a bullet hits an alien or hero
        self.explosionChannel.play(self.explosionSound)