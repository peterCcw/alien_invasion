class Settings:
    """Keeps all of the game settings"""

    def __init__(self):
        """Initialization of game settings"""
        # Screen settings
        self.screen_width = 1024
        self.screen_height = 768
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 0.5

        # Bullet settings
        self.bullet_speed = 0.4
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
