import pygame
from pygame. constants import QUIT

pygame.init()

BLACK = 0, 0, 0
WIGHT = 255, 255, 255

screen = width, height = 800, 600

main_surface = pygame.display.set_mode(screen)

ball = pygame.Surface((10, 10))
ball.fill((WIGHT))
bal_rect = ball.get_rect()
ball_speed = [1, 1]

is_working = True

while is_working: 
    for event in pygame.event.get():
        if event.type == QUIT:
            is_working = False

    bal_rect = bal_rect.move(ball_speed)

    if bal_rect.bottom >= height or bal_rect.top <= 0:
        
        ball_speed[1] = -ball_speed[1]
       
    if bal_rect.right >= width or bal_rect.left <=0:

         ball_speed[0] = -ball_speed[0]


    main_surface.fill((BLACK))

    main_surface.blit(ball, (bal_rect))

    
    #main.surface.fill((155, 155,155))
    pygame.display.flip()



