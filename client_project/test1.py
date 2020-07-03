#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket# 客户端 发送一个数据，再接收一个数据
from pynput import keyboard
from pynput.keyboard import Key, KeyCode
key_stack = []
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
    r"'\x1c'":r"\r"[0],
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
        result = key_map.get(key)
    return result

#client = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #声明socket类型，同时生成链接对象
#client.connect(('127.0.0.1', 55533)) #建立一个链接，连接到本地的6969端口
def on_press(key):
    t = getkey("{0}".format(key))
    if 'q' == t:
        1/0
    msg = "press:{0}".format(t)
    print(msg)
    #print("on_press-----{0}".format(msg))
    #if isinstance(key, KeyCode):
    #    print("--------type KeyCode")
    #    if key.char == None or key.char == '':
    #        print("--------"+char.value)
    #    else:
    #        print("--------"+key.char.lower())
    #elif isinstance(key, Key):
    #    print("--------type Key")
    #    print("---------"+str(key.value))
    #key_stack.append('{0}'.format(key))
#    key_stack.append(str(key).replace('\'', ''))
#    if len(key_stack) > 2:
#        print(key_stack[-1],key_stack[-2],key_stack[-3])
#        print("----------")
#        print("stack[-1] == \x17", key_stack[-1] == '\x17')
#        print("stack[-2] == key.shift", key_stack[-2] == 'Key.shift')
#        print("stack[-3] == key.ctrl_l", key_stack[-3] == 'Key.ctrl_l')
#    if len(key_stack)>2 and key_stack[-1] == '\x17' and key_stack[-2] == 'Key.shift' and key_stack[-3] == 'Key.ctrl_l':
#        exit()

def on_release(key):
    pass

while True:
    with keyboard.Listener(
        on_press = on_press,
        on_release = on_release) as listener:
        listener.join()

#while True:
#    # addr = client.accept()
#    # print '连接地址：', addr
#    for i in range(10):
#        client = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #声明socket类型，同时生成链接对象
#        client.connect(('127.0.0.1', 55533)) #建立一个链接，连接到本地的6969端口
#        msg = '欢迎访问菜鸟教程！'  #strip默认取出字符串的头尾空格
#        print('-------before send')
#        client.send(msg.encode('utf-8'))  #发送一条信息 python3 只接收btye流
#        data = client.recv(1024) #接收一个信息，并指定接收的大小 为1024字节
#        print('recv:',data.decode()) #输出我接收的信息
#        client.close() #关闭这个链接
