#-*- coding:utf-8 -*-
# @Time  :2019/5/28 10:38
import socket,os
def postfile(sk,filepath):
    sk.connect(('127.0.0.1',2019))
    filesize=os.stat(filepath).st_size
    #发送文件长度
    sk.sendall(bytes(str(filesize),encoding='utf8'))
    sk.recv(1024)# 避免粘包

    #发送文件名称
    filename=os.path.split(filepath)[1]
    sk.sendall(bytes(filename,encoding='utf8'))
    sk.recv(1024)  # 避免粘包

    #发送文件
    with open(filepath,'rb') as f:
        while filesize>0:
            sk.sendall(f.read(1024))
            filesize-=1024
    sk.close()


sk=socket.socket()
postfile(sk,'./timg.bmp')

