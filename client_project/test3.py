#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket# 客户端 发送一个数据，再接收一个数据
from pynput.keyboard import Key, KeyCode, Controller
import time
keyboard = Controller()

#keyboard.press(Key.caps_lock)
#time.sleep(14)
#keyboard.release(Key.caps_lock)

keyboard.press(Key.caps_lock)
keyboard.release(Key.caps_lock)
time.sleep(10)
keyboard.press(Key.caps_lock)
keyboard.release(Key.caps_lock)

