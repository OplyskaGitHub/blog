import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT
pygame.init()

BLACK = 0, 0, 0
WIGHT = 255, 255, 255

screen = width, height = 800, 600

BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 0, 0

main_surface = pygame.display.set_mode(screen)

ball = pygame.Surface((20, 20))
ball.fill(WHITE)
ball_rect = ball.get_rect()
ball_speed = 1

enemy = pygame.Surface((20, 20))
enemy.fill(RED)
enemy_rect = pygame.Rect(100, 100, enemy.get_size())
enemy_speed = 1

is_working = True

while is_working: 
    for event in pygame.event.get():
        if event.type == QUIT:
            is_working = False

    pressed_keys = pygame.key.get_pressed()

    if ball_rect.bottom >= height or ball_rect.top <= 0:
        ball.fill((255, 0, 0))
        ball_speed[1] = -ball_speed[1]
    
    main_surface.fill((BLACK))

    main_surface.blit(ball, ball_rect)
    main_surface.blit(enemy, enemy_rect)

    if pressed_keys[K_DOWN]:
        ball_rect = ball_rect.move(0, ball_speed)

    if pressed_keys[K_UP]:
        ball_rect = ball_rect.move(0, -ball_speed)

    if pressed_keys[K_RIGHT]:
        ball_rect = ball_rect.move(ball_speed, 0)
    
    if pressed_keys[K_LEFT]:
        ball_rect = ball_rect.move(-ball_speed, 0)

    enemy_rect = enemy_rect.move(-enemy_speed, 0)

    #main.surface.fill((155, 155,155))
    pygame.display.flip()

print ('')

