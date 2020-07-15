#!/usr/bin/python
# -*- coding: UTF-8 -*-
udp_ip = '0.0.0.0'
udp_port = 5000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((udp_ip, udp_port))

while True:
    data, addr = sock.recvfrom(32)
    print("received message: %s" % data)
