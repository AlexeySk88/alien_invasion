import sys
import pygame
from bullet import Bullet


def check_evens(ship, bullets, settings, screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ship, settings, screen, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)


def check_keydown_event(event, ship, settings, screen, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(ship, bullets, settings, screen)
    elif event.key == pygame.K_q:
        sys.exit()


def fire_bullets(ship, bullets, settings, screen):
    if len(bullets) < settings.bullet_allowed:
        new_bullets = Bullet(settings, screen, ship)
        bullets.add(new_bullets)


def check_keyup_event(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ship, bullets, alien, settings, screen):
    screen.fill(settings.bg_color)
    for bullet in bullets:
        bullet.draw_bullet()

    ship.blitme()
    alien.blitme()
    pygame.display.flip()


def update_bullets(bullets):
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
