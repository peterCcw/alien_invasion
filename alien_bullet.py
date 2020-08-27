import random

import pygame
from pygame.sprite import Sprite


class AlienBullet(Sprite):
    """Manages bullets shot by the aliens"""
    def __init__(self, ai_game):
        """Create the bullet obj in the random alien's location"""
        super().__init__()
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.alien_bullet_color

        # Creating the bullet rectangle in the (0, 0) point and defining its
        # proper location on random alien
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        alien_shoot = random.choice(self.ai_game.aliens.sprites())
        self.rect.midbottom = alien_shoot.rect.midbottom

        # Vertical location kept as float
        self.y = float(self.rect.y)

    def update(self):
        """Change bullet's location"""
        # Updating the bullet's location
        self.y += self.settings.bullet_speed
        # Updating the bullet's rect's location
        self.rect.y = self.y

    def draw_bullet(self):
        """Display bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
