from .constants import *


def exit(self):
    print(
        "\nYou are on one side of the room. On the others, there is a door and a slate with some "
        "writing on it. You walk over to read it. \n"
    )
    print(
        "It says:\nthyseznuffinempyrtint. thadevwsborrd. \nYou wonder what it means and try to sound it out.\n"
    )
    sleep(2)
    while True:
        go = (
            input(
                f"{Fore.BLUE}{Style.BRIGHT}\nWould you like to head through the door now? {Style.RESET_ALL}"
            )
            .strip()
            .lower()
        )
        while go not in ["y", "yes", "n", "no"]:
            go = (
                input(
                    f"{Fore.BLUE}{Style.BRIGHT}Would you like to head through the door now? {Style.RESET_ALL}"
                )
                .strip()
                .lower()
            )
        if go in ["y", "yes"]:
            return "win_witch"
        print("\nYou stay in the room for a little while longer.\n")
        sleep(3)
