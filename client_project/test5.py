#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket
import sys
from pynput import keyboard
from pynput.keyboard import Key, KeyCode
key_stack = []
def on_press(key):
    msg = '{0}'.format(key) 
    print(msg)
    #print("'\x02'" == msg)
    print(r"'\x02'" == msg)
    if "'q'" == msg:
        1/0
def on_release(key):
    pass

while True:
    with keyboard.Listener(
        on_press = on_press,
        on_release = on_release) as listener:
        listener.join()
