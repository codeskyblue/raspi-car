#!/usr/bin/env python3
# coding:utf-8
#

import time
import gpiozero as gz
from signal import pause

def main():
    r = gz.Robot((14, 4), (18, 15))
    r.forward()
    time.sleep(.2)
    r.stop()

    plan_a = True
    if plan_a:
        buttons = []
        ports = (26, 19, 13, 6)
        funcs = (r.forward, r.backward, r.left, r.right)
        for i in range(4):
            btn = gz.Button(ports[i])
            print("Set button:", btn, ports[i])
            btn.when_pressed = funcs[i]
            btn.when_released = r.stop
            buttons.append(btn)

        print(buttons)

    if not plan_a:
        #for port_num in (26, 19, 13, 6)
        btnF = gz.Button(26)
        btnF.when_pressed = r.forward
        btnF.when_released = r.stop

        btnB = gz.Button(19)
        btnB.when_pressed = r.backward
        btnB.when_released = r.stop

    pause()

if __name__ == "__main__":
    main()
