import pygame
import random
import time

class Character(object):
    def __init__(self):
        self.name = '<undefined>'
        self.power = power
        self.speed = speed

class Player1(Character):
    def __init__(self, x, y):
        self.name = 'player1'
        self.y = y
        self.y = y
        # self.power = 10
        # self.speed = 20

class Goalie(Character):
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

        # self.power = 20
        # self.speed = 10

def main():

    width = 500
    height = 700
    player1 = Player1(250, 200)
    goalie = Goalie(245, 10)
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Penalty Shootout')
    clock = pygame.time.Clock()
    stop_game = False

    image = pygame.image.load('football-pitch2.png').convert_alpha()
    playerimage = pygame.image.load('hero.png').convert_alpha()
    # player2 = pygame.image.load().convert_alpha()
    goalieimage = pygame.image.load('monster.png').convert_alpha()
    # ballimage = pygame.image.load('footbal.png').convert_alpha()
    counter = 0
    while not stop_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop_game = True

        counter = 0
        goalie = Goalie(165, 10)
        goaliemove = [goalie.moveright, goalie.moveleft]
        moveright  = 165
        moveleft = 300
        movement = goaliemove[random.randint(0,1)]


        if counter <= 60:
            if movement == moveright and movement == moveleft:
                movement +=1




            #  if movement >=165 and movement <= 300:
             #
            #      movement +=1
            #      getattr(goalie, movement)()

            movement()

            counter = 0


            screen.blit(image, (0, 0))
            screen.blit(playerimage,(250,200))
            screen.blit(goalieimage,(goalie.x, goalie.y))

            pygame.display.update()
            clock.tick(60)

        screen.blit(image, (0, 0))
        screen.blit(playerimage,(250,200))
        screen.blit(goalieimage,(goalie.x, goalie.y))

        pygame.display.update()
        clock.tick(60)


    pygame.quit()

if __name__ == '__main__':
    main()
