"""
Added a store. The hero can now buy a tonic or a sword. A tonic will add 2 to the hero's health wherease a sword will add 2 power.
"""
import random
import time

class Character(object):
    def __init__(self):
        self.name = '<undefined>'
        self.health = 10
        self.power = 5
        self.coins = 30

    def alive(self):
        return self.health > 0

    def attack(self, enemy):
        if not self.alive():
            return
        print "%s attacks %s" % (self.name, enemy.name)
        enemy.receive_damage(self.power)
        time.sleep(0.5)

    def receive_damage(self, points):
        self.health -= points
        print "%s received %d damage." % (self.name, points)
        if self.health <= 0:
            print "%s is dead." % self.name

    def print_status(self):
        print "%s has %d health and %d power." % (self.name, self.health, self.power)

class Hero(Character):
    def __init__(self):
        self.name = 'hero'
        self.health = 143
        self.power = 35
        self.coins = 30

    def restore(self):
        self.health = 10
        print "Hero's health is restored to %d!" % self.health
        time.sleep(1)

    def buy(self, item):
        if self.coins - item.cost < 0:
            print 'you are out of coins'
        else:
            self.coins -= item.cost
            item.apply(hero)

    # def receive_damage(self, points):
    #     self.health -= points
    #     print "%s received %d damage." % (self.name, points)
    #     if self.health <= 0:
    #         print "%s is dead." % self.name


    # def attack(self, enemy):
    #     morePower = random.random() < 0.3
    #     if morePower:
    #         print '%s doubles his power' % self.name
    #         self.health = self.health * 2

class Goblin(Character):
    def __init__(self):
        self.name = 'goblin'
        self.health =41
        self.power = 33
        self.bounty = 5

class Wizard(Character):
    def __init__(self):
        self.name = 'wizard'
        self.health = 58
        self.power = 41
        self.bounty = 6

    def attack(self, enemy):
        swap_power = random.random() > 0.5
        if swap_power:
            print "%s swaps power with %s during attack" % (self.name, enemy.name)
            self.power, enemy.power = enemy.power, self.power
        super(Wizard, self).attack(enemy)
        if swap_power:
            self.power, enemy.power = enemy.power, self.power

class EvilMedic(Character):
    def __init__(self):
        self.name = 'EvilMedic'
        self.health = 50
        self.power = 22

    def attack(self, enemy):
        recuperate = random.random() < 0.5
        if recuperate:
            print '%s increases his health' % self.name
            self.health = self.health + 2


class Shadowy(Character):
    def __init__(self):
        self.name = 'shadow'
        self.health = 14
        self.power =14


class Zombie(Character):
    def __init__(self):
        self.name = 'zombie'
        self.health = 26
        self.power = 11

    def receive_damage(self, points):
        self.health -= points
        print "%s received %d damage." % (self.name, points)
        if self.health < 5:
            self.health += 10
            print "%s cannot die *insert evil laugh here*" % self.name

class Vampire(Character):
    def __init__(self):
        self.name = 'vampire'
        self.health = 29
        self.power = 18

class Battle(object):
    def do_battle(self, hero, enemy):
        print "====================="
        print "Hero faces the %s" % enemy.name
        print "====================="
        while hero.alive() and enemy.alive():
            hero.print_status()
            enemy.print_status()
            time.sleep(1.5)
            print "-----------------------"
            print "What do you want to do?"
            print "1. fight %s" % enemy.name
            print "2. do nothing"
            print "3. flee"
            print "> ",
            input = int(raw_input())
            if input == 1:
                hero.attack(enemy)
            elif input == 2:
                pass
            elif input == 3:
                print "Goodbye."
                exit(0)
            else:
                print "Invalid input %r" % input
                continue
            enemy.attack(hero)
        if hero.alive():
            print "You defeated the %s" % enemy.name
            return True
        else:
            print "YOU LOSE!"
            return False

class Evade(object):
    cost = 3
    name = 'evade'
    def apply(self, character):
        character.evade += 3
        print "%s's health is increased by %d." %(character.name, character.health)

class SuperTonic(object):
    cost = 6
    name = 'supertonic'
    def apply(self, character):
        character.health += 10

        print "%s's health is increased by %d." %(character.name, character.health)

class Armor(object):
    cost = 7
    name = 'armor'
    def apply(self, character):
        character.power +=2
        print "%s's power is increased to by %d." %(character.name, character.power)


class Tonic(object):
    cost = 5
    name = 'tonic'
    def apply(self, character):
        character.health += 2
        print "%s's health increased to %d." % (character.name, character.health)

class Sword(object):
    cost = 10
    name = 'sword'
    def apply(self, character):
        character.power += 2
        print "%s's power increased to %d." % (character.name, character.power)

class Spear(object):
    cost = 8
    name = 'spear'
    def apply(self, character):
        character.power += 3
        print "%s's power increased to %d." % (character.name, character.power)

class Nunchaku(object):
    cost = 12
    name = 'nunchaku'
    def apply(self, character):
        character.power += 9
        print "%s's power increased to %d." % (character.name, character.power)

class Store(object):
    # If you define a variable in the scope of a class:
    # This is a class variable and you can access it like
    # Store.items => [Tonic, Sword]
    items = [Tonic, Sword, Armor, SuperTonic, Spear, Evade, Nunchaku]
    def do_shopping(self, hero):
        while True:
            print "====================="
            print "Welcome to the store!"
            print "====================="
            print "You have %d coins." % hero.coins
            print "What do you want to do?"
            for i in xrange(len(Store.items)):
                item = Store.items[i]
                print "%d. buy %s (%d)" % (i + 1, item.name, item.cost)
            print "10. leave"
            input = int(raw_input("> "))
            if input == 10:
                break
            else:
                ItemToBuy = Store.items[input - 1]
                item = ItemToBuy()
                hero.buy(item)

hero = Hero()
enemies = [Goblin(), Wizard(), Shadowy(), Vampire(), EvilMedic(), Zombie()]
battle_engine = Battle()
shopping_engine = Store()

for enemy in enemies:
    hero_won = battle_engine.do_battle(hero, enemy)
    if not hero_won:
        print "YOU LOSE!"
        exit(0)
    shopping_engine.do_shopping(hero)

print "YOU WIN!"
