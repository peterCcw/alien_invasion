import sys
import pygame


class AlienInvasion:
    """Main class which manages resources and game"""
    def __init__(self):
        """Initialize the game and create it's resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1024, 768))
        pygame.display.set_caption('Alien Invasion')

        # Defining background color
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Begin of main game loop"""
        while True:
            # Waiting for key press or mouse click
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Refreshing the screen during each iteration
            self.screen.fill(self.bg_color)

            # Displaying last modified screen
            pygame.display.flip()


if __name__ == '__main__':
    # Creating instance of game and running it
    ai = AlienInvasion()
    ai.run_game()
