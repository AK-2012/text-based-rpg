from .constants import *


def dead(self):
    sleep(2)
    # ascii art :)
    print(f"""{Fore.RED}{Style.BRIGHT}
------------------------------------------------------------------------------------------------

oooooo   oooo   .oooooo.   ooooo     ooo    oooooooooo.   ooooo oooooooooooo oooooooooo.
 `888.   .8'   d8P'  `Y8b  `888'     `8'    `888'   `Y8b  `888' `888'     `8 `888'   `Y8b
  `888. .8'   888      888  888       8      888      888  888   888          888      888
   `888.8'    888      888  888       8      888      888  888   888oooo8     888      888
    `888'     888      888  888       8      888      888  888   888    "     888      888
     888      `88b    d88'  `88.    .8'      888     d88'  888   888       o  888     d88' .o.
    o888o      `Y8bood8P'     `YbodP'       o888bood8P'   o888o o888ooooood8 o888bood8P'   Y8P

------------------------------------------------------------------------------------------------

""")
    self.hearts = 0
    sleep(1)
    return "end"
