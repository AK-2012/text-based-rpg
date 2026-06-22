from .constants import *


def dungeon(self):
    print("\nYou return to the dungeon you were imprisoned in. The place gives you shivers.")
    if "hand" not in self.items:
        print("Your inmate's bloody hand lies on the ground. You grimace at their lifeless body.")
    while True:
        do = input(f"{Fore.BLUE}{Style.BRIGHT}What would you like to do? {Style.RESET_ALL}").strip().lower()
        if "take" in do and "hand" in do and "hand" not in self.items:
            print(f"{Fore.YELLOW}{Style.BRIGHT}Bloody hand added to inventory.")
            self.items.append("hand")
        elif do == "leave":
            print("You head out of the dungeon into the colosseum.")
            return "colosseum"
        else:
            print("Nothing happens. ")
