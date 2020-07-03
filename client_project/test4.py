#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket
import sys
from pynput import keyboard
from pynput.keyboard import Key, KeyCode
key_stack = []
def on_press(key):
    msg = '{0}'.format(key) 
    print(len(msg))
    for i in range(0,len(msg)):
        print(msg[i])
    print("'p'" == msg)    
    if "'\x02'" == msg:
        1/0
#    print('''msg=='\x02'''', ''''\x02''''==msg)
    print("msg=='\x02'", "'\x02'" == msg)
    print(msg)
def on_release(key):
    pass

while True:
    with keyboard.Listener(
        on_press = on_press,
        on_release = on_release) as listener:
        listener.join()
