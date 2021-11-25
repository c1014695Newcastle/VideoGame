import sys,time

def slow_print(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.025)

class Tareth():

    def __init__(self, contract, bottle):
        self.prompt = "\nTareth stands off in a darkly lit corner of the room, his eyes fixed on the table and the body of his former business partner. It hadn't been long, but you could already see the pain in his eyes.\n"
        slow_print(self.prompt)
        if bottle == 0 and contract == 0:
            self.standard_conversation()
        elif bottle == 0 and contract == 1:
            self.bottle_conversation()
        elif bottle == 1 and contract == 0:
            self.contract_conversation()
        else:
            self.contract_and_bottle_conversation()

    def standard_conversation(self):
        self.start = "\n[TARETH]: What do you want?\n   1 - Ask about relationship with Issac\n   2 - Ask about relationship with William\n   3 - Ask about relationship with Mia\n   4 - Ask about relationship with Janet\n     5 - Leave\n"
        slow_print(self.start)
        self.choice = input("> ")
        while self.choice not in ["1","2","3","4","5"]:
            print("Invalid, try again")
            self.reply = input("> ")
        if self.choice == "1":
            self.issac_rel()
        elif self.choice == "2":
            self.william_rel()
        elif self.choice == "3":
            self.mia_rel()
        elif self.choice == "4":
            self.janet_rel()
        else:
            self.main_room()

    def bottle_conversation(self):
        self.start = "[TARETH]: What do you want?\n   1 - Ask about relationship with Issac\n    2 - Ask about relationship with William\n   3 - Ask about relationship with Mia\n   4 - Ask about relationship with Janet\n    5 - Ask about the bottle\n   6 - Leave"
        slow_print(self.start)
        self.choice = input("> ")
        while self.choice not in ["1", "2", "3", "4","5","6"]:
            print("Invalid, try again")
            self.reply = input("> ")
        if self.choice == "1":
            self.issac_rel()
        elif self.choice == "2":
            self.william_rel()
        elif self.choice == "3":
            self.mia_rel()
        elif self.choice == "4":
            self.janet_rel()
        elif self.choice == "5":
            self.bottle()
        else:
            self.main_room()

    def contract_conversation(self):
        self.start = "[TARETH]: What do you want?\n   1 - Ask about relationship with Issac\n    2 - Ask about relationship with William\n   3 - Ask about relationship with Mia\n   4 - Ask about relationship with Janet\n    5 - Ask about the contract\n   6 - Leave\n"
        slow_print(self.start)
        self.choice = input("> ")
        while self.choice not in ["1", "2", "3", "4","5","6"]:
            print("Invalid, try again")
            self.reply = input("> ")
        if self.choice == "1":
            self.issac_rel()
        elif self.choice == "2":
            self.william_rel()
        elif self.choice == "3":
            self.mia_rel()
        elif self.choice == "4":
            self.janet_rel()
        elif self.choice == "5":
            self.contract()
        else:
            self.main_room()

    def contract_and_bottle_conversation(self):
        self.start = "[TARETH]: What do you want?\n   1 - Ask about relationship with Issac\n    2 - Ask about relationship with William\n   3 - Ask about relationship with Mia\n   4 - Ask about relationship with Janet\n    5 - Ask about the bottle\n   6 - Ask about the contract\n   6 - Leave\n"
        slow_print(self.start)
        self.choice = input("> ")
        while self.choice not in ["1", "2", "3", "4","5","6"]:
            print("Invalid, try again")
            self.reply = input("> ")
        if self.choice == "1":
            self.issac_rel()
        elif self.choice == "2":
            self.william_rel()
        elif self.choice == "3":
            self.mia_rel()
        elif self.choice == "4":
            self.janet_rel()
        elif self.choice == "5":
            self.bottle()
        elif self.choice == "6":
            self.contract()
        else:
            self.main_room()


    def issac_rel(self):
        self.response = "[TARETH]: We were good friends since college. We ended up going to the same university and when we finished, we knew we wanted to work together. So, we founded our company and everything went great for us. Only, now it's not. I guess it all started when he became distant. Ever since he got engaged, he's been spending less time around the office and less time on the company.\n    1 - Ask why he thinks they became distant\n    2 - Ask if he got angry at his friend abandoning him\n"
        slow_print(self.response)
        self.reply = input("> ")
        while self.reply not in ["1","2"]:
            print("Invalid, try again")
            self.reply = input("> ")
        if self.reply == "1":
            self.response = "[YOU]: Do you think she was the reason you became distant?\n\n[TARETH]: Definitely. I never really liked her much to begin with. She was always too controlling for my liking. A little word of advice: don't trust a thing that woman says.\n"
        else:
            self.response = "[YOU]: So, you were angry at him, because he chose her over you?\n\n[TARETH]: If you're trying to make it seem like I killed him, I didn't. Now, fuck off and go accuse someone else.\n"
        slow_print(self.response)
        self.standard_conversation()


    def william_rel(self):
        self.response = "[TARETH]: The kid? I never liked him much. He's okay, but nothing special - too coddled by his mother and father to truly understand what it takes to succeed.\n   1 - Agree\n   2 - Disagree\n"
        slow_print(self.response)
        self.reply = input("> ")
        while self.reply not in ["1","2"]:
            print("Invalid, try again")
            self.reply = input("> ")
        if self.reply == "1":
            self.response = "[YOU]: He doesn't seem like the brightest, I must admit\n\n[TARETH]: *laughs* Glad you agree with me. I couldn't stand that kid when he used to come into the office. Hard to get anything done when he's yapping at you all the time.\n"
        else:
            self.response = "[YOU]: He's not that bad.\n\n[TARETH]: Hmm, thought you would've seen it like me. Nevermind.\n"
        slow_print(self.response)
        self.standard_conversation()


    def mia_rel(self):
        self.response = "[TARETH]: Her? Never really had much trouble with her to be honest. She was always the quiet one out of his kids. A talented artist, for sure, but she had little interest in her father's business\n   1 - Ask if she ever argued with her dad\n   2 - Say she sounds like a good kid\n"
        slow_print(self.response)
        self.reply = input("> ")
        while self.reply not in ["1","2"]:
            print("Invalid, try again")
            self.reply = input("> ")
        if self.reply == "1":
            self.response = "[YOU]: It sounds like she would have argued with him a lot, don't you think?\n\n[TARETH]: Meh, I never heard much from them. They got along most of the time, from what I know at least.\n"
        else:
            self.response = "[YOU]: She sounds like a good kid.\n\n[TARETH]: The better of the two, for sure. Shame though, she had what it took to take over from him.\n"
        slow_print(self.response)
        self.standard_conversation()


    def janet_rel(self):
        self.response = "[TARETH]: Oh... her. I never really liked her. From the moment we met in Issac's office, we never got along.\n   1 - Ask why\n   2 - Ask if he thinks she did it\n   3 - Say she can't be that bad\n"
        slow_print(self.response)
        self.reply = input("> ")
        while self.reply not in ["1","2","3"]:
            print("Invalid, try again")
            self.reply = input("> ")
        if self.reply == "1":
            self.response = "[YOU]: Why did you not like her?\n\n[TARETH]: She was always trying to boss him around, even at work. It was like it was her company, not ours.\n  1 - Ask why he came\n   2 - Say nothing\n"
            self.reply = input("> ")
            while self.reply not in ["1", "2"]:
                print("Invalid, try again")
                self.reply = input("> ")
            if self.reply == "1":
                self.response = "[YOU]: If you have such a problem with her then why did you come tonight?\n\n[TARETH]: Issac's my friend, and as much as I don't like her, I wanted to be there for him, like the old days... I...I guess I've lost all that now.\n"
            else:
                self.response = "\n"
        elif self.reply == "2":
            self.response = "[YOU]: Do you think she did it?\n\n[TARETH]: As bad as she may be, I don't think that she had the guts to do something like this. At least I hope not."
        else:
            self.response = "[YOU]: He's not that bad.\n\n[TARETH]: Hmm, thought you would've seen it like me. Nevermind.\n"
        slow_print(self.response)
        self.standard_conversation()

    def bottle(self):
        print("WIP")

    def contract(self):
        print("WIP")