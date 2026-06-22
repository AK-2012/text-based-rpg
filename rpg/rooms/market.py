from .constants import *


def market(self):
    # sluuuurp
    print("\nYou head to the bustling streets of the market. Various peddlers and stalls are around. Mouth-watering "
            "aromas hit you since you've had the same meal of stale bread and cheese, peas, and hard water for the whole"
            " time you were imprisoned. Around you, you see delectable street foods. One stall has hot, fresh xiao long bao."
            " Another has shish kebabs right off the grill. Across from where you're standing, pani puri is being handed out"
            " to patrons. You would love to buy something, but have no money. Numerous other goods are being sold as well, "
            "with a pretty lady modeling for an accessory booth and home goods being sold by a pudgy, friendly-looking fellow. "
            "A quick path through the alleys can lead you to the slums, or heading a little further up the market path can "
            "lead you to the rich neighborhood. Back where you came is the colosseum's spectator entrance. ")
    # if the man's daughter is still kidnapped
    if "coins" not in self.items:
        print("Off in the corner a dewy-eyed, middle-aged man with a dejected look on his face is handing out flyers. ")
    while True:
        go = input(f"{Fore.BLUE}{Style.BRIGHT}\nWhere would you like to go? {Style.RESET_ALL}").strip().lower()
        # we do not want the player walking around with the dad's girl. that is unsafe and concerning.
        if not any(word in go for word in ["man", "guy", "flyer"]) and "girl" in self.items:
            print("You might want to go to the girl's father...")
            continue
        else:
            # start daughter quest
            if any(word in go for word in ["man", "guy", "flyer"]) and "coins" not in self.items:
                break
            # leave
            elif "slums" in go:
                return "slums"
            elif "rich" in go:
                return "rich"
            elif ("spectator" in go and "entrance" in go) or "colosseum" in go:
                return "spectator_entrance"
            # data validation
            else:
                print("Nothing happens.")
    # quest for daughter -- 1st encounter
    if "flyer" not in self.items:
        print("\nYou head over to the dejected, dewy-eyed, middle-aged man. You ask if he's okay. ")
        print("\"Am I okay! Of course not! I've been handing these flyers out all morning, and nobody's batted an eye. "
            "That's how all these people here are; nobody's willing to put themselves in harm's way for a little girl's sake. "
            "My daughter was kidnapped by some of those vulgar slum scoundrels! I don't suppose you'd be fine with helping"
            " a guy out, will you?\"")
        help = input().strip().lower()
        # invalid inputs
        while help not in ["n", "y", "no", "yes"]:
            help = input(f"{Fore.BLUE}{Style.BRIGHT}\"Hmm?\" {Style.RESET_ALL}").strip().lower()
        # not helping
        if help in ["n", "no"]:
            print("\nThe man sighs. \"Yeah. I thought so. I'm sorry, I've just been having a bad day. I'll see you around, I"
                " s'pose.\" The man sighs and goes back to handing out fliers. ")
        # being a good person
        else:
            print("\nThe man's eyes light up. \"Oh, thank you, thank you, bless you. You are a savior. My daughter was"
                " kidnapped earlier by some nasty slum scum. You could probably find her if you headed over there. "
                "If you can bring her back, I'll give you a good sum of cash.\" He eyes your clothes. \"You could "
                "probably get something to eat and maybe some new clothes, too. Thank you.\" Before you leave, "
                "he hands you a flyer with a picture of his daughter. You tuck it away in your pocket.")
            self.items.append("flyer")
    # return daughter
    else:
        if "girl" in self.items:
            print("The man's eyes light up as you head over with his daughter. A smile lights up his face. "
            "He thanks you profusely while he and his daughter have a heartfelt reunion. He hands you a small bag of coins.")
            self.items.append("coins")
            self.items.remove("girl")
            self.eat()
            print(f"{Fore.GREEN}{Style.BRIGHT}You head over to a stall and buy some food. You ravenously dig in, and "
                    f"it's over before you know it. You have {self.hearts} hearts now.")
        else:
            print("\nThe man says, "
                    "\"You still haven't found her? Okay... Please do find her soon. I hope nothing too bad has happened to her. Please do find her. Please.\"")
    while True:
        go = input(f"{Fore.BLUE}{Style.BRIGHT}Where would you like to go? {Style.RESET_ALL}").strip().lower()
        # leave
        if "slums" in go:
            return "slums"
        elif "rich" in go:
            return "rich"
        elif ("spectator" in go and "entrance" in go) or "colosseum" in go:
            return "spectator_entrance"
        # data validation
        else:
            print("Nothing happens.")
