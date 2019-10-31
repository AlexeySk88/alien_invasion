class Game_stats():
    """Отслеживание статистики для игры Alien Invasion."""

    def __init__(self, settings):
        self.settings = settings
        self.reset_stats()

    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры."""
        self.ship_left = self.settings.ship_limit
