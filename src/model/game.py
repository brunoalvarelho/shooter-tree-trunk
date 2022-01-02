import pygame
from src.model.player import Player
from src.model.monster import Monster


class Game:
    def __init__(self):
        self.key_pressed = {}
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.all_monsters = pygame.sprite.Group()
        self.spawn_monster('mummy')
        self.spawn_monster('mummy')

    def spawn_monster(self, type_monster):
        self.all_monsters.add(Monster(self, type_monster))

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
