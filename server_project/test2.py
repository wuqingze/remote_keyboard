#!/usr/bin/python
# -*- coding: UTF-8 -*-
import socket

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
server.bind(('0.0.0.0', 5000)) #绑定要监听的端口
server.listen(5) #开始监听 表示可以使用五个链接排队
while True:# conn就是客户端链接过来而在服务端为期生成的一个链接实例
    conn,addr = server.accept() #等待链接,多个链接的时候就会出现问题,其实返回了两个值
    data = conn.recv(32)  #接收数据
    if not data:
	break
    t = data.decode()
    print(t)
