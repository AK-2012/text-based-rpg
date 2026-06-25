from .constants import *


def riddle_door(self):
    print(
        "You approach the stone door the troll was guarding. Runes glow faintly across its surface. "
    )
    print(
        'The inscription asks, "What is not alive but grows, does not breathe but needs air?"\n'
    )
    while True:
        answer = (
            input(f"{Fore.BLUE}{Style.BRIGHT}What is your answer? {Style.RESET_ALL}")
            .strip()
            .lower()
        )
        if answer == "fire":
            print(
                "The runes flare brightly, then fade. The door grinds open, revealing a small chamber beyond. "
            )
            print(
                "On a gilded pedestal in the center of the room rests an ornate key shaped like a dragon."
            )
            if "dragonhold key" not in self.items:
                self.items.append("dragonhold key")
                print(
                    f"{Fore.YELLOW}{Style.BRIGHT}\nMysterious key added to inventory.\n"
                )
            print(
                "With the key in hand, you leave the chamber and return to the room where you fought the troll. "
            )
            return "troll_room"
        print( # wrong answer
            "The runes glow a vicious red. Your chest tightens as heat blooms under your skin. "
            "In an instant, your body is consumed by invisible flame.\n"
        )
        return "dead"
