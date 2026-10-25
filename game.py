import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Python-Game")

running = True
x = 375
y = 500
bullet_x = 375
bullet_y = 500

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            bullet_x = x + 20
            bullet_y = y

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        x = x - 2
    if keys[pygame.K_d]:
        x = x + 2
    if keys[pygame.K_w]:
        y = y - 2
    if keys[pygame.K_s]:
        y = y + 2

    bullet_y = bullet_y - 5

    screen.fill((30, 30, 40))
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 50, 50))
    pygame.draw.rect(screen, (255, 255, 0), (bullet_x, bullet_y, 10, 20))
    pygame.display.flip()

pygame.quit()