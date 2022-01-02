import pygame
from src.model.game import Game

# generate game windows
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Shooter Tree Trunk")
screen = pygame.display.set_mode((1080, 720))
background = pygame.image.load("src/assets/background.jpg")

# generate game
game = Game()

# run the game
running = True
while running:
    # handle global environment (background,player,missile,alien,mummy)
    screen.blit(background, (0, -250))
    screen.blit(game.player.image, game.player.rect)
    game.player.update_health_bar(screen)
    game.player.all_missiles.draw(screen)
    game.all_monsters.draw(screen)

    # handle missile
    for missile in game.player.all_missiles:
        missile.move()

    # handle monster
    for monster in game.all_monsters:
        monster.move()
        monster.update_health_bar(screen)

    # handle game remotes
    if game.key_pressed.get(pygame.K_d) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
        if game.key_pressed.get(pygame.K_z) and game.player.rect.y > game.player.velocity:
            game.player.jump()
        elif game.key_pressed.get(pygame.K_z) is False \
                and game.player.rect.y < screen.get_height() - game.player.rect.height - game.player.velocity:
            game.player.fall_jump()
    elif game.key_pressed.get(pygame.K_q) and game.player.rect.x > 0:
        game.player.move_left()
        if game.key_pressed.get(pygame.K_z) and game.player.rect.y > game.player.velocity:
            game.player.jump()
        elif game.key_pressed.get(pygame.K_z) is False \
                and game.player.rect.y < screen.get_height() - game.player.rect.height - game.player.velocity:
            game.player.fall_jump()
    elif game.key_pressed.get(pygame.K_z) and game.player.rect.y > game.player.velocity:
        game.player.jump()
    elif game.key_pressed.get(pygame.K_z) is False \
            and game.player.rect.y < screen.get_height() - game.player.rect.height - game.player.velocity:
        game.player.fall_jump()

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

    clock.tick(120)