class Character:
    def __init__(self, hearts=10, items=None, attack=2):
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
        if self.hearts <= 0:
            return True
        return False

    def damage_check(self):
        # check for different items and change player's damage accordingly
        base = 2
        if "sword" in self.items:
            base += 2
        if any(w in self.items for w in ["longsword", "dagger", "rapier"]):
            base += 3
        self.attack = base
