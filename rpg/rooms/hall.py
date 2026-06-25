from .constants import *


def hall(self):
    print(
        "You enter the hall. It is lit with torches, but shadows still creep in the corners. It is colder here."
    )
    print(
        "After walking for a little bit, you encounter a griffin. Remembering that they are nonviolent creatures"
        " who survive to serve a purpose, you do not attack. "
    )
    # king not dead yet
    if "killed_king" not in self.flags:
        print(
            'The griffin speaks. "I guard this passage beyond the Room o\' Doom. Only those who prove worthy may pass."'
        )
        # elf's blessing/touch/staff
        if "staff" in self.items:
            print(
                'The griffin eyes you. "An elf\'s touch and blessing... very well, prove your worth with a number."'
            )
            print(
                "The griffin is thinking of a number between 1 and 10. Guess correctly to pass."
            )
            secret_number = random.randint(1, 10)
            while True:
                try:
                    guess = int(
                        input(
                            f"{Fore.BLUE}{Style.BRIGHT}What is your guess? {Style.RESET_ALL}"
                        ).strip()
                    )
                    if guess < 1 or guess > 10:
                        raise ValueError
                    if guess == secret_number:
                        print(
                            'Correct! The griffin bows its head. "You may pass to the Four Seasons Room."'
                        )
                        return "four_seasons_room"
                    else:
                        print("Wrong! The griffin shrieks.")
                except ValueError:
                    print("Enter a valid number between 1 and 10.")
        # No staff
        else:
            print(
                'The griffin blocks your path. "You lack power and wisdom. You are unworthy. Turn back."'
            )
        # player is a failure
        while True:
            go = (
                input(
                    f"{Fore.BLUE}{Style.BRIGHT}\nDo you turn back or try to pass anyway? {Style.RESET_ALL}"
                )
                .strip()
                .lower()
            )
            if "back" in go:
                print("You wisely turn back toward the Room o' Doom.")
                return "room_o_doom"
            elif "pass" in go:
                print("The griffin deems you unworthy and strikes you down instantly.")
                return "dead"
            else:
                print("The griffin awaits your decision.")
    # king do be dead
    else:
        print(
            'The griffin speaks. "I guard this path to the outside, and you have proven worthy. Pass."'
        )
        return "four_seasons_room"
