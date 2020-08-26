class GameStats:
    """Monitoring game statistics"""
    def __init__(self, ai_game):
        """Initialize statistic data class"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Game set to inactive
        self.game_active = False

        # Best score
        self._initialize_high_score()

    def reset_stats(self):
        """Reset statistic data"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def _initialize_high_score(self):
        """Initialize high score by reading from the file"""
        try:
            file_object = open('best_score_txt', 'r')
        except FileNotFoundError:
            self.high_score = 0
        else:
            high_score = file_object.readline()
            self.high_score = int(high_score.strip())
            file_object.close()
