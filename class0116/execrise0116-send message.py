#-*- coding:utf-8 -*-
# @Time  :2019/1/17 13:20
#@Author :lenmon_tang
#@Email:140@qq.com
#@File:execrise0116-send message.py

#发短信

def send():
    message = input('请输入您要发送的信息：')
    print('确定发送请按Y,取消请按N，重新输入请按R')
    choose = input()
    if choose == 'Y':
        print('信息已发送：%s' % message)
    elif choose == 'N':
        print('信息已取消发送，保存为草稿')
    elif choose == 'R':
        send()

send()
