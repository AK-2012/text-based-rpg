from .constants import *


def stairs(self):
    print(
        "\nYou are at the top of a stairwell. This area is much easier to navigate than the previous;"
        " signs mark where different places are. Behind you are the stairs whence you emerged. "
        "At the bottom is the King's entrance to the colosseum. You look around and read the signs."
        " In one direction, a path leads to the King's hall, "
        "guard quarters, and King's quarters. In the other direction, there is only one thing on the"
        " sign, but it has been scribbled out and replaced in a bright, unnatural purple: 'Room o' "
        "Doom'. For some reason it doesn't give off those kinds of vibes.\n"
    )
    while True:
        go = (
            input(
                f"{Fore.BLUE}{Style.BRIGHT}Where would you like to go? {Style.RESET_ALL}"
            )
            .strip()
            .lower()
        )
        if "doom" in go and "room" in go:
            return "room_o_doom"
        elif "king" in go and "quarter" in go:
            return "kings_quarters"
        elif "king" in go and "hall" in go:
            return "kings_hall"
        elif ("king" in go and "entrance" in go) or "stairs" in go or "colosseum" in go:
            return "kings_entrance"
        elif "guard" in go and "quarter" in go:
            return "guard_quarters"
        else:
            print("Nothing happens. ")
