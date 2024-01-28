import pynput

from pynput.keyboard import Key, Listener

def on_press(key):
    print("press")

def on_release(key):
    print("release")

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()