#-*- coding:utf-8 -*-
# @Time  :2019/5/28 9:47
import socket
s=socket.socket()
s.connect(('127.0.0.1',2020))
send=bytes('hello',encoding='utf8')
s.sendall(send)
recv=s.recv(1024)
print('服务端给你发送了：',str(recv,encoding='utf8'))
s.close()