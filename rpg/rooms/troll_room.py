from .constants import *


def troll_room(self):
    if "killed_troll" not in self.flags:
        print(
            "You follow the newly opened passage. The air grows thick with the smell of sweat and old blood. "
            "You step into a cavernous chamber where a hulking troll stands guard before a heavy stone door.\n"
        )
        print(
            "The troll turns toward you, baring jagged teeth, and hefts a massive club.\n"
        )
        print(
            "You ground yourself and charge. Steel clashes against flesh as you battle the troll.\n"
        )
        self.fight("troll", random.randint(1, 3), 8)
        self.flags.add("killed_troll")
        print(
            f"{Fore.GREEN}{Style.BRIGHT}You stagger, breathing hard. You have {self.hearts} hearts left."
        )
        print(
            "Behind you, a portcullis falls with a deafening rumble of old stone. "
            "There is no way back, only the stone door ahead.\n"
        )
        return "riddle_door"
    # killed troll, heading back
    print("You return to the room where you fought the troll. The portcullis has opened now. "
    "You pass through and return to the passage where you met the nymph, the portcullis falling"
    " for the final time as you leave this ancient chamber. \n")
    return "nymph_passage"