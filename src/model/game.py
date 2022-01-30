import pygame
from src.model.player import Player
from src.model.monster import Monster
from src.event.comet_event import CometFallEvent


class Game:
    def __init__(self):
        self.is_playing = False
        self.key_pressed = {}
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.all_monsters = pygame.sprite.Group()
        self.comet_event = CometFallEvent(self)

    def start(self):
        self.is_playing = True
        self.spawn_monster('mummy')
        self.spawn_monster('mummy')

    def run(self, screen):
        screen.blit(self.player.image, self.player.rect)
        self.player.update_health_bar(screen)
        self.player.all_missiles.draw(screen)
        self.all_monsters.draw(screen)
        self.comet_event.update_bar(screen)
        self.comet_event.all_comets.draw(screen)

        # handle comet
        for comet in self.comet_event.all_comets:
            comet.fall()

        # handle missile
        for missile in self.player.all_missiles:
            missile.move()

        # handle monster
        for monster in self.all_monsters:
            monster.move()
            monster.update_health_bar(screen)

        # handle game remotes
        if self.key_pressed.get(pygame.K_d) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
            if self.key_pressed.get(pygame.K_z) and self.player.rect.y > self.player.velocity:
                self.player.jump()
            elif self.key_pressed.get(pygame.K_z) is False \
                    and self.player.rect.y < screen.get_height() - self.player.rect.height - self.player.velocity:
                self.player.fall_jump()
        elif self.key_pressed.get(pygame.K_q) and self.player.rect.x > 0:
            self.player.move_left()
            if self.key_pressed.get(pygame.K_z) and self.player.rect.y > self.player.velocity:
                self.player.jump()
            elif self.key_pressed.get(pygame.K_z) is False \
                    and self.player.rect.y < screen.get_height() - self.player.rect.height - self.player.velocity:
                self.player.fall_jump()
        elif self.key_pressed.get(pygame.K_z) and self.player.rect.y > self.player.velocity:
            self.player.jump()
        elif self.key_pressed.get(pygame.K_z) is False \
                and self.player.rect.y < screen.get_height() - self.player.rect.height - self.player.velocity:
            self.player.fall_jump()

    def spawn_monster(self, type_monster):
        self.all_monsters.add(Monster(self, type_monster))

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def game_over(self):
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.all_players = pygame.sprite.Group()
        self.all_players.add(self.player)
        self.player.rect.y = 450
        self.comet_event.all_comets = pygame.sprite.Group()
        self.comet_event.reset_bar_percent()
        self.is_playing = False
