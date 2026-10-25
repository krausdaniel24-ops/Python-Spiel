import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Python-Game")

running = True
x = 375
y = 500
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x = x - 2
    if keys[pygame.K_RIGHT]:
        x = x + 2
    if keys[pygame.K_UP]:
        y = y - 2
    if keys[pygame.K_DOWN]:
        y = y + 2


    screen.fill((30, 30, 40))
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 50, 50))
    pygame.display.flip()
pygame.quit()

    