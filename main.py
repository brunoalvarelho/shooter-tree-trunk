import pygame
from src.model.game import Game

# generate game windows
pygame.init()
pygame.display.set_caption("Shooter Tree Trunk")
screen = pygame.display.set_mode((1080, 720))
background = pygame.image.load("src/assets/background.jpg")

# generate game
game = Game()

# run the game
running = True
while running:
    # handle global environment (background,player)
    screen.blit(background, (0, -250))
    screen.blit(game.player.image, game.player.rect)

    # handle game remotes
    if game.keyPressed.get(pygame.K_d) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
        if game.keyPressed.get(pygame.K_SPACE) and game.player.rect.y > game.player.velocity:
            game.player.jump()
        elif game.keyPressed.get(pygame.K_SPACE) is False \
                and game.player.rect.y < screen.get_height() - game.player.rect.height - game.player.velocity:
            game.player.fall_jump()
    elif game.keyPressed.get(pygame.K_q) and game.player.rect.x > 0:
        game.player.move_left()
        if game.keyPressed.get(pygame.K_SPACE) and game.player.rect.y > game.player.velocity:
            game.player.jump()
        elif game.keyPressed.get(pygame.K_SPACE) is False \
                and game.player.rect.y < screen.get_height() - game.player.rect.height - game.player.velocity:
            game.player.fall_jump()
    elif game.keyPressed.get(pygame.K_SPACE) and game.player.rect.y > game.player.velocity:
        game.player.jump()
    elif game.keyPressed.get(pygame.K_SPACE) is False \
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
            game.keyPressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.keyPressed[event.key] = False
