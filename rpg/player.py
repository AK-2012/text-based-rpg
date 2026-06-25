from rooms.constants import *


class Character:
    def __init__(self, hearts=10, items=None, attack=1):
        self.hearts = hearts
        self.attack = attack
        self.items = [] if items is None else items
        self.flags = set()
        self.room = "start"

    def eat(self):
        # for saving the man's daughter in the slums
        self.hearts = 13

    def bathe(self):
        # for bath in king's quarters
        self.hearts += 2

    def dead_check(self):
        return self.hearts <= 0

    def damage_check(self):
        # check for different items and change player's damage accordingly
        if "sword" in self.items:
            self.attack += 2
        if any(w in self.items for w in ["longsword", "dagger", "rapier"]):
            self.attack += 3

    def fight(self, enemy="ghost", enemy_damage=1, enemy_hearts=2):
        while enemy_hearts > 0: # while enemy not dead
            input("Press anything to attack. ")
            enemy_hearts -= self.attack
            print(f"You deal {self.attack} damage to the {enemy}. ")
            print(f"{enemy.capitalize()} hearts: {max(0, enemy_hearts)}\n")
            if enemy_hearts <= 0: # enemy is dead
                print(f"The {enemy} is dead.")
                return
            self.hearts -= enemy_damage
            print(f"The {enemy} deals {enemy_damage} damage to you. {Fore.GREEN}{Style.BRIGHT}You have {max(0, self.hearts)} hearts left. {Style.RESET_ALL}\n")
            if self.dead_check(): # player dead
                return "dead"
