#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket# 客户端 发送一个数据，再接收一个数据
from pynput import keyboard

#client = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #声明socket类型，同时生成链接对象
#client.connect(('127.0.0.1', 55533)) #建立一个链接，连接到本地的6969端口
def on_press(key):
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #声明socket类型，同时生成链接对象
    client.connect(('127.0.0.1', 55533)) #建立一个链接，连接到本地的6969端口
    msg = "press:{0}".format(key)
    print("on_press-----{0}".format(msg))
    client.send(msg.encode('utf-8'))  #发送一条信息 python3 只接收btye流
    data = client.recv(1024) #接收一个信息，并指定接收的大小 为1024字节
    print('recv:',data.decode()) #输出我接收的信息
    client.close()

def on_release(key):
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #声明socket类型，同时生成链接对象
    client.connect(('127.0.0.1', 55533)) #建立一个链接，连接到本地的6969端口
    msg = "release:{0}".format(key)
    print("on_release-----{0}".format(msg))
    client.send(msg.encode('utf-8'))  #发送一条信息 python3 只接收btye流
    data = client.recv(1024) #接收一个信息，并指定接收的大小 为1024字节
    print('recv:',data.decode()) #输出我接收的信息
    client.close()

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
