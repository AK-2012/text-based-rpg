from .constants import *


def win_witch(self):
    # main ending
    print(
        "Walking out of the castle, the sun is rising. You bask in the sunlight for a moment, a smile spreading"
        " across your face. At last, the lands are freed of the tyrant. At last, YOU are free again. You walk off"
        " into the forest, heading back towards your village to provide them the great news. "
    )
    if "has_heart" in self.flags:
        print("By your side, the Heart of the Seasons pulsates in a bright yellow. "
        "You smile, knowing wherever you go will prosper, much needed after the tyranny of the king. ")
        print(rf"""{Fore.YELLOW}{Style.BRIGHT}

                \ _________ /
               _ /_|_____|_\ _
                 '. \   / .'
                   '.\ /.'
                     '.' 
        """)
    print(rf"""{Fore.CYAN}{Style.BRIGHT}

          ........::::::::::::..           .......|...............::::::::........
     .:::::;;;;;;;;;;;:::::.... .     \   | ../....::::;;;;:::::.......
         .       ...........   / \\_   \  |  /     ......  .     ........./\
...:::../\\_  ......     ..._/'   \\\_  \###/   /\_    .../ \_.......   _//
.::::./   \\\ _   .../\    /'      \\\\#######//   \/\x  //   \_   ....////X
    _/      \\\\   _/ \\\ /  x       \\\\###////     xXXx//     \__  _////Xxx
  ./   x       \\\/     \/ x X           \//////    XxXX           \/////xxXxx
 /     XxX     \\/         XxX X                      Xx            ////  Xx
-----XxX-------------|-------XxX-----------*--------|-X-*-----|------------X--
       X        _X      *    X      **         **     X       x   **    *  X
      _X                    _X           x                *          x     X_


        """)
    return "end"
