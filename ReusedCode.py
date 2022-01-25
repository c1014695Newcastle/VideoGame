import sys, time, os

def checkn(n):
    choice = input("> ")
    while choice not in [str(w) for w in range(1, n+1)]:
        choice = input("Invalid - Try again \n> ")
    return choice

def slow_print(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.00001)

