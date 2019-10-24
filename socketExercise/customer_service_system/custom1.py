#-*- coding:utf-8 -*-
# @Time  :2019/5/28 17:31
# coding=utf-8
from socket import *
addr=('',0)
buffersize=1024
class ConnectionHandle:
    LEN_LEN=4
    LEN_LEN_TYPE=7

    @staticmethod
    def encode(type,sendmsg):
        len='{:04}'.format(len(sendmsg)+ConnectionHandle.LEN_LEN_TYPE).encode()
        type=type.encode()
        msgbody=sendmsg.encode()
        return b'|'.join([len,type,msgbody])
    @staticmethod
    def decode(msg):
        msg=str(msg,encoding='utf8')
        type=int(msg[5,6])
        msgbody=msg[ConnectionHandle.LEN_LEN_TYPE:]
        return type,msgbody

    def readmsg(self):
        msg=self.sk.recv(buffersize)
        if msg:
            return self.decode(msg)

    def sendmsg(self,type,reply):
        sendmsg=self.encode(type,reply)
        self.sk.sendall(sendmsg)

    def handlemsg(self,type,msgbody):
        if type==1:
            self.username=msgbody
            print('连接的用户名称是：',msgbody)
        elif type==2:
            print(f'{self.username}：',msgbody)
            reply=input('>>')
            self.sendmsg(type,reply)

    def mainloop(self):
        while True:
            type,msgbody=self.readmsg()
            self.handlemsg(type,msgbody)

sk=socket.socket()
sk.bind(addr)
sk.listen(5)
print('等待连接：')
conn,addr=sk.accept()
handler=ConnectionHandle(sk)
handler.mainloop()
sk.close()

