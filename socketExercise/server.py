#-*- coding:utf-8 -*-
# @Time  :2019/5/28 9:47
import socket
addr=('127.0.0.1',2020)
s=socket.socket()
s.bind(addr)
s.listen(5)
print('服务端进入等待状态')
conn,clientaddr=s.accept()
print('服务端开始服务了')
#1024表示每次最多接受1024个字节
recv=conn.recv(1024)
print('客户端给你发送了：',str(recv,encoding='utf8'))
reply=bytes('hello too',encoding='utf8')
conn.sendall(reply)
s.close()
