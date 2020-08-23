import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Represents single alien"""
    def __init__(self, ai_game):
        """Initialize alien and define its initial location"""
        super().__init__()
        self.screen = ai_game.screen

        # Loading alien's image and defining its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Setting new alien near left upper corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Storaging direct horizontal location of the alien
        self.x = float(self.rect.x)
