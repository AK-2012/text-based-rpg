from .constants import *


def weapons_chamber(self):
    if any(weapon in self.items for weapon in ["longsword", "dagger", "rapier"]):
        print("You already got a weapon, so you return to the witch's toewr. ")
        return "witch_tower"
    print("You enter an armory filled to the brim with weapons. Most are under lock and key, "
            "but a few aren't, including swords, bows, staffs, and subdivisions of them. You"
            " see a few weapons that suit your taste: a longsword, a dagger, and a rapier. ")
    take = input(f"{Fore.BLUE}{Style.BRIGHT}Which weapon would you like to take? {Style.RESET_ALL}").strip().lower()
    while take not in ["longsword", "dagger", "rapier"]:
        take = input(f"{Fore.BLUE}{Style.BRIGHT}Which weapon would you like to take? {Style.RESET_ALL}").strip().lower()
    self.damage_check()
    print(f"You took the {take}. You deal {self.attack} damage now. You return to the witch's tower.")
    return "witch_tower"
