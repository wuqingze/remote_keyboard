#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket# 客户端 发送一个数据，再接收一个数据
from pynput.keyboard import Key, KeyCode, Controller
import time
time.sleep(4)
keyboard = Controller()
kv1 = KeyCode.from_vk(0x17)
#keyboard.press(kv1)
#keyboard.release(kv1)

#keyboard.press(Key.ctrl)
#keyboard.press('w')
#keyboard.release(Key.ctrl)
#keyboard.release('w')

keyboard.press(Key.ctrl)
keyboard.press(kv1)
keyboard.release(Key.ctrl)
keyboard.release(kv1)

