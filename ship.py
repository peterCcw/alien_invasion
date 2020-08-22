import pygame


class Ship:
    """Manages the player's ship"""

    def __init__(self, ai_game):
        """Initialize player's ship and it's initial location"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Loading image of the ship and getting its rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Every new ship appears at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Display player's ship at its current location"""
        self.screen.blit(self.image, self.rect)
