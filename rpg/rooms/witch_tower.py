from .constants import *


def witch_tower(self):
    print(
        "\nYou step out into a circular tower room. The walls seem to shift and twist "
        "whenever you look at them for too long, making your head spin. In the center of the room "
        "stands a woman in tattered robes, her empty eye sockets covered with a strip of cloth.\n"
    )
    if "eye" in self.items:
        # have eye already
        print(
            "The witch tilts her head as if she can still see you. "
            '"You have what you came for," she murmurs. "My bargain with fate is already sealed." '
            "You feel an uncomfortable pressure in your skull and decide not to linger here.\n"
        )
        while True:
            go = (
                input(
                    f"{Fore.BLUE}{Style.BRIGHT}The portal is behind you. Off to the side is the weapons chamber,"
                    f" and to the other side is the dragonhold. Where would you like to go? {Style.RESET_ALL}"
                )
                .strip()
                .lower()
            )
            if "portal" in go:
                return "room_o_doom"
            elif "weapons" in go:
                return "weapons_chamber"
            elif "dragon" in go:
                return "dragonhold"
            else:
                print("Nothing happens.")
    print( # no eye...yet
        "The woman turns her head toward you, though her covered eyes could not possibly see. "
        '"So, another plaything of the king slips through his fingers," she says, voice dry and amused. '
        '"He keeps me here, chained by oaths and my own magic, but even blind I see more than he." '
        "She lets out a laugh, making you shiver. "
    )
    # if the player got the elf staff. :) just something for some ✨FLAIR✨
    if "staff" in self.items:
        print('Her head tilts slightly. "An elf\'s touch lingers on you. Odd."')
    if "sold_staff" in self.flags:
        print("She clicks her tongue. \"I smell greed, yet an elf's blessing lies on you.\"")
    # Main choice loop
    while True:
        print(
            "\nShe raises a hand toward you, fingers trembling with restrained power.\n"
            "\"You want justice, don’t you? The king’s blood on the floor, his crown in the people's hands. "
            'All he fears, I can give you, in one of my eyes. It will cost you… but less than it cost me."'
        )
        choice = (
            input(
                f"{Fore.BLUE}{Style.BRIGHT}\nDo you take one of the witch's eyes? {Style.RESET_ALL}"
            )
            .strip()
            .lower()
        )
        while choice not in ["y", "yes", "n", "no"]:
            choice = (
                input(
                    f"{Fore.BLUE}{Style.BRIGHT}Do you take one of the witch's eyes? {Style.RESET_ALL}"
                )
                .strip()
                .lower()
            )
        # haha player loses if they don't have it but they don't know that yet
        if choice in ["n", "no"]:
            print(
                "\nYou step back. It feels like the witch is looking at you somewhat condescendingly. "
                '"Go," she says. "Challenge him with your puny strength alone."\n'
            )
            break
        # the player isn't a WEAK COWARD
        else:
            print(
                "\nYou step closer. Her hand cups your face, cold and burning at the same time.\n"
                "A scream rips through you; yours or hers, you cannot tell. You stagger but remain standing.\n"
            )
            print(
                "Your perception twists. You feel presences in the castle, threads of fear and obedience. You "
                "feel, with a terrible certainty, the ease of ending a life with a flick of your hand."
            )
            self.items.append("eye")
            print(f"{Fore.YELLOW}{Style.BRIGHT}\nWitch's eye added to inventory.\n")
            print(
                'The witch laughs sinisterly. "Go, then. Show him what he has made of me."'
            )
            break
    while True:
        go = (
            input(
                f"{Fore.BLUE}{Style.BRIGHT}The portal is behind you. Off to the side is the weapons chamber,"
                f" and to the other side is the dragonhold. Where would you like to go? {Style.RESET_ALL}"
            )
            .strip()
            .lower()
        )
        if "portal" in go:
            return "room_o_doom"
        elif "weapons" in go:
            return "weapons_chamber"
        elif "dragon" in go:
            return "dragonhold"
        else:
            print("Nothing happens.")
