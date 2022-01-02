import os
import pygame


class Monster(pygame.sprite.Sprite):
    def __init__(self, game, type_monster):
        super().__init__()
        self.game = game
        self.type_monster = type_monster
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.velocity = 1
        self.image = pygame.image.load(os.path.join(os.getcwd(), "src/assets/mummy.png"))
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 490

    def move(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
