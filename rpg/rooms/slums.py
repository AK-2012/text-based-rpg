from .constants import *


def slums(self):
    self.hearts -= 1
    print(
        "\nYou head to the filthy slums. A rock hits you, thrown by some child-beggar scorning you, and you lose a heart."
    )
    if self.dead_check():
        return "dead"
    print(f"{Fore.GREEN}{Style.BRIGHT}You have {self.hearts} hearts left. ")
    if "has_daughter_quest" in self.flags and "rescued_daughter" not in self.flags:
        print(
            "\nYou see some suspicious-looking people a few walks away. They glare at you. You pull out the flyer, and"
            ' they advance upon you. "Do you have any business with us?" A burly man asks. You tell them you\'re searching'
            ' for the girl in the flyer. The men look down at you, scowling. "And why are you looking for her?"'
            " You tell them her father asked you to. Behind them, you see something you didn't notice earlier: a girl, "
            "matching the description and photo on the flyer perfectly, looking up at you with wide, teary eyes. "
        )
        while True:
            do = (
                input(
                    f"{Fore.BLUE}{Style.BRIGHT}Do you fight or run? {Style.RESET_ALL}"
                )
                .strip()
                .lower()
            )
            if do == "run":
                print(
                    "You head out of the slums back to the market, running from the burly men. "
                )
                return "market"
            elif do == "fight":
                print(
                    "\nYou beat up the men. For all their weight and bulk, their fighting skills are"
                    " inferior to yours. You take the girl, soothing her with words that she'll see her "
                    "father, and head back to the market. She clutches your hand on the way, eyeing "
                    "the people around you warily. "
                )
                self.flags.add("has_daughter")
                return "market"
            else:
                print("Nothing happens. ")
    while True:
        go = (
            input(
                f"{Fore.BLUE}{Style.BRIGHT}Where would you like to go? {Style.RESET_ALL}"
            )
            .strip()
            .lower()
        )
        if ("spectator" in go and "entrance" in go) or "colosseum" in go:
            return "spectator_entrance"
        elif "market" in go:
            return "market"
        elif "rich" in go:
            return "rich neighborhood"
        else:
            print("Nothing happens.")
