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
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 0.4
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 0.5
        self.fleet_drop_speed = 200
        # fleet_direction equal 1 means move right, -1 means move left
        self.fleet_direction = 1
