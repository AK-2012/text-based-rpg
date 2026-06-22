from .constants import *


def other_dungeon(self):
    print("When you enter the other dungeon, you notice a door with a lock on it. Although the paths are identical, this dungeon has a closed door. ")
    if "key" in self.items:
        print("The door seems like it can be unlocked by the guard's key you took earlier. ")
    while True:
        do = input(f"{Fore.BLUE}{Style.BRIGHT}What would you like to do? {Style.RESET_ALL}").strip().lower()
        # this is where the player w/o a key will leave
        if do == "leave":
            print("You head out of the other dungeon into the colosseum. ")
            return "colosseum"
        # if they have key
        elif ("door" in do or "open" in do or "unlock" in do) and "key" in self.items:
            break
        # invalid inputs obvi
        else:
            print("Nothing happens. ")
    # this only runs if the player has the guard's key and no staff
    if "staff" not in self.items:
        print("\nThere are two prisoners, an elf and an old man. The old man opens his eyes at your"
                " approach and eyes you up and down. The elf is unshackled, except for a chain binding "
                "him to the wall. The man has all his limbs chained. When the elf notices you, he smiles"
                " radiantly even under the grime all over him. \"Hello,\" he says. \"What is your business"
                " with us?\" he asks. \n")
        print("You tell him you were another prisoner, but escaped and came here to see what was here. "
                "You ask him if you can free him, and his eyes become melancholy. \"I could free myself "
                "if I desired, but I remain here to keep this man company. The king... the cruel king, "
                "he lost the key to this man's bindings, else he could have been released. This man has "
                "been here for longer than the king himself, serving his sentence when the king rose to "
                "power. It was initially only a year, for petty theft, and now he has been here for "
                "as long as anybody can remember. It is unfair to let the actions of one man dictate"
                " the fate of others.\" The elf rises and produces something from somewhere in the shadows."
                " \"I refuse to leave, but my spirit is with you. Take my staff. It may help you so.\"\n")
        self.items.append("staff")
        print(f"{Fore.YELLOW}{Style.BRIGHT}Elf's staff added to inventory. \n")
        print("As you thank him and turn to leave back to the colosseum, the old man speaks for the"
                " first time. \"We will pray for you. Good luck.\" You thank them again and head back to "
                "the colosseum. ")
        return "colosseum"
    else:
        print("\nThe elf and old man's eyes light up when you enter again. \"You're back,\" the elf"
                " muses. Seeing him again, you really can't help but admire his looks. You become slightly"
                " jealous but show nothing of it. ")
        print("\"You really should go. We will do fine here alone. You have your own path to take. Although,"
                " it was nice seeing you again,\" the elf says. An ethereal smile spreads across his face, dazzling you,"
                " then he shoos you out of the room, sending you walking back to the colosseum. ")
