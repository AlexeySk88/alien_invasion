import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


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


def update_screen(ship, bullets, aliens, settings, screen):
    screen.fill(settings.bg_color)
    for bullet in bullets:
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)
    pygame.display.flip()


def update_bullets(bullets, aliens, ship, settings, screen):
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_aliens_collisions(aliens, bullets, ship, settings, screen)


def create_fleet(settings, screen, aliens, ship):
    """Создает флот пришельцев."""
    alien = Alien(settings, screen)
    number_aliens_x = get_number_aliens_x(settings, alien.rect.width)
    number_rows = get_number_rows(settings, alien.rect.height, ship.rect.height)
    for alien_row in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(settings, screen, aliens, alien_number, alien_row)


def get_number_aliens_x(settings, alien_width) -> int:
    """Вычисляет количество пришельцев в ряду."""
    avalible_space = settings.screen_width - alien_width * 2
    return int(avalible_space / (alien_width * 2))


def create_alien(settings, screen, aliens, alien_number, row_number):
    """Создает пришельца и размещает его в ряду."""
    new_alien = Alien(settings, screen)
    alien_width = new_alien.rect.width
    new_alien.x = alien_width + alien_width * 2 * alien_number
    new_alien.rect.x = new_alien.x
    new_alien.rect.y = new_alien.rect.height + new_alien.rect.height * 2 * row_number
    aliens.add(new_alien)


def get_number_rows(settings, alien_height, ship_height) -> int:
    """Определяет количество рядов, помещающихся на экране."""
    avalible_space_y = settings.screen_height - (alien_height * 3) - ship_height
    return int(avalible_space_y / (alien_height * 2))


def update_aliens(settings, stats, aliens, ship, bullets, screen):
    """
    Проверяет, достиг ли флот края экрана,
    после чего обновляет позиции всех пришельцев во флоте.
    """
    check_fleet_edges(settings, aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(stats, aliens, bullets, ship, settings, screen)


def change_fleet_directions(settings, aliens):
    """Опускает весь флот и меняет направление флота."""
    for alien in aliens.sprites():
        alien.rect.y += settings.aliens_fleet_drop_speed
    settings.fleet_direction *= -1


def check_fleet_edges(settings, aliens):
    """Реагирует на достижение пришельцем края экрана."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_directions(settings, aliens)
            break


def check_bullet_aliens_collisions(aliens, bullets, ship, settings, screen):
    """Проверка попаданий в пришельцев."""
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(settings, screen, aliens, ship)


def ship_hit(stats, aliens, bullets, ship, settings, screen):
    """Обрабатывает столкновение корабля с пришельцем."""
    stats.ship_left -= 1

    aliens.empty()
    bullets.empty()

    create_fleet(settings, screen, aliens, ship)
    ship.center_ship()

    sleep(0.5)
