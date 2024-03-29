import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Класс для управления пулями, выпущенными кораблем."""

    def __init__(self, settings, screen, ship):
        """Класс для управления пулями, выпущенными кораблем."""
        super().__init__()
        self.screen = screen

        # Создание пули в позиции (0,0) и назначение правильной позиции.
        self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Позиция пули хранится в вещественном формате.
        self.y = float(self.rect.y)

        self.color = settings.bullet_color
        self.speed_factor = settings.ship_speed_factor

    def update(self):
        """Перемещает пулю вверх по экрану."""
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """Перемещает пулю вверх по экрану."""
        pygame.draw.rect(self.screen, self.color, self.rect)
