from .constants import *


def dragonhold(self):
    print(
        "\nYou step into a vast, dim chamber that smells of smoke and old stone, older than the new castle. "
        "Chains as thick as tree trunks stretch from the walls and ceiling to a huge shape curled in the dim light. "
        "You gasp as your eyes behold the majestic creature in the midst of them all. "
        "Its iridescent scales shift like living oil, rainbow hues of white, gold, maroon, and amethyst flashing with every angle. "
        "A single black eye cracks open, the depths of them unseen, but lighted by the white in the dragon's pupils. "
    )

    # player doesn't have the key to the locks
    if "dragonhold key" not in self.items:
        print(
            "You notice an enormous lock built into the main set of shackles, its surface "
            "covered in strange runes. Something in you whispers that you are missing the key"
            " to this prison. The dragon watches you for a moment, then closes its eye again, indifferent."
        )
        print(
            "There is nothing else you can do here. You return to the witch's tower. "
        )
        return "witch_tower"
    # player has key to the locks
    else:
        print(
            "As you step closer, the dragon’s eye widens, focusing fully on you. You are reminded"
            " of the dragonhold key you got in the King's secret chamber tunnel. There is an enormous"
            " lock built into the main set of shackles, its surface covered in strange runes. In the "
            "center is a disproportionately small keyhole, but it matches your key perfectly. "
        )
        print(
            "Your attention goes back to the dragon. Seeing you take out the key, its eye shows"
            " desperation and pleading. A powerful voice, not your own, whispers in the back of your "
            'mind, "Save me. Let the king die at our hands."'
        )
        while True:
            free = (
                input(
                    f"{Fore.BLUE}{Style.BRIGHT}Do you free the dragon? {Style.RESET_ALL}"
                )
                .strip()
                .lower()
            )
            while free not in ["y", "yes", "n", "no"]:
                free = (
                    input(
                        f"{Fore.BLUE}{Style.BRIGHT}Do you free the dragon? {Style.RESET_ALL}"
                    )
                    .strip()
                    .lower()
                )
            if free in ["y", "yes"]:
                print(
                    "You walk closer, in front of the keyhole, and take a breath. Inserting the key, you free"
                    " the dragon. "
                )
                return "win_dragon"
            else:
                print(
                    "You put the key back in your pocket. A rumble starts in the floor, and you realize the"
                    " dragon is causing it. Fearful, you try to stumble back towards the witch tower, but a "
                    "blast of heat smothers you before you make it all the way there. You scream in agony as"
                    " you are burned alive. In your last moments, you remember what your mother told you about"
                    ' dragons when you were a wee babe: "Never anger a dragon, for their wrath burns hotter than'
                    ' any forge and spares none who defy them."'
                )
                return "dead"
