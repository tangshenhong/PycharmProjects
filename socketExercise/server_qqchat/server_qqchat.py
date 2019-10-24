#-*- coding:utf-8 -*-
# @Time  :2019/5/28 11:54
import socketserver
class MySocket(socketserver.BaseRequestHandler):
    def handle(self):
        name=str(self.request.recv(1024),encoding='utf8')
        print('服务器被%s连接了'%name)
        while True:
            while True:
                try:
                    recv = str(self.request.recv(1024), encoding='utf8')
                    print('\n%s：' % name, recv)
                    if recv=='exit':break
                    say = input('\n服务器：')
                    self.request.sendall(bytes(say, encoding='utf8'))
                except:
                    break

            self.request.close()
if __name__=='__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 2019), MySocket)
    server.serve_forever()




# import socket
# sk=socket.socket()
# ip_port=('127.0.0.1',2019)
# sk.bind(ip_port)
# sk.listen(5)
# while True:
#     print('服务器空闲了...')
#     conn, clientaddr = sk.accept()
#     while True:
#         recv = str(conn.recv(1024),encoding='utf8')
#         print('client：', recv)
#         if recv == 'exit':
#             conn.close()
#             break
#         say = input('server：')
#         conn.sendall(bytes(say, encoding='utf8'))
#         if say == 'exit':
#             conn.close()
#             break
#
# sk.close()