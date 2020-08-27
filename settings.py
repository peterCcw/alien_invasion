class Settings:
    """Keeps all of the game settings"""

    def __init__(self):
        """Initialization of game settings"""
        # Screen settings
        self.screen_width = 1024
        self.screen_height = 768
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        self.alien_bullet_color = (255, 0, 0)
        self.alien_bullets_allowed = 1


        # Alien settings
        self.bouncing_height = 15
        self.fleet_drop_speed = 15

        # Speed of game change
        self.speedup_scale = 1.5

        # Score multiplier for each level
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings which are changed during the game"""
        self.ship_speed = 0.5
        self.bullet_speed = 0.7
        self.alien_speed = 0.5
        self.alien_bouncing_speed = 0.1
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_bouncing_speed *= self.speedup_scale
        if self.alien_bouncing_speed > self.bouncing_height:
            self.alien_bouncing_speed = self.bouncing_height

        self.alien_points = int(self.alien_points * self.score_scale)
