    import pygame
import time
import random

# class Character(object):
#     def __init__(self):
#         self.name = 'undefined'
#
#     def move(self):
#         if self.x == 480:
#             self.x = 0
#             self.x += 1
#         elif self.x == 0:
#             self.x = 480
#             self.x -=1
#         elif self.y == 510:
#             self.y = 0
#             self.y -= 1
#         elif self.y  == 0:
#             self.y = 510
#             self.y = += 1



class Monster(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # self.image = pygame.image.load('monster.png').convert_alpha()


    def moveright(self):
        self.x += 1

    def moveleft(self):
        self.x -= 1

    def movedown(self):
        self.y += 1

    def moveup(self):
        self.y -= 1

    def upright(self):
        self.x += 1
        self.y -= 1

    def downright(self):
        self.x -= 1
        self.y += 1

    def upleft(self):
        self.y += 1
        self.x -= 1

    def downleft(self):
        self.y -= 1
        self.x += 1

    # def monstericon(self):
    #     screen.blit(self.image, (self.x, self.y))

class Hero(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # self.image = pygame.image.load('hero.png').convert_alpha()

    def moveright(self):
        self.x += 1

    def moveleft(self):
        self.x -= 1

    def movedown(self):
        self.y += 1

    def moveup(self):
        self.y -= 1


def main():
    width = 510
    height = 480
    pygame.init()
    monster = Monster(150, 200)
    hero = Hero(255, 240)

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Monster Game')
    clock = pygame.time.Clock()

    # Game initialization
    image = pygame.image.load('background.png').convert_alpha()
    heroimage = pygame.image.load('hero.png').convert_alpha()
    monsterimage = pygame.image.load('monster.png').convert_alpha()
    stop_game = False

    while not stop_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop_game = True
        counter = 0
        movelist = ['movedown', 'moveup', 'moveleft', 'moveright', 'upright', 'downright', 'downleft', 'upleft']
        movement = movelist[random.randint(0, 7)]

        while counter <= 120:
            if movement == 'movedown':
                getattr(monster, movement)()
                screen.blit(image, (0, 0))
                screen.blit(heroimage, (255, 240))
                screen.blit(monsterimage, (monster.x, monster.y))
                pygame.display.update()
                clock.tick(60)

                if monster.y == 480:
                    monster.y = 0
                    getattr(monster, movement)()

                    screen.blit(image, (0, 0))
                    screen.blit(heroimage, (255, 240))
                    screen.blit(monsterimage, (monster.x, monster.y))
                    pygame.display.update()
                    clock.tick(60)
            elif movement == "moveup":
                getattr(monster, movement)()

                screen.blit(image, (0, 0))
                screen.blit(heroimage, (255, 240))
                screen.blit(monsterimage, (monster.x, monster.y))
                pygame.display.update()
                clock.tick(60)
                if monster.y == 0:
                    monster.y = 480
                    getattr(monster, movement)()

                    screen.blit(image, (0, 0))
                    screen.blit(heroimage, (255, 240))
                    screen.blit(monsterimage, (monster.x, monster.y))
                    pygame.display.update()
                    clock.tick(60)
            elif movement == "moveright":
                getattr(monster, movement)()

                screen.blit(image, (0, 0))
                screen.blit(heroimage, (255, 240))
                screen.blit(monsterimage, (monster.x, monster.y))
                pygame.display.update()
                clock.tick(60)
                if monster.x == 510:
                    monster.x = 0
                    getattr(monster, movement)()

                    screen.blit(image, (0, 0))
                    screen.blit(heroimage, (255, 240))
                    screen.blit(monsterimage, (monster.x, monster.y))
                    pygame.display.update()
                    clock.tick(60)
            elif movement == "moveleft":
                getattr(monster, movement)()

                screen.blit(image, (0, 0))
                screen.blit(heroimage, (255, 240))
                screen.blit(monsterimage, (monster.x, monster.y))
                pygame.display.update()
                clock.tick(60)
                if monster.x == 0:
                    monster.x = 510
                    getattr(monster, movement)()

                    screen.blit(image, (0, 0))
                    screen.blit(heroimage, (255, 240))
                    screen.blit(monsterimage, (monster.x, monster.y))
                    pygame.display.update()
                    clock.tick(60)
            counter += 1



        # Draw background


        # Game display


    pygame.quit()

if __name__ == '__main__':
    main()
