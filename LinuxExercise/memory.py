#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# @Time  :2019/5/31 14:46
import paramiko,os,time
class MemUseRate:
    def __init__(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect('192.168.86.130', 22333, 'tsh', '123')
        self.ssh=ssh
    # 从文件中获取内容，以字典返回
    def getContent(self):
        infodict = {}
        with open('/proc/meminfo', 'r') as f:
            infolist = f.readlines()
            for info in infolist:
                name, value = info.split(':')
                value = int(value.split('kB')[0].strip())
                infodict[name] = value
        return infodict
    def mainloop(self):
        infodict = self.getContent()
        # 计算内存使用率
        memtotal = infodict['MemTotal']
        memfree = infodict['MemFree']
        buffers = infodict['Buffers']
        cached = infodict['Cached']
        avaMem = '%.2f%%' % ((memfree + buffers + cached) / memtotal * 100)
        timestamp = time.strftime('%Y-%m-%d_%H:%M:%S', time.localtime())
        #追加写入ret.txt文件中
        with open('./ret.txt', 'a') as f:
            f.write(timestamp+'\t'+avaMem+'\n')

memuserate=MemUseRate()
#不断循环，退出由auto.py文件控制，通过结束时杀死进程的方式
while True:
    memuserate.mainloop()
    time.sleep(5)
memuserate.ssh.close()

