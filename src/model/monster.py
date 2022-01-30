import os
import pygame
import random


class Monster(pygame.sprite.Sprite):
    def __init__(self, game, type_monster):
        super().__init__()
        self.game = game
        self.type_monster = type_monster
        self.health = 100
        self.max_health = 100
        self.attack = 3
        self.velocity = random.randint(1, 3)
        self.image = pygame.image.load(os.path.join(os.getcwd(), "src/assets/mummy.png"))
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 500)
        self.rect.y = 490

    def remove(self):
        self.game.all_monsters.remove(self)

    def move(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        else:
            # monster attack player if touch it
            self.game.player.damage(self.attack)

        # delete item if not in screen
        if self.rect.x < 0:
            self.health = self.max_health
            self.velocity = random.randint(1, 3)
            self.rect.x = 1000 + random.randint(0, 500)

    def damage(self, damage):
        self.health -= damage

        # If monster die create new monster
        if self.health < 0:
            if self.game.comet_event.is_full_loaded():
                self.game.all_monsters.remove(self)
                self.game.comet_event.attempt_fall(number_comet=random.randint(10, 20))
            else:
                self.health = self.max_health
                self.velocity = random.randint(1, 3)
                self.rect.x = 1000 + random.randint(0, 500)

    def update_health_bar(self, surface):
        pygame.draw.rect(surface, (50, 50, 50), [self.rect.x + 10, self.rect.y - 5, self.max_health, 5])
        pygame.draw.rect(surface, (138, 252, 0), [self.rect.x + 10, self.rect.y - 5, self.health, 5])
