class GameStats:
    """Monitoring game statistics"""
    def __init__(self, ai_game):
        """Initialize statistic data class"""
        self.settings = ai_game.settings
        self.reset_stats()
        # Game set to active
        self.game_active = True

    def reset_stats(self):
        """Reset statistic data"""
        self.ships_left = self.settings.ship_limit
