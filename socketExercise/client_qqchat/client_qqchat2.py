#-*- coding:utf-8 -*-
# @Time  :2019/5/28 14:29
import socket
sk=socket.socket()
ip_port=('127.0.0.1',2019)
sk.connect(ip_port)
name='chat2'
print('%s启动了'%name)
#向服务器发送请求者姓名
sk.sendall(bytes(name,encoding='utf8'))
while True:
    say = input('%s：'%name)
    sk.sendall(bytes(say, encoding='utf8'))
    if say=='exit':break
    resp = str(sk.recv(1024),encoding='utf8')
    print('server:', resp)
    if resp=='exit':break
sk.close()