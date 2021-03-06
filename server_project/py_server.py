#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket
import pynput.keyboard
from pynput.keyboard import Key, Controller
import threading

key_map = {
    'Key.alt':Key.alt,
    'Key.alt_l':Key.alt_l,
    'Key.alt_r':Key.alt_r,
    'Key.alt_gr':Key.alt_gr,
    'Key.backspace':Key.backspace,
    'Key.caps_lock':Key.caps_lock,
    'Key.cmd':Key.cmd,
    'Key.cmd_l':Key.cmd_l,
    'Key.ctrl':Key.ctrl,
    'Key.ctrl_l':Key.ctrl_l ,
    'Key.delete':Key.delete,
    'Key.down':Key.down,
    'Key.end':Key.end,
    'Key.enter':Key.enter,
    'Key.esc':Key.esc,
    'Key.f1':Key.f1,
    'Key.f2':Key.f2,
    'Key.f3':Key.f3,
    'Key.f4':Key.f4,
    'Key.f5':Key.f5,
    'Key.f6':Key.f6,
    'Key.f7':Key.f7,
    'Key.f8':Key.f8,
    'Key.f9':Key.f9,
    'Key.f10':Key.f10,
    'Key.f11':Key.f11,
    'Key.f12':Key.f12,
    'Key.f13':Key.f13,
    'Key.f14':Key.f14,
    'Key.f15':Key.f15,
    'Key.f16':Key.f16,
    'Key.f17':Key.f17,
    'Key.f18':Key.f18,
    'Key.f19':Key.f19,
    'Key.f20':Key.f20,
    'Key.home':Key.home,
    'Key.left':Key.left,
    'Key.page_down':Key.page_down,
    'Key.page_up':Key.page_up,
    'Key.right':Key.right,
    'Key.shift':Key.shift,
    'Key.shift_l':Key.shift_l,
    'Key.shift_r':Key.shift_r,
    'Key.space':Key.space,
    'Key.tab':Key.tab,
    'Key.up':Key.up,
    'Key.media_play_pause':Key.media_play_pause,
    'Key.media_volume_mute':Key.media_volume_mute,
    'Key.media_volume_down':Key.media_volume_down,
    'Key.media_volume_up':Key.media_volume_up,
    'Key.media_previous':Key.media_previous,
    'Key.media_next':Key.media_next,
    'Key.insert':Key.insert,
    'Key.menu':Key.menu,
    'Key.num_lock':Key.num_lock,
    'Key.pause':Key.pause,
    'Key.print_screen':Key.print_screen,
    'Key.scroll_lock':Key.scroll_lock,
    '\\\\':'\\'
}

def process(conn):
    while True:
        try:
            data = conn.recv(32)  #接收数据
            if not data:
                break
            t = data.decode()
            msg = ''
            for i in range(0, len(t)):
                if '\x00' != t[i]:
                    msg += t[i]
                else:
                    break
            if len(msg) == 0:
                continue
            print('recive:', msg) #打印接收到的数据
            if 'press:' in msg:
                key = msg.split("press:")[1]
                key = key_map.get(key, key)
                keyboard.press(key)
            elif 'release:' in msg:
                key = msg.split("release:")[1]
                key = key_map.get(key, key)
                keyboard.release(key)
            conn.send(data.upper()) #然后再发送数据
        except Error as e:
            print('关闭了正在占线的链接！')
    conn.close()

keyboard = Controller()
# 建立一个服务端
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('127.0.0.1',2000)) #绑定要监听的端口
server.listen(5) #开始监听 表示可以使用五个链接排队
while True:# conn就是客户端链接过来而在服务端为期生成的一个链接实例
    conn,addr = server.accept() #等待链接,多个链接的时候就会出现问题,其实返回了两个值
    print(conn,addr)
    t = threading.Thread(target=process, args=(conn,))
    t.start()

