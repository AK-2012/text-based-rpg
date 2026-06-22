from player import Character
from rooms import *
from rooms.constants import *

def main():
    while True:
        system("clear")
        player = Character()
        while True:
            try:
                player.room = globals()[player.room](player)
                if player.room == "end":
                    break
            except (EOFError, KeyboardInterrupt):
                print()
                break
        again = input(f"{Fore.BLUE}{Style.BRIGHT}Would you like to play again? (y/n) {Style.RESET_ALL}").strip().lower()
        while again not in ["y", "n"]:
            again = input(f"{Fore.BLUE}{Style.BRIGHT}Would you like to play again? (y/n) {Style.RESET_ALL}").strip().lower()
        if again == "y":
            continue
        break
    print("Thanks for playing!")
    sys.exit(0)


if __name__ == "__main__":
    main()

