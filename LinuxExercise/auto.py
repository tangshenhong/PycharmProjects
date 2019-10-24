#-*- coding:utf-8 -*-
# @Time  :2019/5/31 16:13
import paramiko,time
#连接linux
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh.connect('192.168.86.130', 22333, 'tsh', '123')
#查看是否存在姓名文件夹，不存在则新建
name='tangshenhong'
stdin, stdout, stderr=ssh.exec_command('find %s'%name)
reply=str(stdout.read(),encoding='utf8')
if not reply:
    stdin, stdout, stderr = ssh.exec_command('mkdir %s'%name)
#将memory.py拷贝到远程主机上
sftp=ssh.open_sftp()
sftp.put('./memory.py','%s/memory.py'%name)
#运行memory.py
ssh.exec_command('chmod +x %s/memory.py'%name)
ssh.exec_command('python %s/memory.py'%name)
#等待5分钟
time.sleep(30)
#为防止memory.py不断运行，结束时杀死进程
stdin,stdout,stderr=ssh.exec_command('pgrep python')
pid=str(stdout.read(),encoding='utf8')
ssh.exec_command('kill -9 %s'%pid)
#将结果文件ret.txt拷贝回本地
sftp.get('./ret.txt','./ret.txt')
#删除linux上的结果文件
ssh.exec_command('rm %s/memory.py'%name)
ssh.exec_command('rm ret.txt')
sftp.close()
ssh.close()
