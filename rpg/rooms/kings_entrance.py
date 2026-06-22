from .constants import *


def kings_entrance(self):
     # die if 4 or less hearts
     print("\nWalking up to the King's entrance, you see a few guards strolling about. One of them notices you"
          " and alerts the other two. They run towards you, and you're forced to fight. You lose 3 hearts in "
          "the process.\n")
     self.hearts -= 3
     if self.dead_check():
          return "dead"
     print(f"{Fore.GREEN}{Style.BRIGHT}You have {self.hearts} hearts left. ")
     print("\nNow that the guards have been eliminated, you notice a stairwell in the back of the room."
          " It doesn't look like it's supposed to stand out, but it does anyways, contrasting the "
          "colourful furniture with its drab surface. You assume that's the way to the upper floor "
          "and follow it. ")
     return "stairs"
