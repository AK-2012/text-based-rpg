from .constants import *


def four_seasons_room(self):
    print(
        "\nYou enter a large, dome shaped room. It is beautiful and chaotic all at once; "
        "each quarter of the room is taken up by a different representation of a season. "
        "Where you are, fresh new spring buds are rising through the dirt at your feet. "
        "A cherry blossom tree's flowers emanate a sweet scent. On the right of this quarter, "
        "snow is falling from god-knows-where onto a bluish-green-needled pine tree. The floor"
        " is blanketed with freshly fallen snow. On the left of this quarter, heat shimmers the"
        " air. Plants in full green lushly cover it, and a bird tweets on one of them. Finally, "
        "across from you, a maple tree drops its leaves in hues of red, orange, and gold onto the"
        "already-carpeted dirt. You now understand why the name is the Four Seasons Room. \n"
    )
    print(
        "\nYou see a pedestal in the center of the room, where the seasons meet."
        "There rests a crystal the size of your fist, slowly cycling through soft green,"
        " blazing gold, deep crimson, and cold blue light. As you draw closer, you recognize"
        " the stories from your homeland: this is the Heart of the Seasons, a stone formed by"
        " the gods placing together a tear of each season's essence, said to nurture the land"
        " and slowly aid the user.\n"
    )
    reach = (
        input(
            f"{Fore.BLUE}{Style.BRIGHT}The Heart is calling to you. Do you answer? {Style.RESET_ALL}"
        )
        .strip()
        .lower()
    )
    while reach not in ["y", "yes"]:
        reach = (
            input(
                f"{Fore.BLUE}{Style.BRIGHT}The Heart wants an answer. \n{Style.RESET_ALL}"
            )
            .strip()
            .lower()
        )
    print("You reach out to cradle the Heart.\n")
    if "crown" not in self.items:
        print(
            "\nThe Heart rejects you, unconvinced of your valor and dignity. A heavenly feeling"
            " spreads through you, then consumes you."
        )
        return "dead"
    print(
        "\nThe Heart accepts you, convinced of your valor and dignity. You smile looking down at it. "
    )
    print(
        "You head out of the room into the next corridor. A triangular room opens up before you. "
    )
    return "exit"
