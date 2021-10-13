from pynput import keyboard
from pynput.keyboard import Controller as keyboard_controller
from pynput.mouse import Controller as mouse_controller
from pynput.mouse import Button
from pynput.mouse import *

import time
'''
STEPS 

download python im not showing you how to do that 

import this garbage 
on mac do    -    "pip3 install pynput"    and    "pip3 install keyboard"
on windows do    -    "pip install pynput"    and    "pip install keyboard"
BAM YOU'RE DONE     if it doens't work don't blame me im just the moron who coded this :)


# to get the code uhhhh it will prob be in the desc but idk #
# to get the code uhhhh it will prob be in the desc but idk #
# to get the code uhhhh it will prob be in the desc but idk #
# to get the code uhhhh it will prob be in the desc but idk #

# to get the code uhhhh it will prob be in the desc but idk #
# to get the code uhhhh it will prob be in the desc but idk #

# fun facts # 
this thing can click up to about 600 cps
it crashed my computer so like u were warned but only if u read this
also um it can be buggy so be careful about that
'''


mouse = mouse_controller()
keys = keyboard_controller()

left = False
right = False
CPS = int(input("CPS (default=10): ") or 10)
if CPS == 0:
    delay = 0
else:
    delay = 1 / CPS


def key_pressed(key):
    global left, right
    kill = 'k'
    toggle_left = '['
    toggle_right = ']'
    try:
        if key.char == kill:
            quit()

        if key.char == toggle_left and not left:
            left = True

        elif key.char == toggle_left and left:
            left = False

        if key.char == toggle_right and not right:
            right = True

        elif key.char == toggle_right and right:
            right = False

    except:
        pass


key_listener = keyboard.Listener(on_press=key_pressed)
key_listener.start()



while True:
    try:
        if left:
            mouse.click(Button.left)
            time.sleep(delay)
        elif right:
            mouse.click(Button.right)
            time.sleep(delay)

    except KeyboardInterrupt:
        print("\nClicker Stopped!")
        break
quit()
