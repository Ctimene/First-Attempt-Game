import pygame

pygame.init()

window_width = 800
window_height = 600

window = pygame.display.set_mode((window_width, window_height))
window.fill((0, 0, 0))
pygame.display.set_caption("My First Pygame")

player = pygame.Rect((300, 250, 50, 50))

run = True
while run:

    window.fill((0, 0, 0,))

    pygame.draw.rect(window, (255, 0, 0), player)

    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-2, 0)
    elif key[pygame.K_d] == True:
        player.move_ip(2, 0)
    elif key[pygame.K_w] == True:
        player.move_ip(0, -2)
    elif key[pygame.K_s] == True:
        player.move_ip(0, 2)
    elif key[pygame.K_c] == True:
        if window.fill == (0, 0, 0):
            window.fill((255, 255, 255))
            pygame.draw.rect(window, (0, 255, 0), player)
        else:
            window.fill((0, 0, 0))
            pygame.draw.rect(window, (255, 0, 0), player)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
    pygame.display.update()

pygame.quit()