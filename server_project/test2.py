#!/usr/bin/python
# -*- coding: UTF-8 -*-
import socket

# ����һ�������
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

'''
TCP Э�����������ӵġ��ɿ��ġ������ֽ����Ĵ����ͨ��Э��3��
Ӧ�ò㽻��TCP Э������ݲ���������ϢΪ��λ��Ŀ���������䣬
��Щ������ĳЩ����»ᱻ��ϳ�һ�����ݶη��͸�Ŀ���������

Nagle �㷨��һ��ͨ���������ݰ��ķ�ʽ��� TCP �������ܵ��㷨4��
��Ϊ����������ޣ������ὫС�����ݿ�ֱ�ӷ��͵�Ŀ��������
���ǻ��ڱ��ػ������еȴ���������͵����ݣ����������������ݵ�
������Ȼ��Ӱ��ʵʱ�Ժ������ӳ٣������ܹ���������ӵ�µĿ���
�Բ����ٶ��⿪����
'''
server.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY,True) #���tcpմ�����⣬
server.bind(('0.0.0.0', 5000)) #��Ҫ�����Ķ˿�
server.listen(5) #��ʼ���� ��ʾ����ʹ����������Ŷ�
while True:# conn���ǿͻ������ӹ������ڷ����Ϊ�����ɵ�һ������ʵ��
    conn,addr = server.accept() #�ȴ�����,������ӵ�ʱ��ͻ��������,��ʵ����������ֵ
    data = conn.recv(32)  #��������
    if not data:
	break
    t = data.decode()
    print(t)
