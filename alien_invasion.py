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
            # Waiting for key press or mouse click
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Refreshing the screen during each iteration
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # Displaying last modified screen
            pygame.display.flip()


if __name__ == '__main__':
    # Creating instance of game and running it
    ai = AlienInvasion()
    ai.run_game()
