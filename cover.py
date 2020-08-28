import pygame
from pygame.sprite import Sprite


class Cover(Sprite):
    """Manages the cover"""

    def __init__(self, ai_game):
        """Initialize cover and it's initial location"""
        super().__init__()
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.damage_level = 4

        self.screen_rect = self.screen.get_rect()

        # Loading image of the cover and getting its rectangle
        self.image = pygame.image.load('images/cover.bmp')
        self.rect = self.image.get_rect()

    def blitme(self):
        """Display player's ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def damage_cover(self):
        """Damage cover and change it's image. After 4th hit cover
        is destroyed
        """
        self.damage_level -= 1
        if self.damage_level == 3:
            self.image = pygame.image.load('images/cover_damaged.bmp')
        if self.damage_level == 2:
            self.image = pygame.image.load('images/cover_badly_damaged.bmp')
        if self.damage_level == 1:
            self.image = pygame.image.load('images/cover_almost_destroyed.bmp')
        if self.damage_level == 0:
            self.ai_game.covers.remove(self)

