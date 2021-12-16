# coding: utf-8
#

import time
import sys
from blessed import Terminal
import gpiozero as gz


def main():
    r = gz.Robot((14, 4), (18, 15))
    term = Terminal()

    with term.cbreak():
        print("Press any key to continue, z to quit")
        while True:
            inp = term.inkey(timeout=.5)
            print("Input:", inp)
            handle_input(r, inp)


def handle_input(r, _input: str):
    inp = _input.lower()
    if inp == "z":
        sys.exit(0)
    elif inp == "w":
        r.forward()
    elif inp == "s":
        r.backward()
    elif inp == "q":
        r.value = (0.15, 1)
    elif inp == "e":
        r.value = (1, 0.15)
    elif inp == "a":
        r.left()
    elif inp == "d":
        r.right()
    else:
        r.stop()
        

if __name__ == "__main__":
    main()
