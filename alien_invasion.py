import sys

import pygame
import game_functions as gf
from pygame.sprite import Group
from settings import Settings
from ship import Ship


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    ship = Ship(ai_settings, screen)
    bullets = Group()
    pygame.display.set_caption(ai_settings.game_name)

    while True:
        gf.check_evens(ship, bullets, ai_settings, screen)
        ship.update()
        bullets.update()
        gf.update_bullets(bullets)
        gf.update_screen(ship, bullets, ai_settings,  screen)


run_game()
