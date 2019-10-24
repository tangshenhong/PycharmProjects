#-*- coding:utf-8 -*-
# @Time  :2019/5/28 10:38
import socket
def getfile(conn):
    #接收文件长度
    filesize=int(str(conn.recv(1024),encoding='utf8'))
    conn.sendall(bytes('ok',encoding='utf8'))#避免粘包
    #接收文件名称
    filename=str(conn.recv(1024),encoding='utf8')
    conn.sendall(bytes('ok', encoding='utf8'))  # 避免粘包
    #接收文件
    with open('./%s'%filename,'wb') as f:
        while filesize>0:
            f.write(conn.recv(1024))
            filesize-=1024
    conn.close()

sk=socket.socket()
sk.bind(('127.0.0.1',2019))
sk.listen(5)
conn,clientaddr=sk.accept()
getfile(conn)
sk.close()