from .constants import *


def room_o_doom(self):
    print("""
There's a portal in this room. Made of a beautiful black marble, runic script carved into it spells out:

 )_)  _   _ _     ) o  _   _   _)_ ( _   _          o _)_ _ ( _  | _    _ ( _   _   _ ) _
( (  )_) ) )_)   (  ( )_) (    (_   ) ) )_)   )_)_) ( (_ (_  ) )  (    (_( )_) (_) (_( )_) o
    (_    (_         (_   _)           (_                         _)                  (_

You feel like you should go through. Back in one direction are the stairs, and in the other is a hallway.
              """)
    while True:
        go = (
            input(
                f"{Fore.BLUE}{Style.BRIGHT}Where would you like to go? {Style.RESET_ALL}"
            )
            .strip()
            .lower()
        )
        if "portal" in go or "through" in go or "witch" in go:
            return "witch_tower"
        elif "hall" in go:
            return "hall"
        elif "stair" in go:
            return "stairs"
        else:
            print("Nothing happens. ")
