# import the libraries
import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, Key, KeyCode

# define your variables
delay = 0.001
clicking = False                # Set clicking to False so the clicker doesn't run on start
spKey = KeyCode(char='f')       # The key to start and stop the autoclicker

# make an object
mouse = Controller()

# make a function with a key parameter
def on_press(key):
    global clicking             # You need a global variable since the variable is defined oustide of this function
    if key == spKey:
        if clicking == True:    # If clicking is already running/True 
            clicking = False    # Set clicking to False to turn the clicker off
            print("Off")

        elif clicking == False: # If clicking is not running/False
            clicking = True     # Set clicking to True/run the clicker
            print("Clicking...")

# make a function that loops left click
def click_loop():
    while True:
        if clicking:            # If clicking == True, run this code block
            mouse.press(Button.left)
            mouse.release(Button.left)
            time.sleep(delay)


thread = threading.Thread(target=click_loop)
thread.start()

with Listener(on_press=on_press) as listener:
    listener.join()
