import pygame
import math
from src.model.game import Game

# generate game windows
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Shooter Tree Trunk")
screen = pygame.display.set_mode((1080, 720))
background = pygame.image.load("src/assets/background.jpg")
banner = pygame.image.load("src/assets/banner.png")
banner = pygame.transform.scale(banner, (500, 500))
banner_position = banner.get_rect()
banner_position.x = math.ceil(screen.get_width() / 4)
play_button = pygame.image.load("src/assets/button.png")
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_position = play_button.get_rect()
play_button_position.x = math.ceil(screen.get_width() / 3.3)
play_button_position.y = math.ceil(screen.get_height() / 1.8)

# generate game
game = Game()

# run the game
running = True
while running:
    # handle global environment (background,player,missile,alien,mummy)
    screen.blit(background, (0, -250))

    # run game
    if game.is_playing:
        game.run(screen)
    else:
        screen.blit(play_button, play_button_position)
        screen.blit(banner, banner_position)

    pygame.display.flip()  # update full display surface to the screen

    # handle pygame setting
    for event in pygame.event.get():
        # quit the game
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            game.key_pressed[event.key] = True
            if event.key == pygame.K_SPACE:
                game.player.launch_missile()
        elif event.type == pygame.KEYUP:
            game.key_pressed[event.key] = False
        elif event.type == pygame.MOUSEBUTTONDOWN and play_button_position.collidepoint(event.pos):
            game.start()

    clock.tick(120)
