import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, Key, KeyCode

delay = 0.001
clicking = False
spKey = KeyCode(char='f')

mouse = Controller()


def on_press(key):
    global clicking
    if key == spKey:
        if clicking == True:
            clicking = False
            print("Off")

        elif clicking == False:
            clicking = True
            print("Clicking...")


def click_loop():
    while True:
        if clicking:
            mouse.press(Button.left)
            mouse.release(Button.left)
            time.sleep(delay)


thread = threading.Thread(target=click_loop)
thread.start()

with Listener(on_press=on_press) as listener:
    listener.join()
