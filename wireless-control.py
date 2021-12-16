#!/usr/bin/env python3
# coding:utf-8
#

import time
import gpiozero as gz
from signal import pause
from functools import partial


class MyRobot:
    def __init__(self):
        self._robot = gz.Robot((14, 4), (18, 15))
        self._cmds = []

    def push(self, command: str):
        self._cmds.append(command)
        self._execute()

    def pop(self):
        self._cmds.pop()
        self._execute()

    def _execute(self):
        if len(self._cmds) == 0:
            self._robot.stop()
        else:
            method_name = self._cmds[-1]
            fn = getattr(self._robot, method_name)
            fn()


def main2():
    r = MyRobot()
    buttons = []
    ports = (26, 19, 13, 6)
    funcs = ("forward", "backward", "left", "right")
    for i in range(4):
        btn = gz.Button(ports[i])
        print("Set button:", ports[i], funcs[i])
        btn.when_pressed = partial(r.push, funcs[i])
        btn.when_released = r.pop
        buttons.append(btn)

    print(buttons)


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
        # for port_num in (26, 19, 13, 6)
        btnF = gz.Button(26)
        btnF.when_pressed = r.forward
        btnF.when_released = r.stop

        btnB = gz.Button(19)
        btnB.when_pressed = r.backward
        btnB.when_released = r.stop

    pause()


if __name__ == "__main__":
    # main()
    main2()
