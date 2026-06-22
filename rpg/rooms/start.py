from .constants import *


def start(self):
    # beginning of game.
    print("You are in a dungeon. You remember you are a ruler of your people raising an uprising against the malevolent king. "
            "However, seeing as where you are now, you assume you have been captured. You hope your people are okay. "
            "There is an inmate across from you. He appears to be dead, but is an elf. You yourself are unshackled and can move freely. "
            "Your inmate's hand is on the floor, free for the taking. He seems to have died of blood loss after torture, a gruesome death. "
            "There is one door leading out of the dungeon.\n")
    # stats
    print(f"{Fore.GREEN}{Style.BRIGHT}Current stats: {self.hearts} hearts, {self.attack} attack damage. You have no items.\n")
    while True:
        do = input(f"{Fore.BLUE}{Style.BRIGHT}What would you like to do? (leave) (take ____) {Style.RESET_ALL}").strip().lower()
        if "take" in do and "hand" in do and "hand" not in self.items:
            print(f"{Fore.YELLOW}{Style.BRIGHT}Bloody hand added to inventory.\n")
            self.items.append("hand")
        elif do == "leave":
            print("\nYou head towards the dungeon entrance. A guard is standing with his back to you. You twist his neck, killing him. He has a sword.\n")
            while True:
                do = input(f"{Fore.BLUE}{Style.BRIGHT}What would you like to do? {Style.RESET_ALL}").strip().lower()
                if "take" in do and "sword" in do and "sword" not in self.items:
                    self.items.append("sword")
                    self.damage_check()
                    print(f"{Fore.YELLOW}{Style.BRIGHT}Sword added to inventory. You can deal {self.attack} attack damage. \n")
                elif do == "leave":
                    print("\nYou head out of the dungeon into a colosseum. \n")
                    return "colosseum"
                else:
                    print("Nothing happens.")
        else:
            print("Nothing happens.")
