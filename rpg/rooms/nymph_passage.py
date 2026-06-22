from .constants import *


def nymph_passage(self):
      if "dragonhold key" not in self.items:
            print("\nYou squeeze into the hidden passage. The air grows cooler and damp as you descend. "
                  "The stone walls close in as you move toward a faint glow ahead.\n")
            print("Eventually, you emerge into a small cell. A beautiful shackled nymph hangs from glowing chains "
                  "bolted into the wall, her eyes full of ancient sorrow.")
            while True:
                  do = input(f"{Fore.BLUE}{Style.BRIGHT}\nYou can talk to the nymph or attempt to free her. What would you like to do? {Style.RESET_ALL}").strip().lower()
                  if "talk" in do:
                        print("\"I have been here for longer than I can remember,\" she whispers. "
                              "\"If you can break these chains, I will help you escape this place.\"")
                  elif "free" in do:
                        if "hand" in self.items:
                              print("You press the bloody elf hand against the glowing chains. The runes flicker and die, "
                                    "and the shackles snap open. The nymph steps free.")
                              print("\"Thank you,\" she says softly. \"I cannot stay, but I can open a way.\" "
                                    "She places her hand on the far wall. A hidden doorway grinds open.")
                              print("\"Beyond this path lies a great danger, but also a key to your freedom. "
                                    "May fortune favor you.\" With that, she vanishes in a swirl of light.")
                              return "troll_room"
                        else:
                              print("You tug at the chains, but they will not break. The nymph shakes her head.\n"
                                    "\"These bindings were forged with blood. Only a piece of the dead can open them. "
                                    "You do not have what you need.\"\n")
                              print("You nod sorrowfully, knowing you cannot free her. You head back through the hidden"
                                    " passage into the bathing chambers, then back further into the King's quarters.")
                              return "kings_quarters"
                  else:
                        print("Nothing happens.\n")
      else:
            print("Your work here is done. You head back to the bathing chamber, then the King's quarters.")
            return "kings_quarters"
