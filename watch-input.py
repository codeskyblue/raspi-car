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
        print("Press any key to continue")
        while True:
            inp = term.inkey(timeout=.5)
            print("Input:", inp)
            handle_input(inp)


def handle_input(r, _input: str):
    inp = _input.lower()
    if inp == "q":
        sys.exit(0)
    elif inp == "w":
        r.value = (1, 1)
    elif inp == "a":
        r.value = (0, 1)
    elif inp == "s":
        r.value = (-1, -1)
    else:
        r.value = (0, 0)
    time.sleep(.2)
        

if __name__ == "__main__":
    main()
