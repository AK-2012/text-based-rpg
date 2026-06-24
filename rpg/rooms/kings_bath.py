from .constants import *


def kings_bath(self):
    print(
        "You enter the bath chamber. Steam clings to the air. A large stone tub dominates the room, "
        "and a cracked mirror hangs above a small basin. The room is quiet and oddly peaceful.\n"
    )
    while True:
        do = (
            input(
                f"{Fore.BLUE}{Style.BRIGHT}You can take a bath or leave. What would you like to do? {Style.RESET_ALL}"
            )
            .strip()
            .lower()
        )
        if "bath" in do:
            if "clothes" not in self.items:
                print(
                    "You strip and sink into the warm water, heaving a sigh, and wash away the grime of the dungeon. "
                    "You feel a bit more energized.\n"
                )
                self.bathe()
                self.items.append("clothes")
                print(
                    f"{Fore.GREEN}{Style.BRIGHT}You have {self.hearts} hearts now. As you put a set of clean tunic and pants stolen from the king's wardrobe on,"
                    " you notice a tile in the wall next to the mirror is loose. "
                )
                break
            else:
                print(
                    "You already took a bath! You shake your head at your forgetfulness. "
                    "You remember the loose tile in the wall next to the mirror. "
                )
                break
        elif do == "leave":
            print(
                "You leave the bath chamber and return to the main room of the king's quarters."
            )
            return "kings_quarters"
        else:
            print("Nothing happens.\n")
    print(
        "You have a feeling you can pry off the tile. There may be something hidden behind it. "
    )
    pry = (
        input(f"{Fore.BLUE}{Style.BRIGHT}Do you pry off the tile? {Style.RESET_ALL}")
        .strip()
        .lower()
    )
    while pry not in ["y", "yes", "n", "no"]:
        pry = (
            input(
                f"{Fore.BLUE}{Style.BRIGHT}Do you pry off the tile? {Style.RESET_ALL}"
            )
            .strip()
            .lower()
        )
    if pry in ["y", "yes"]:
        print(
            "You pry up the loose tile, revealing a narrow, hidden passage leading down, and enter."
        )
        return "nymph_passage"
    print(
        "Like the weak, unadventurous coward you are, you don't pry off the tile. Instead, you"
        " head back to the King's quarters. Little sissy."
    )
    return "kings_quarters"
