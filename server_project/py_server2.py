#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket
import pynput.keyboard
from pynput.keyboard import Key, Controller
import time
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
            print("[{0} {1}] - {2}".format(threading.currentThread().getName(), time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), msg))

            if 'press:' not in msg and 'release:' not in msg:
                continue

            if 'press:' in msg and 'release:' in msg:
                continue

            if 'press:' in msg and not ( len(msg.split('press:')) == 2 and msg.startswith('press:')):
                continue

            if 'release:' in msg and not ( len(msg.split('release:')) == 2 and msg.startswith('release:')):
                continue

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

'''
TCP 协议是面向连接的、可靠的、基于字节流的传输层通信协议3，
应用层交给TCP 协议的数据并不会以消息为单位向目的主机传输，
这些数据在某些情况下会被组合成一个数据段发送给目标的主机。

Nagle 算法是一种通过减少数据包的方式提高 TCP 传输性能的算法4。
因为网络带宽有限，它不会将小的数据块直接发送到目的主机，
而是会在本地缓冲区中等待更多待发送的数据，这种批量发送数据的
策略虽然会影响实时性和网络延迟，但是能够降低网络拥堵的可能
性并减少额外开销。
'''
server.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY,True) #解决tcp沾包问题，

server.bind(('0.0.0.0',2001)) #绑定要监听的端口
server.listen(5) #开始监听 表示可以使用五个链接排队
while True:# conn就是客户端链接过来而在服务端为期生成的一个链接实例
    conn,addr = server.accept() #等待链接,多个链接的时候就会出现问题,其实返回了两个值
    print(conn,addr)
    t = threading.Thread(target=process, args=(conn,))
    t.start()

