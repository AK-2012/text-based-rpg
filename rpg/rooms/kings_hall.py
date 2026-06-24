from .constants import *


def kings_hall(self):
    print("A large set of ornate wooden doors lay before you.")
    # player hasn't killed king.
    if "crown" not in self.items:
        if "eye" not in self.items:
            print("You feel like you shouldn't go in.")
        while True:
            enter = input(f"{Fore.BLUE}{Style.BRIGHT}Do you enter? {Style.RESET_ALL}")
            while enter not in ["y", "yes", "n", "no"]:
                enter = input(
                    f"{Fore.BLUE}{Style.BRIGHT}Do you enter? {Style.RESET_ALL}"
                )
            if enter in ["y", "yes"]:
                break
            # leave king's hall for whatever reason
            elif enter in ["n", "no"]:
                while True:
                    go = input(
                        f"{Fore.BLUE}{Style.BRIGHT}The guard quarters, King's quarters, and stairs are "
                        f"behind you. Where would you like to go? {Style.RESET_ALL}"
                    )
                    if "stair" in go:
                        return "stairs"
                    elif "guard" in go and "quarter" in go:
                        return "guard_quarters"
                    elif "king" in go and "quarter" in go:
                        return "kings_quarters"
                    else:
                        print("Nothing happens.")
        # enter king's hall
        print(
            "You enter the hall. The King smirks at the sight of you, an"
            " ugly smirk. He has no idea of the power you have possessed "
            "from the witch. The King speaks, a honeyed voice unfit for his deeds. "
        )
        print(
            '"So you have escaped your cell, huh? No matter. This is '
            'where you will meet your end, false leader. Guards!"\n'
        )
        # player has witch's eye, kills king
        if "eye" in self.items:
            print(
                "The guards advance upon you, but you raise your hand and they all freeze "
                "involuntarily. The King, to your satisfaction, looks shocked. He seems to"
                " want to say something, but your magic shuts his mouth.\n "
            )
            if "staff" in self.items:
                print(
                    'You speak. "You may have control over an army. You may have a dragon'
                    " chained in your stronghold. You might believe you are unstoppable "
                    "and powerful for these reasons. However, what of the world outside"
                    " this stronghold, outside the underground city? There are still nobles,"
                    " and children, and magical creatures, and beings superior to us. Yet"
                    " you pay them no heed. All that matters to you is your castle and throne, "
                    "so you eradicate all outside of it. A wise elf, in your castle alone, once"
                    " told me it is unfair to let the actions of one man dictate the fate of "
                    "others. I believe it is even more unfair when this one man has not faced "
                    "anything. You have never led your army into battle. You make others do your"
                    " dirty work. Even all you have at your hands, all the wealth, riches, strength,"
                    " loyalty-- None of it was earned by you. We may have accepted you because of "
                    "your predecessor, but it will be no more. Meet the same fate as the ones "
                    'suffering under your hand."'
                )
            else:
                print(
                    'You speak. "You may have control over an army. You may have wealth'
                    " and riches available at a moment's notice. You might believe you are unstoppable "
                    "and powerful for these reasons. However, what of the world outside"
                    " this stronghold, outside the underground city? There are still nobles,"
                    " and children, and magical creatures, and beings superior to us. Yet"
                    " you pay them no heed. All that matters to you is your castle and throne, "
                    "so you eradicate all outside of it. You are weak and a coward."
                    " You have never led your army into battle. You make others do your"
                    " dirty work. Even all you have at your hands, all the wealth, riches, strength,"
                    " loyalty-- None of it was earned by you. We may have accepted you because of "
                    "your predecessor, but it will be no more. Meet the same fate as the ones "
                    'suffering under your hand."'
                )
            print(
                "\nYou flick your hand. Nothing happens at first, but then the king starts"
                "convulsing violently. You clench your fist, and he curls up into a ball. "
                "His insides crush and he starts vomiting up blood. A last flick of your hand"
                " makes the king shriek, and then he is moving no more. You take his crown and "
                "leave the room with the guards still frozen.\n"
            )
            print(f"{Fore.YELLOW}{Style.BRIGHT}\nKing's crown added to inventory.\n")
            self.items.append("crown")
            return "stairs"
        # player doesn't have witch's eye, dies
        else:
            print(
                "The guards advance upon you. You try to fight back, but their sheer numbers"
                " overwhelm you. There was nothing you could do to save yourself."
            )
            return "dead"
    # player killed king
    else:
        print("Your work here is done. You head back to the stairs. ")
        return "stairs"
