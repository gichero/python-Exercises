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
        # self.power = 10
        # self.speed = 20

class Goalie(object):
    def __init__(self, x, y):
        self.name = 'goalie'
        self.x = x
        self.y = y

    def moveright(self):
        self.x += 1

    def moveleft(self):
        self.x -=1

    def move():
        pass

        self.power = 20
        self.speed = 10

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
    clock = pygame.time.Clock()
    stop_game = False
    gameExit = False
    image = pygame.image.load('football-pitch2.png').convert_alpha()
    playerimage = pygame.image.load('monster.png').convert_alpha()
    goalieimage = pygame.image.load('howard.png').convert_alpha()
    ballimage = pygame.image.load('football.png').convert_alpha()
    counter = 0

    while not stop_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop_game = True

        counter = 0
        goalie = Goalie(165, 7)

        goaliemove = [goalie.moveright, goalie.moveleft]
        moveright  = 165
        moveleft = 300
        movement = goaliemove[random.randint(0,1)]


        if counter <= 60:
            # if movement == moveright and movement == moveleft:
            #     movement +=1
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_LEFT:
                    x -= 10
                if event.type == pygame.K_RIGHT:
                    x -= 10

                screen.blit(image,(0, 0))
                screen.blit(playerimage,(250,200))
                screen.blit(goalieimage,(goalie.x, goalie.y))
                screen.blit(ballimage,(250,180))

                pygame.display.update()
                clock.tick(10)

            # if movement >=165 and movement <= 300:
            #
            #      movement +=1
            #      getattr(goalie, movement)()

            movement()

            counter = 0


            screen.blit(image,(0, 0))
            screen.blit(playerimage,(250,200))
            screen.blit(goalieimage,(goalie.x, goalie.y))
            screen.blit(ballimage,(250,180))

            pygame.display.update()
            clock.tick(10)

        screen.blit(image, (0, 0))
        screen.blit(playerimage,(250,200))
        screen.blit(goalieimage,(goalie.x, goalie.y))
        screen.blit(ballimage,(250,180))

        pygame.display.update()
        clock.tick(10)


    pygame.quit()

if __name__ == '__main__':
    main()
