#-*- coding:utf-8 -*-
# @Time  :2019/1/16 13:13
#@Author :lenmon_tang
#@Email:140@qq.com
#@File:execrise0115-02.py

#使用双层while循环打印九九乘法表
i=1
while i<10:
    j=1
    while j<=i:
        print('%d*%d=%d ' % (j, i, j * i), end='')
        j+=1
    print()
    i+=1