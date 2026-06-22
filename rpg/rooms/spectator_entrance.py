from .constants import *


def spectator_entrance(self):
    # AKA underground city
    print("You are in the spectator entrance to the colosseum. Across from you are the three main sections of the underground city: the "
            "slums, the market, and the exclusive networks for the rich (the rich neighborhood). Behind you is the colosseum. ")
    while True:
        go = input(f"{Fore.BLUE}{Style.BRIGHT}Where would you like to go? {Style.RESET_ALL}").lower().strip()
        if "colosseum" in go:
            return "colosseum"
        elif "slums" in go:
            return "slums"
        elif "market" in go:
            return "market"
        elif "rich" in go:
            return "rich"
        else:
            print("Nothing happens. ")
            continue
