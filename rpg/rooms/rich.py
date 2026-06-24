from .constants import *


def rich(self):
    print(
        "\nYou head over to the exclusive network of rich people in the underground city, the rich neighborhood. "
        "It smells like money here, and the streets are free of all dirt. Rich kids playing outside eye your soiled"
        " clothes with distaste. You hear one ask its mommy if you're a beggar.\n"
    )
    print(
        "A stall catches your eye. It is the only one there. A man with an interesting assortment of trinkets"
        " is selling them. You walk up to him. He eyes you warily, clearly distrustful of you. You ask him "
        'if he has anything you can buy. \n"For you? Nothing. If you have something useful on you, I can give'
        ' you some information, though." '
    )
    if "staff" in self.items:
        print(
            "\nYou're suddenly reminded of the staff the elf gave you. You present it to the seller. He "
            "nods with satisfaction. \"An elf's staff? I don't know where you got this, but it'll do, if"
            " you're willing to give it up.\""
        )
        do = (
            input(
                f"{Fore.BLUE}{Style.BRIGHT}\nWould you like to give him the staff in exchange for information? {Style.RESET_ALL}"
            )
            .strip()
            .lower()
        )
        while do not in ["y", "yes", "n", "no"]:
            do = (
                input(
                    f"{Fore.BLUE}{Style.BRIGHT}Would you like to give him the staff in exchange for information? {Style.RESET_ALL}"
                )
                .strip()
                .lower()
            )
        if do in ["y", "yes"]:
            print(
                '\nYou hand the staff over to him. He grins. "Great. Let me tell you about the King\'s castle." '
                'He eyes around you warily, leaning in closer and talking quieter. "They say the King has a lot'
                " of secrets. I'd say this is just rumour if I hadn't heard more than a few people talking about"
                " it. Apparently, on the highest floor, a witch's residency is located, and there's also a chained"
                " dragon. I believe the king's tryna force them to do his bidding, but that's just speculation; "
                "who knows? But back to the witch -- it's said that she's blind since the king managed to take out"
                " her eyes. He's still scared as a dog with its tail between its legs when it comes to her, but "
                "it's said that if somebody else can take an eye of hers, they get... inhuman powers.\" He looks"
                " around you. \"You might even be able to get out of the castle. But don't tell anybody I told you"
                ' that. Now shoo."'
            )
        else:
            print(
                "The man sighs. \"If that's what you want. My offer still stands if you're ever interested.\""
            )
    # no elf staff
    else:
        print(
            "You don't have anything useful the man might like. He clicks his tongue and shoos you away from the stall. "
        )
    print("\nYou head back to the street.")
    while True:
        go = (
            input(
                f"{Fore.BLUE}{Style.BRIGHT}Where would you like to go? {Style.RESET_ALL}"
            )
            .strip()
            .lower()
        )
        if "market" in go:
            return "market"
        elif "slums" in go:
            return "slums"
        elif ("spectator" in go and "entrance" in go) or "colosseum" in go:
            return "spectator_entrance"
        else:
            print("Nothing happens.")
