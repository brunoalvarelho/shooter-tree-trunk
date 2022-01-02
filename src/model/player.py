import os
import pygame


class Player(pygame.sprite.Sprite):
    # Player constructor
    def __init__(self, ):
        super().__init__()
        self.health = 100
        self.maxHealth = 100
        self.attack = 10
        self.velocity = 1
        self.gravity = 2
        self.image = pygame.image.load(os.path.join(os.getcwd(), "src/assets/player.png"))
        self.rect = self.image.get_rect()
        self.rect.y = 450

    def move_left(self):
        self.rect.x -= self.velocity

    def move_right(self):
        self.rect.x += self.velocity

    def jump(self):
        self.rect.y -= self.gravity

    def fall_jump(self):
        if self.rect.y + self.gravity > 450:
            self.rect.y = 450
        else:
            self.rect.y += self.gravity
