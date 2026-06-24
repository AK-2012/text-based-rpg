from .constants import *


def colosseum(self):
    print("\nYou are in the colosseum. A guard notices you. \n")
    while True:
        do = (
            input(f"{Fore.BLUE}{Style.BRIGHT}Do you fight or run? {Style.RESET_ALL}")
            .strip()
            .lower()
        )
        if do == "fight":
            if "sword" in self.items:
                d = random.randint(1, 3)
                print(
                    f"\nYou deal {self.attack} damage to the guard. He deals {d} damage to you. The guard passes out.\n"
                )
                self.hearts -= d
                if self.dead_check():
                    return "dead"
                print(
                    f"{Fore.GREEN}{Style.BRIGHT}You have {self.hearts} hearts left. \n"
                )
                break
            else:
                print(
                    "\nThere is no weapon to fight the guard with. You pitifully attempt to fistfight the armored guard, but he stabs you through the stomach. \n"
                )
                return "dead"
        elif do == "run":
            print(
                "\nYou try to run away. The guard follows, and your weakened state makes him catch up. You "
                "feel a sudden pressure in your stomach, then a burning pain as your body realizes it has been stabbed.\n"
            )
            return "dead"
        else:
            print("Nothing happens.")
    if "key" not in self.items:
        print(
            "\nYou notice something shiny in the guard's pocket. As you bend down to examine it, you notice it is a key."
        )
    print(
        "\nAs you examine your surroundings, you see five different paths. "
        "One leads back to the dungeon you came from. Another has a rancid stench emanating from it, like one of beasts. "
        "You don't want to enter it to find out, but it seems to be a beast room. Next to the beast room is an identical pathway as your dungeon. "
        "You assume it's the other dungeon you heard about from guard gossip. Turning more, there is the sound of people from the next pathway. "
        'You assume that is the spectator entrance to the colosseum. Yet another path is adorned luxuriously with decor and has a sign on it: "King\'s Entrance". \n'
    )
    print(
        "Places you can go: the Dungeon, the other dungeon, the beast room, the spectator entrance, and the King's entrance."
    )
    while True:
        go = (
            input(
                f"\n{Fore.BLUE}{Style.BRIGHT}What would you like to do? {Style.RESET_ALL}"
            )
            .strip()
            .lower()
        )
        if "take" in go and "key" in go and "key" not in self.items:
            print(f"{Fore.YELLOW}{Style.BRIGHT}Key added to inventory.\n")
            self.items.append("key")
        elif "dungeon" in go and "other" not in go:
            print("You head back to your dungeon. \n")
            return "dungeon"
        elif "other dungeon" in go:
            print("You go to the pathway you assume leads to the other dungeon.\n")
            return "other_dungeon"
        elif "beast" in go and "room" in go:
            print(
                "As you head towards the beast room, your mind becomes fuzzy."
                " The rancid stench becomes heavier in your nostrils, and you start losing your senses. You pass out.\n"
            )
            return "dead"
        elif "spectator" in go and "entrance" in go:
            print("You head towards the sound of people in the spectator entrance.\n")
            return "spectator_entrance"
        elif "king" in go and "entrance" in go:
            print("You head towards the beautifully adorned King's entrance.\n")
            return "kings_entrance"
        else:
            print("Nothing happens.")
