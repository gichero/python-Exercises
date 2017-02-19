import pygame
import random
import time


KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275

class Player(object):
    def __init__(self, x, y):
        self.name = 'player'
        self.y = y
        self.y = y

    def render(self,screen):
         pygame.image.load('monster.png').convert_alpha()


class Goalie(object):
    def __init__(self, x, y):
        self.name = 'goalie'
        self.x = 0
        self.y = 0
        self.speed_x = 0
        self.speed_y = 0

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def render(self, screen):
         pygame.image.load('howard.png').convert_alpha()

class Ball():
    def __init__(self, x, y):
        self.name = 'ball'
        self.x = x
        self.y = y

    def render(self, screen):
         pygame.image.load('football.png').convert_alpha()


def main():
    # declare size of canvas
    width = 500
    height = 700

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Penalty Shootout')
    # clock = pygame.time.Clock()

    # image = pygame.image.load('football-pitch2.png').convert_alpha()
    # playerimage = pygame.image.load('monster.png').convert_alpha()
    # goalieimage = pygame.image.load('howard.png').convert_alpha()
    # ballimage = pygame.image.load('football.png').convert_alpha()

    #game initialization
    player = Player(250, 200)
    goalie = Goalie(245, 10)
    ball = Ball(250, 180)

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():
            # Event handling
            if event.type == pygame.KEYDOWN:
            # activate the cooresponding speeds
            # when an arrow key is pressed down
                if event.key == KEY_DOWN:
                    goalie.speed_y = 5
                elif event.key == KEY_UP:
                    goalie.speed_y = -5
                elif event.key == KEY_LEFT:
                    goalie.speed_x = -5
                elif event.key == KEY_RIGHT:
                    goalie.speed_x = 5
            if event.type == pygame.KEYUP:
                # deactivate the cooresponding speeds
                # when an arrow key is released
                if event.key == KEY_DOWN:
                    goalie.speed_y = 0
                elif event.key == KEY_UP:
                    goalie.speed_y = 0
                elif event.key == KEY_LEFT:
                    goalie.speed_x = 0
                elif event.key == KEY_RIGHT:
                    goalie.speed_x = 0
            if event.type == pygame.QUIT:
                stop_game = True

        goalie.update()

        image = pygame.image.load('football-pitch2.png').convert_alpha()
        playerimage = pygame.image.load('monster.png').convert_alpha()
        goalieimage = pygame.image.load('howard.png').convert_alpha()
        ballimage = pygame.image.load('football.png').convert_alpha()

        goalie.render(screen)

        screen.blit(image, (0, 0))
        screen.blit(playerimage,(250,200))
        screen.blit(goalieimage,(245, 10))
        screen.blit(ballimage,(250,180))

        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':

    main()
