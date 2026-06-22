from .constants import *


def troll_room(self):
    print("You follow the newly opened passage. The air grows thick with the smell of sweat and old blood. "
          "You step into a cavernous chamber where a hulking troll stands guard before a heavy stone door.\n")
    print("The troll turns toward you, baring jagged teeth, and hefts a massive club.\n")
    # player doesn't have enough hearts
    if self.hearts < 5:
        print("You feel a spike of terror as the troll charges. You are too weak to stand "
              "a chance. The club crashes down, and everything goes dark.\n")
        return "dead"
    print("You ground yourself and charge. Steel clashes against flesh as you battle the troll.\n")
    # simple battle: trade a random amount of damage, but you always eventually win if you qualify
    for _ in range(2):
          dmg = random.randint(1, 2)
          self.hearts -= dmg
          print(f"The troll lands a crushing blow, dealing {dmg} damage. ")
          input(f"{Fore.BLUE}{Style.BRIGHT}Press something to attack. {Style.RESET_ALL}")
          dmg = random.randint(1, self.attack)
          print(f"You deal {dmg} damage. ")
    print("The troll is dead. ")
    print(f"{Fore.GREEN}{Style.BRIGHT}You stagger, breathing hard. You have {self.hearts} hearts left.")
    print("Behind you, the passage collapses with a deafening rumble. There is no way back, "
          "only the stone door ahead.\n")
    return "riddle_door"
