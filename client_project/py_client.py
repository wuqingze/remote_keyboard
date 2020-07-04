#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket# 客户端 发送一个数据，再接收一个数据
import os
from pynput import keyboard

key_stack = []

lock = True
special_key = [
 'Key.alt',
 'Key.alt_l',
 'Key.alt_r',
 'Key.alt_gr',
 'Key.cmd',
 'Key.cmd_l',
 'Key.ctrl',
 'Key.ctrl_l',
 'Key.esc',
 'Key.home',
 'Key.left',
 'Key.right',
 'Key.shift',
 'Key.shift_l',
 'Key.shift_r',
 'Key.space',
 'Key.tab',
]

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
    r"'\x1c'":r"\t"[0],
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
    r"<65>":"a",
    r"<66>":"b",
    r"<67>":"c",
    r"<68>":"d",
    r"<69>":"e",
    r"<70>":"f",
    r"<71>":"g",
    r"<72>":"h",
    r"<73>":"i",
    r"<74>":"j",
    r"<75>":"k",
    r"<76>":"l",
    r"<77>":"m",
    r"<78>":"n",
    r"<79>":"o",
    r"<80>":"p",
    r"<81>":"q",
    r"<82>":"r",
    r"<83>":"s",
    r"<84>":"t",
    r"<85>":"u",
    r"<86>":"v",
    r"<87>":"w",
    r"<88>":"x",
    r"<89>":"y",
    r"<90>":"z",
    r"'{'":"[",
    r"'|'":r"\t"[0],
    r"'}'":"]",
    r"':'":";",
    '\'"\'':"'",
    r"'<'":",",
    r"'>'":".",
    r"'?'":"/",
    r"'_'":"-",
    r"'+'":"="
}

def release_all_special_key():
    for key in special_key:
        client = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #声明socket类型，同时生成链接对象
        client.connect(('127.0.0.1', 55533)) #建立一个链接，连接到本地的6969端口
        msg = 'release:'+key
        client.send(msg.encode('utf-8'))  #发送一条信息 python3 只接收btye流
        data = client.recv(1024) #接收一个信息，并指定接收的大小 为1024字节
        client.close()

def getkey(key):
#目的是将引号给去掉
    t = "{0}".format(key)
    result = ''
    if None == key_map.get(t,None):
        if "'" == t[0] or '"' == t[0]:
            result = t[1:-1]
        else:
            result = t
    else:
        result = key_map.get(t)
    return result

def on_press(key):
    global lock
    t = getkey(key)
    key_stack.append(t)
    if len(key_stack) > 1:
        if key_stack[-1] == 'q'  and key_stack[-2] == 'Key.ctrl_l':
            1/0
        elif key_stack[-1] == '.'  and key_stack[-2] == 'Key.ctrl_l':
            lock = not lock
            if lock:
                print("keyboard lock...")
            else:
                print("remote keyboard connected...")
            release_all_special_key()
            return
    if lock:
        return
    msg = "press:{0}".format(t)
    print("on_press-----{0}".format(msg))
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #声明socket类型，同时生成链接对象
    client.connect(('127.0.0.1', 55533)) #建立一个链接，连接到本地的6969端口
    client.send(msg.encode('utf-8'))  #发送一条信息 python3 只接收btye流
    #data = client.recv(1024) #接收一个信息，并指定接收的大小 为1024字节
    #print('recv:',data.decode()) #输出我接收的信息
    client.close()
    key_stack.append('{0}'.format(key))

def on_release(key):
    global lock 
    if lock:
        return
    t = getkey(key)
    msg = "release:{0}".format(t)
    print("on_release-----{0}".format(msg))
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #声明socket类型，同时生成链接对象
    client.connect(('127.0.0.1', 55533)) #建立一个链接，连接到本地的6969端口
    client.send(msg.encode('utf-8'))  #发送一条信息 python3 只接收btye流
    #data = client.recv(1024) #接收一个信息，并指定接收的大小 为1024字节
    #print('recv:',data.decode()) #输出我接收的信息
    client.close()

while True:
    with keyboard.Listener(
        on_press = on_press,
        on_release = on_release) as listener:
        listener.join()
print("wait inpuputt...")
