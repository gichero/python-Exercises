import pygame

class Square(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

x = 400
y = 400

pygame.init()
screen = pygame.display.set_mode((600, 600))

stop_game = False
while not stop_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop_game = True

    x += 1
    y += 1

    screen.fill((0, 0, 0))

    pygame.draw.rect(
        screen,
        (244, 244, 66),
        (x, y, 50, 50),
        0)
    #
    pygame.display.update()


pygame.quit()
