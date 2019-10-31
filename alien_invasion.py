import sys

import pygame
import game_functions as gf
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from game_stats import Game_stats


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    ship = Ship(ai_settings, screen)
    stats = Game_stats(ai_settings)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, aliens, ship)
    pygame.display.set_caption(ai_settings.game_name)

    while True:
        gf.check_evens(ship, bullets, ai_settings, screen)
        ship.update()
        bullets.update()
        gf.update_bullets(bullets, aliens, ship, ai_settings, screen)
        gf.update_aliens(ai_settings, stats, aliens, ship, bullets, screen)
        gf.update_screen(ship, bullets, aliens, ai_settings,  screen)


run_game()
