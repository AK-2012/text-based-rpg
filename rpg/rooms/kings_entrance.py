from .constants import *


def kings_entrance(self):
    if "killed_guards" not in self.flags:
        # die if 3 or less hearts
        print(
            "\nWalking up to the King's entrance, you see a few guards strolling about. One of them notices you"
            " and alerts the other two. They run towards you, and you're forced to fight. "
        )
        self.fight("guards", 1, random.randint(7,12))
        self.flags.add("killed_guards")
        print(
            "\nNow that the guards have been eliminated, you notice a stairwell in the back of the room."
            " It doesn't look like it's supposed to stand out, but it does anyways, contrasting the "
            "colourful furniture with its drab surface. You assume that's the way to the upper floor "
            "and follow it. "
        )
        return "stairs"
    print("You're back in the colorfully decorated King's entrance to the colosseum. Behind you are the stairs.")
    while True:
        go = (
            input(
                f"{Fore.BLUE}{Style.BRIGHT}Where would you like to go? {Style.RESET_ALL}"
            )
            .strip()
            .lower()
        )
        if "stairs" in go or "stairwell" in go:
            return "stairs"
        elif "colosseum" in go:
            return "colosseum"
        else:
            print("Nothing happens. ")
