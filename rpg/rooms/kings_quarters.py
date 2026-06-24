from .constants import *


def kings_quarters(self):
    # Player has just chosen to go to the king's quarters from the middle floor
    print(
        "\nYou step into the King's quarters. The room is lavish: a massive bed, "
        "heavy velvet curtains, golden trim, and a marble floor. In the corner is"
        " a door presumably leading to the bathing chamber. Yet the air feels cold and wrong.\n"
    )

    while True:
        do = (
            input(
                f"{Fore.BLUE}{Style.BRIGHT}Behind you is the hallway to the stairs. In front is the room and"
                f" bathing chamber. Where would you like to go? {Style.RESET_ALL}"
            )
            .strip()
            .lower()
        )
        if "bath" in do or "chamber" in do:
            return "kings_bath"
        elif "hall" in do or "stairs" in do:
            print("You leave the King's quarters and return to the stairs.")
            return "stairs"
        else:
            print("Nothing happens.")
