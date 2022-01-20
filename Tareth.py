import sys, time
import InputValidation


def slow_print(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.00001)


def contract_safe():
    response = """
[YOU]: If he hated this contract so much, then why keep it?

[TARETH]: Issac was meticulous, liked to have everything in little filing cabinets and colour-coded folders. He probably wanted to send it to the office to make sure his records weren't incomplete.
1 - Ask why he waited so long to do it
2 - Ask if he kept all of his rejected contracts
"""
    slow_print(response)
    choice = InputValidation.check2()
    if choice == "1":
        response = """
[YOU]: If he was that meticulous, then why wait so long to have it put away? It's dated for nearly three weeks ago.

[TARETH]: Issac worked from home most days ever since he got engaged. He wanted to spend more time with his wife. He would only come in when he had to. Board meetings, contract signings, things that worked better when the joint owner wasn't video calling in. Now, if you wouldn't mind, I'd like to be alone for a bit.
"""
    else:
        response = """
[YOU]: Did he do this with everything?

[TARETH]: Pretty much. There was nothing worthless in his eyes. Every failure was a lesson learnt and every failed deal was a reminder that our values came first. You have to admire him for that.
"""
    slow_print(response)


class Tareth:

    def __init__(self, inventory):
        self.prompt = "\nTareth stands off in a darkly lit corner of the room, his eyes fixed on the table and the body of his former business partner. It hadn't been long, but you could already see the pain in his eyes.\n"
        slow_print(self.prompt)
        self.conversation_picker(inventory)

    def conversation_picker(self, inventory):
        if inventory["Scotch Bottle"] == 0 and inventory["Contract"] == 0:
            self.standard_conversation(inventory)
        elif inventory["Scotch Bottle"] == 1 and inventory["Contract"] == 0:
            self.bottle_conversation(inventory)
        elif inventory["Scotch Bottle"] == 0 and inventory["Contract"] == 1:
            self.contract_conversation(inventory)
        else:
            self.contract_and_bottle_conversation(inventory)

    def standard_conversation(self, inventory):
        start = "\n[TARETH]: What do you want?\n   1 - Ask about relationship with Issac\n   2 - Ask about relationship with William\n   3 - Ask about relationship with Mia\n   4 - Ask about relationship with Janet\n     5 - Leave\n"
        slow_print(start)
        choice = InputValidation.check5()
        if choice == "1":
            self.issac_rel(inventory)
        elif choice == "2":
            self.william_rel(inventory)
        elif choice == "3":
            self.mia_rel(inventory)
        elif choice == "4":
            self.janet_rel(inventory)
        else:
            return inventory

    def bottle_conversation(self, inventory):
        start = "[TARETH]: What do you want?\n   1 - Ask about relationship with Issac\n    2 - Ask about relationship with William\n   3 - Ask about relationship with Mia\n   4 - Ask about relationship with Janet\n    5 - Ask about the bottle\n   6 - Leave"
        slow_print(start)
        choice = InputValidation.check6()
        if choice == "1":
            self.issac_rel(inventory)
        elif choice == "2":
            self.william_rel(inventory)
        elif choice == "3":
            self.mia_rel(inventory)
        elif choice == "4":
            self.janet_rel(inventory)
        elif choice == "5":
            self.bottle(inventory)

    def contract_conversation(self, inventory):
        self.start = "[TARETH]: What do you want?\n   1 - Ask about relationship with Issac\n    2 - Ask about relationship with William\n   3 - Ask about relationship with Mia\n   4 - Ask about relationship with Janet\n    5 - Ask about the contract\n   6 - Leave\n"
        slow_print(self.start)
        self.choice = input("> ")
        while self.choice not in ["1", "2", "3", "4", "5", "6"]:
            print("Invalid, try again")
            self.reply = input("> ")
        if self.choice == "1":
            self.issac_rel(inventory)
        elif self.choice == "2":
            self.william_rel(inventory)
        elif self.choice == "3":
            self.mia_rel(inventory)
        elif self.choice == "4":
            self.janet_rel(inventory)
        elif self.choice == "5":
            self.contract(inventory)

    def contract_and_bottle_conversation(self, inventory):
        self.start = "[TARETH]: What do you want?\n   1 - Ask about relationship with Issac\n    2 - Ask about relationship with William\n   3 - Ask about relationship with Mia\n   4 - Ask about relationship with Janet\n    5 - Ask about the bottle\n   6 - Ask about the contract\n   6 - Leave\n"
        slow_print(self.start)
        self.choice = input("> ")
        while self.choice not in ["1", "2", "3", "4", "5", "6"]:
            print("Invalid, try again")
            self.reply = input("> ")
        if self.choice == "1":
            self.issac_rel(inventory)
        elif self.choice == "2":
            self.william_rel(inventory)
        elif self.choice == "3":
            self.mia_rel(inventory)
        elif self.choice == "4":
            self.janet_rel(inventory)
        elif self.choice == "5":
            self.bottle(inventory)
        elif self.choice == "6":
            self.contract(inventory)


    def issac_rel(self, inventory):
        self.response = "[TARETH]: We were good friends since college. We ended up going to the same university and when we finished, we knew we wanted to work together. So, we founded our company and everything went great for us. Only, now it's not. I guess it all started when he became distant. Ever since he got engaged, he's been spending less time around the office and less time on the company.\n    1 - Ask why he thinks they became distant\n    2 - Ask if he got angry at his friend abandoning him\n"
        slow_print(self.response)
        self.reply = input("> ")
        while self.reply not in ["1", "2"]:
            print("Invalid, try again")
            self.reply = input("> ")
        if self.reply == "1":
            self.response = "[YOU]: Do you think she was the reason you became distant?\n\n[TARETH]: Definitely. I never really liked her much to begin with. She was always too controlling for my liking. A little word of advice: don't trust a thing that woman says.\n"
        else:
            self.response = "[YOU]: So, you were angry at him, because he chose her over you?\n\n[TARETH]: If you're trying to make it seem like I killed him, I didn't. Now, fuck off and go accuse someone else.\n"
        slow_print(self.response)
        self.conversation_picker(inventory)

    def william_rel(self, inventory):
        self.response = "[TARETH]: The kid? I never liked him much. He's okay, but nothing special - too coddled by his mother and father to truly understand what it takes to succeed.\n   1 - Agree\n   2 - Disagree\n"
        slow_print(self.response)
        self.reply = input("> ")
        while self.reply not in ["1", "2"]:
            print("Invalid, try again")
            self.reply = input("> ")
        if self.reply == "1":
            self.response = "[YOU]: He doesn't seem like the brightest, I must admit\n\n[TARETH]: *laughs* Glad you agree with me. I couldn't stand that kid when he used to come into the office. Hard to get anything done when he's yapping at you all the time.\n"
        else:
            self.response = "[YOU]: He's not that bad.\n\n[TARETH]: Hmm, thought you would've seen it like me. Nevermind.\n"
        slow_print(self.response)
        self.conversation_picker(inventory)

    def mia_rel(self, inventory):
        self.response = "[TARETH]: Her? Never really had much trouble with her to be honest. She was always the quiet one out of his kids. A talented artist, for sure, but she had little interest in her father's business\n   1 - Ask if she ever argued with her dad\n   2 - Say she sounds like a good kid\n"
        slow_print(self.response)
        self.reply = input("> ")
        while self.reply not in ["1", "2"]:
            print("Invalid, try again")
            self.reply = input("> ")
        if self.reply == "1":
            self.response = "[YOU]: It sounds like she would have argued with him a lot, don't you think?\n\n[TARETH]: Meh, I never heard much from them. They got along most of the time, from what I know at least.\n"
        else:
            self.response = "[YOU]: She sounds like a good kid.\n\n[TARETH]: The better of the two, for sure. Shame though, she had what it took to take over from him.\n"
        slow_print(self.response)
        self.conversation_picker(inventory)

    def janet_rel(self, inventory):
        self.response = "[TARETH]: Oh... her. I never really liked her. From the moment we met in Issac's office, we never got along.\n   1 - Ask why\n   2 - Ask if he thinks she did it\n   3 - Say she can't be that bad\n"
        slow_print(self.response)
        self.reply = input("> ")
        while self.reply not in ["1", "2", "3"]:
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
        self.conversation_picker(inventory)

    def bottle(self, inventory):
        response = """
[YOU]: I found this bottle in his study alongside a congratulations card.

[TARETH]: Oh, that. Yeah, we used to drink this around the office all the time - usually to celebrate a big score or some new deal we cooked up. Those were the days. I thought that this might remind of that time, so we could go back.
    1 - Ask why he was so sentimental
    2 - Ask why the seal was openned but the bottle was full
    3 - Ask if he wants a drink
"""
        slow_print(response)
        reply = InputValidation.check3()
        if reply == "1":
            response = """
[TARETH]: I dunno. I guess when you've known someone a certain way for so long, you always see them like that. I missed my business partner, but more importantly, I missed my friend. You get me, right?
    1 - Yes
    2 - No
"""
            slow_print(response)
            choice = InputValidation.check2()
            if choice == "1":
                response = "[TARETH]: I knew you would. Now, if you wouldn't mind, I'd like to be alone for a bit."
            else:
                response = "[TARETH]: Well, maybe one day you will. Now, if you wouldn't mind, I'd like to be alone for a bit."
            slow_print(response)
        elif reply == "2":
            response = """
[TARETH]: Issac was always picky with when he drank. Had to be a certain way, a certain temperature and with certain additions. He was a particular man; I guess that's what made him so good at business. Still, it's a shame he didn't drink it when he had the chance.
    1 - Ask what will happen with the company now
    2 - Ask what he will do now
            """
            slow_print(response)
            choice = InputValidation.check2()
            if choice == "1":
                response = """
[YOU]: So now that the joint owner is dead, what will happen with the business now?

[TARETH]: Well, that depends. If the prodigal son rises to the occassion, I'll sell my stocks and retire some place nice and warm while my empire falls. If not, then I'll continue in his name. Let's hope I don't have to wait long. That information should be in his will, though I have no clue where he hid it. Now, if you wouldn't mind, I'd like to be alone for a bit."""
            else:
                response = """
[YOU]: So what's next for you?

[TARETH]: Well all eyes are going to be on me. I'll have to hold a press briefing this weekend and clear the air. After that, whoever gets the stock gets the stock. That information should be in his will, though I have no clue where he hid it. Now, if you wouldn't mind, I'd like to be alone for a bit."""
            slow_print(response)
        else:
            response = """
[TARETH]: No thanks. That bottle was meant to be for him - it would be bad of me to take it from him. Now, if you wouldn't mind, I'd like to be alone for a bit.
"""
            slow_print(response)

    def contract(self, inventory):
        response = """
[YOU]: I found this contract in his study safe. It has your signature on it, but not his. Care to explain?

[TARETH]: That was a business deal that Issac didn't particularly like. He said he found it too shady to stake our brand name on it. We made an agreement that both of us have to sign on a deal for it to be accepted, but as you can tell, it never went through. Shame it never did.
    1 - Ask why
    2 - Ask if there were more like it
    3 - Ask why it was in his safe
"""
        slow_print(response)
        choice = InputValidation.check3()
        if choice == "1":
            self.contract_reasoning(inventory)
        elif choice == "2":
            self.contract_questioning(inventory)
        else:
            contract_safe(inventory)

    def contract_reasoning(self, inventory):
        response = """
[YOU]: What was so special about this deal?

[TARETH]: It was with another large firm in the country, we were always in competition so this deal seemed like a perfect way to pour our efforts in the market together. Issac didn't like it because it would mean sacrificing some of our worker benefits for the sake of keeping the profit margins. I assured him this would only be a temporary condition, but even that put him off.
    1 - Ask why he thought it was okay to do that?
    2 - Ask how it ended up in his safe
"""
        slow_print(response)
        choice = InputValidation.check2()
        if choice == "1":
            response = """
[YOU]: You were seriously going to cut worker benefits to compete? Why?

[TARETH]: Because that's business. We have to make hard decisions to reach the top. Issac knew this, but he had a good heart. To be honest, I didn't want to have to do it myself, but the deal rided on us being willing to sacrifice. 
    1 - Say you understand
    2 - Say you don't agree
"""
            choice = InputValidation.check2()
            if choice == "1":
                response = """
[YOU]: If it was only temporary then I don't see the problem/

[TARETH]: Exactly my point. I mean it was nothing massive, just a few bonuses here and there and it would have been fine. They wouldn't have missed them. Now, if you don't mind, I'd like to be left alone.
        """
            else:
                response = """
[YOU]: I can't believe you'd think that's okay.

[TARETH]: Easy there. I'm not talking about slavery. It would have been nothing massive, just a few bonuses here and there and it would have been fine. They wouldn't have missed them. Now, if you don't mind, I'd like to be left alone.
"""
            slow_print(response)
        else:
            response = """
[YOU]: So what's next for you?

[TARETH]: Well all eyes are going to be on me. I'll have to hold a press briefing this weekend and clear the air. After that, whoever gets the stock gets the stock. That information should be in his will, though I have no clue where he hid it. Now, if you wouldn't mind, I'd like to be alone for a bit.
"""
        slow_print(response)

    def contract_questioning(self, inventory):
        response = """
[YOU]: This can't be only kind of contract like this that came across your desk. What was so special about this one?

[TARETH]: Like I said, it was in partnership with one of the biggest firms in the country. This was our shot to grow beyond our wildest dreams. I guess it was never meant to be.
    1 - Ask if he thinks that Issac would have ever changed his mind
    2 - Say you side with him
"""
        slow_print(response)
        choice = InputValidation.check2()
        if choice == "1":
            response = """
[YOU]: Do you think he would have ever changed his mind?

[TARETH]: Who? Issac? No. Once his mind was made, nothing could change it. If there's one thing we both had in common, it was that we were both stubborn. Now, if you wouldn't mind, I'd like to be alone for a bit.
"""
        else:
            response = """
[YOU]: I have to say. If this meant you'd get in with your biggest competitors, then I would have signed it.

[TARETH]: Glad we see eye to eye on this. Shame that me and Issac never did. It would have been easier to boil the salt from the ocean than to change his mind. Now, if you wouldn't mind, I'd like to be alone for a bit.
"""
        slow_print(response)
