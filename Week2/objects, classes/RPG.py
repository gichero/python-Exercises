"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""
class Character(object):
    def alive(self):
        return self.health > 0
        # if self.health >0:
        #     return True

    def print_status(self):
        print "The %s has health %d and %d power." % (self.name, self.health, self.power)
    #    print "The goblin has %d health and %d power." % (self.health, self.power)

    # def attack(self, target):
    #     target.health -= self.power
    #     print "%s does %d damage to %s." % (self.name, self.power, self.target)

class Hero(Character):
    def __init__(self):
        self.name = 'Hero'
        self.health = 10
        self.power = 5

    def attack(self, target):
        target.health -= self.power
        print "You do %d damage to the goblin." % self.power

    # def print_status(self):
    #     print "You have %d health and %d power." % (self.health, self.power)
        #print "The goblin has %d health and %d power." % (self.health, self.power)


class Goblin(Character):
    def __init__(self):
        self.name = 'goblin'
        self.health = 6
        self.power = 2

    def attack(self, target):
        target.health -= self.power
        print "The goblin does %d damage to you." % self.power
        if self.health <= 0:
            print "You are dead."

    # def print_status(self):
    # #     #print "You have %d health and %d power." % (self.health, self.power)
    #     print "The goblin has %d health and %d power." % (self.health, self.power)
# class Zombie(Character):
#     def __init__(self):

def main():
    hero = Hero()
    goblin = Goblin()


    while goblin.alive() and hero.alive():
        hero.print_status()
        goblin.print_status()

        print
        print "What do you want to do?"
        print "1. fight goblin"
        print "2. do nothing"
        print "3. flee"
        print "> ",
        input = raw_input()

        if input == "1":
            # Hero attacks goblin
            hero.attack(goblin)

        if goblin.health > 0:
            # Goblin attacks hero
            goblin.attack(hero)


main()
