#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket# 客户端 发送一个数据，再接收一个数据
from pynput import keyboard
from pynput.keyboard import Key, KeyCode
key_map = {
    r"'\x01'":"a",
    r"'\x02'":"b",
    r"'\x03'":"c",
    r"'\x04'":"d",
    r"'\x05'":"e",
    r"'\x06'":"f",
    r"'\x07'":"g",
    r"'\x08'":"h",
    r"'\x09'":"i",
    r"'\x0a'":"j",
    r"'\x0b'":"k",
    r"'\x0c'":"l",
    r"'\x0d'":"m",
    r"'\x0e'":"n",
    r"'\x0f'":"o",
    r"'\x10'":"p",
    r"'\x11'":"q",
    r"'\x12'":"r",
    r"'\x13'":"s",
    r"'\x14'":"t",
    r"'\x15'":"u",
    r"'\x16'":"v",
    r"'\x17'":"w",
    r"'\x18'":"x",
    r"'\x19'":"y",
    r"'\x1a'":"z",
    r"'\x1b'":"[",
    r"'\x1c'":"\\",
    r"'\x1d'":"]",
    r"'\x1e'":"^",
    r"'\x1f'":"_",
    r"'\x20'":"`",
    r"'\t'":"i",
    r"'\n'":"j",
    r"'\r'":"m",
    r"<186>":";",
    r"<222>":"'",
    r"<188>":",",
    r"<190>":".",
    r"<191>":"/",
}

def on_press(key):
    msg = "{0}".format(key)
    k = key_map.get(msg, msg) 
    stackMsg = "press:{0}".format(k)
    print(stackMsg)

def on_release(key):
    pass

while True:
    with keyboard.Listener(
        on_press = on_press,
        on_release = on_release) as listener:
        listener.join()

