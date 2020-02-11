import pygame

pygame.init()
size = 300, 200
screen = pygame.display.set_mode(size)
screen.fill(pygame.Color('red'))
for i in range(13):
    if i == 0:
        pygame.draw.line(screen, (255, 255, 255), [0, 15], [300, 15], 2)
    else:
        pygame.draw.line(screen, (255, 255, 255), [0, 17 * (i + 1)], [300, 17 * (i + 1)], 2)
    if i % 2 != 0:
        for j in range(10):
            pygame.draw.line(screen, (255, 255, 255), [31 * j + 30, 17 * i], [31 * j + 30, 17 * (i + 1)], 2)
    else:
        if i != 0:
            for j in range(10):
                pygame.draw.line(screen, (255, 255, 255), [31 * j - 13, 17 * i], [31 * j - 13, 17 * (i + 1)], 2)
        else:
            for j in range(10):
                pygame.draw.line(screen, (255, 255, 255), [31 * j - 13, 0], [31 * j - 13, 15], 2)
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()