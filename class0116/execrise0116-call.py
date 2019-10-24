#-*- coding:utf-8 -*-
# @Time  :2019/1/17 13:19
#@Author :lenmon_tang
#@Email:140@qq.com
#@File:execrise0116-call.py

#打电话
number=input('请输入您要拨打的电话：')
def call(num):
    while True:
        print('您的电话已播出，与%s通话中' % num)
        print('如若需要挂断，请输入off')
        if input() == 'off':
            break

call(number)