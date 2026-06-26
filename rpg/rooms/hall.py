from .constants import *


def hall(self):
    print(
        "You enter the hall. It is lit with torches, but shadows still creep in the corners. It is colder here."
        " Spiders scuttle in the walls, webs brushing against you. Dust clings to the floor, and a musty smell fills the air."
        " You can hear the occasional drip of water from the ceiling. "
    )
    print(
        "After walking for a little bit, you encounter a griffin. Remembering they are non-violent creatures"
        " who survive to serve a purpose, you do not attack. "
    )
    # king not dead yet
    if "killed_king" not in self.flags:
        print(
            'The griffin speaks. "I guard this passage to the outside. Only those who prove worthy may pass."'
        )
        if "sold_staff" in self.flags: # elf's touch but sold staff
            print(
                'The griffin eyes you. "An elf\'s blessing... very well, prove your worth."'
            )
            print(
                "The griffin is thinking of a number between 1 and 10. Guess correctly to pass."
            )
            secret_number = random.randint(1, 10) # guess the number
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
                        print("Wrong! The griffin shrieks. \"You shall not pass! Turn back and gain "
                        "power and wisdom. \" You turn back toward the Room O' Doom fearfully.")
                        return "room_o_doom"
                except ValueError:
                    print("Enter a valid number between 1 and 10.")
        elif "staff" in self.items: # has elf staff, hasn't sold
            print(
                "The griffin seems torn. \"An elf\'s staff and blessing, but a duty "
                "to fulfill...\" Suddenly, it looks up with conviction. "
                "\"You are destined for greater things than this. Turn back."
                " Kill our malevolent king sitting upon his thorny throne. \""
            )
        # No staff
        else:
            print(
                'The griffin blocks your path. "You lack power and wisdom. You are unworthy. Turn back."'
            )
        while True: # they better not defy the griffin
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
    else: # king dead
        print(
            'The griffin speaks. "I guard this path to the outside, and you have proven worthy. You may pass."'
        )
        return "four_seasons_room"
