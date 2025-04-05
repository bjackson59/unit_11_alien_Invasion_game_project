import pygame
from typing import TYPE_CHECKING
from bullet import Bullet

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Arsenal:
    def __init__(self, game: 'AlienInvasion'):
        self.game = game
        self.settings = game.settings
        self.magazine = pygame.sprite.Group()

    def update_magazine(self):
        self.magazine.update()
        self._remove_bullets_offscreen()

    def _remove_bullets_offscreen(self):
        for bullet in self.magazine.copy():
            if bullet.rect.left >= 1200:
                self.magazine.remove(bullet)

    def draw(self):
        for bullet in self.magazine:
            bullet.draw_bullet()
    
    def fire_bullet(self):
        if len(self.magazine) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.magazine.add(new_bullet)
            return True
        return False