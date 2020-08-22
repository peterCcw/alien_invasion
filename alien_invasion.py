import sys
import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """Manages resources and the game"""

    def __init__(self):
        """Initialize the game and create it's resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')

        self.ship = Ship(self)

    def run_game(self):
        """Begin of main game loop"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        """React for events generated by the keyboard and the mouse"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                elif event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
                elif event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False

    def _update_screen(self):
        """Update images on the screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Displaying last modified screen
        pygame.display.flip()


if __name__ == '__main__':
    # Creating instance of game and running it
    ai = AlienInvasion()
    ai.run_game()
