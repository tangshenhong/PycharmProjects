#-*- coding:utf-8 -*-
# @Time  :2019/1/16 13:12
#@Author :lenmon_tang
#@Email:140@qq.com
#@File:execrise0115-01.py

#使用双层for循环打印九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print('%d*%d=%d '%(j,i,i*j),end='')
    print()