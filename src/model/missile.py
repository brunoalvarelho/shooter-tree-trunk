import os
import pygame


class Missile(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.velocity = 2
        self.image = pygame.image.load(os.path.join(os.getcwd(), "src/assets/missile.png"))
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 125
        self.rect.y = player.rect.y + 90
        self.origin_image = self.image
        self.angle = 0

    def remove(self):
        self.player.all_missiles.remove(self)

    def rotate(self):
        self.angle += 8
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        # delete item if touch monster
        if self.player.game.check_collision(self, self.player.game.all_monsters):
            self.remove()

        # delete item if not in screen
        if self.rect.x > 1080:
            self.remove()
