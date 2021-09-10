import time
from pynput.keyboard import Key, Controller

keyboard = Controller()

time.sleep(5)

for char in "Good morning Bob. What's going on for you?":
    keyboard.press(char)
    keyboard.release(char)
    time.sleep(0.12)

