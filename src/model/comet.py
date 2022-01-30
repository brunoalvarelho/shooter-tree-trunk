import os
import pygame
import random


class Comet(pygame.sprite.Sprite):
    def __init__(self, comet_event):
        super().__init__()
        self.image = pygame.image.load(os.path.join(os.getcwd(), "src/assets/comet.png"))
        self.comet_event = comet_event
        self.rect = self.image.get_rect()
        self.rect.y = - random.randint(20, 600)
        self.rect.x = random.randint(20, 800)
        self.velocity = random.randint(1, 3)
        self.attack = 25

    def remove(self):
        self.comet_event.all_comets.remove(self)
        if len(self.comet_event.all_comets) == 0:
            self.comet_event.reset_bar_percent()
            self.comet_event.fall_mode = False
            self.comet_event.game.spawn_monster('mummy')
            self.comet_event.game.spawn_monster('mummy')

    def fall(self):
        if not self.comet_event.game.check_collision(self, self.comet_event.game.all_players):
            self.rect.y += self.velocity
        else:
            # monster attack player if touch it
            self.comet_event.game.player.damage(self.attack)
            self.remove()

        if self.rect.y >= 500:
            self.remove()