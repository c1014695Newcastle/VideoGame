def check7():
    choice = input("> ")
    while choice not in ["1", "2", "3", "4", "5", "6", "7"]:
        choice = input("Invalid - Try again \n> ")
    return choice


def check6():
    choice = input("> ")
    while choice not in ["1", "2", "3", "4", "5", "6"]:
        choice = input("Invalid - Try again \n> ")
    return choice


def check4():
    choice = input("> ")
    while choice not in ["1", "2", "3", "4"]:
        choice = input("Invalid - please try again\n> ")
    return choice


def check5():
    choice = input("> ")
    while choice not in ["1", "2", "3", "4", "5"]:
        print("Invalid, try again")
        choice = input("> ")
    return choice

def check3():
    choice = input("> ")
    while choice not in ["1", "2", "3"]:
        print("Invalid, try again")
        choice = input("> ")
    return choice

def check2():
    choice = input("> ")
    while choice not in ["1", "2"]:
        print("Invalid, try again")
        choice = input("> ")
    return choice