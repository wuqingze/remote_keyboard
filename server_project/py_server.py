#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket
import pynput.keyboard


key_map = {
    'alt':Key.alt,
    'alt_l':Key.alt_l,
    'alt_r':Key.alt_r,
    'alt_gr':Key.alt_gr,
    'backspace':Key.backspace,
    'caps_lock':Key.caps_lock,
    'cmd':Key.cmd,
    'cmd_l':Key.cmd_l,
    'ctrl':Key.ctrl,
    'ctrl_l':Key.ctrl_l ,
    'delete':Key.delete,
    'down':Key.down,
    'end':Key.end,
    'enter':Key.enter,
    'esc':Key.esc,
    'f1':Key.f1,
    'f2':Key.f2,
    'f3':Key.f3,
    'f4':Key.f4,
    'f5':Key.f5,
    'f6':Key.f6,
    'f7':Key.f7,
    'f8':Key.f8,
    'f9':Key.f9,
    'f10':Key.f10,
    'f11':Key.f11,
    'f12':Key.f12,
    'f13':Key.f13,
    'f14':Key.f14,
    'f15':Key.f15,
    'f16':Key.f16,
    'f17':Key.f17,
    'f18':Key.f18,
    'f19':Key.f19,
    'f20':Key.f20,
    'home':Key.home,
    'left':Key.left,
    'page_down':Key.page_down,
    'page_up':Key.page_up,
    'right':Key.right,
    'shift':Key.shift,
    'shift_l':Key.shift_l,
    'shift_r':Key.shift_r,
    'space':Key.space,
    'tab':Key.tab,
    'up':Key.up,
    'media_play_pause':Key.media_play_pause,
    'media_volume_mute':Key.media_volume_mute,
    'media_volume_down':Key.media_volume_down,
    'media_volume_up':Key.media_volume_up,
    'media_previous':Key.media_previous,
    'media_next':Key.media_next,
    'insert':Key.insert,
    'menu':Key.menu,
    'num_lock':Key.num_lock,
    'pause':Key.pause,
    'print_screen':Key.print_screen,
    'scroll_lock':Key.scroll_lock
}

# 建立一个服务端
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('127.0.0.1',2000)) #绑定要监听的端口
server.listen(5) #开始监听 表示可以使用五个链接排队
while True:# conn就是客户端链接过来而在服务端为期生成的一个链接实例
    conn,addr = server.accept() #等待链接,多个链接的时候就会出现问题,其实返回了两个值
    print(conn,addr)
    while True:
        try:
            data = conn.recv(1024)  #接收数据
            if not data:
                break
            msg = data.decode()
            print('recive:', msg) #打印接收到的数据
            key_arg = msg.split(':')[1]
            key = key_map.get(key_arg, key_arg)
            if 'press:' in msg:
                keyboard.press(key)
            elif 'release:' in msg:
                keyboard.release(key)
            conn.send(data.upper()) #然后再发送数据
        except Error as e:
            print('关闭了正在占线的链接！')
            break
    conn.close()
