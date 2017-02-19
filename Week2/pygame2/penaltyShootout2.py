import pygame
import random
import time


KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275

class Player(object):
    def __init__(self, x, y):
        self.name = 'player1'
        self.y = y
        self.y = y


class Goalie(object):
    def __init__(self, x, y):
        self.name = 'goalie'
        self.x = x
        self.y = y
        self.speed_x = 0
        self.speed_y = 0

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y

    # def moveright(self):
    #     self.x += 1
    #
    # def moveleft(self):
    #     self.x -=1


class Ball():
    def __init__(self, x, y):
        self.name = 'ball'
        self.x = x
        self.y = y


def main():

    width = 500
    height = 700
    player = Player(250, 200)
    goalie = Goalie(245, 10)
    ball = Ball(250, 180)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Penalty Shootout')
    # clock = pygame.time.Clock()

    image = pygame.image.load('football-pitch2.png').convert_alpha()
    playerimage = pygame.image.load('hero.png').convert_alpha()
    goalieimage = pygame.image.load('monster.png').convert_alpha()
    ballimage = pygame.image.load('football.png').convert_alpha()

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == KEY_DOWN:
                    goalie.speed_y = 1
                elif event.key == KEY_UP:
                    goalie.speed_y = -1
                elif event.key == KEY_LEFT:
                    goalie.speed_x = -1
                elif event.key == KEY_RIGHT:
                    goalie.speed_x = 1
            if event.type == pygame.KEYUP:
                if event.key == KEY_DOWN:
                    goalie.speed_y = 0
                elif event.key == KEY_UP:
                    goalie.speed_y = 0
                elif event.key == KEY_LEFT:
                    goalie.speed_x = 0
                elif event.key == KEY_RIGHT:
                    goalie.speed_x = 0


        # counter = 0
        # movelist = ['moveleft', 'moveright']
        # movement = movelist[random.randint(0, 1)]
        #
        # while counter <= 60:
        #     if movement == 'moveleft':
        #         getattr(goalie, movement)()
        #
        #         screen.blit(image, (0, 0))
        #         screen.blit(playerimage, (250, 200))
        #         screen.blit(goalieimage, (goalie.x, goalie.y))
        #         screen.blit(ballimage, (250, 180))
        #         pygame.display.update()
        #         clock.tick(60)
        #
        #         if goalie.x == 245:
        #             goalie.y = 10
        #             getattr(goalie, movement)()
        #
        #             screen.blit(image, (0, 0))
        #             screen.blit(playerimage, (250, 200))
        #             screen.blit(goalieimage, (goalie.x, goalie.y))
        #             screen.blit(ballimage, (250, 180))
        #             pygame.display.update()
        #             clock.tick(60)
        #
        #     elif movement == "moveright":
        #         getattr(goalie, movement)()
        #
        #         screen.blit(image, (0, 0))
        #         screen.blit(playerimage, (250, 200))
        #         screen.blit(goalieimage, (goalie.x, goalie.y))
        #         screen.blit(ballimage, (250, 180))
        #         pygame.display.update()
        #         clock.tick(60)
        #
        #         if goalie.x == 245:
        #             goalie.x = 10
        #             getattr(goalie, movement)()
        #
        #             screen.blit(image, (0, 0))
        #             screen.blit(playerimage, (250, 200))
        #             screen.blit(goalieimage, (goalie.x, goalie.y))
        #             screen.blit(ballimage, (250, 180))
        #             pygame.display.update()
        #             clock.tick(60)
        #     counter += 1

        # pygame.display.update()
        # clock.tick(60)
        #
        #
        #
        goalie.update()
        screen.blit(image, (0, 0))
        screen.blit(playerimage,(250,200))
        screen.blit(goalieimage,(245,10))
        screen.blit(ballimage,(250,180))

        pygame.display.update()
        # clock.tick(60)

    pygame.quit()

if __name__ == '__main__':

    main()
