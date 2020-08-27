import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Represents single alien"""
    def __init__(self, ai_game):
        """Initialize alien and define its initial location"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Loading alien's image and defining its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Setting new alien near left upper corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Storaging direct location of the alien
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.bouncing_direction = -1
        self.current_bounce_distance = 0

    def check_edges(self):
        """Return True if alien reach is next to the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move alien left or right and bounce up and down"""
        # Horizontal movement
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        # Vertical movement
        self._bouncing_movement()

        self.rect.x = self.x
        self.rect.y = self.y

    def _bouncing_movement(self):
        """Change alien's y up and down"""
        # Calculating movement up or down
        shift = float(self.settings.alien_bouncing_speed * self.bouncing_direction)

        # Changing y and increasing bounce distance - current height of bounce
        self.y += shift
        self.current_bounce_distance += float(self.settings.alien_bouncing_speed)

        # Rounding because of inaccuracy of float calculations
        self.y = round(self.y, 2)
        self.current_bounce_distance = round(self.current_bounce_distance, 2)

        # Check if alien reached max height of bounce - switch direction
        if self.current_bounce_distance >= self.settings.bouncing_height:
            self.current_bounce_distance = 0
            self.bouncing_direction *= -1
