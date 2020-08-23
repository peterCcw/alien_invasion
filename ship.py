import pygame


class Ship:
    """Manages the player's ship"""

    def __init__(self, ai_game):
        """Initialize player's ship and it's initial location"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.screen_rect = self.screen.get_rect()

        # Loading image of the ship and getting its rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Every new ship appears at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Horizontal location kept as float
        self.x = float(self.rect.x)

        # Flags indicating move of the ship
        self.moving_left = False
        self.moving_right = False

    def update(self):
        """Update location of the ship depending on the move flag"""
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        # Update rect obj by self.x value
        self.rect.x = self.x

    def blitme(self):
        """Display player's ship at its current location"""
        self.screen.blit(self.image, self.rect)
