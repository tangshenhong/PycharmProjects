#-*- coding:utf-8 -*-
# @Time  :2019/1/11 10:32
#@Author :lenmon_tang
#@Email:140@qq.com
#@File:exercise0110-03.py

#-------------------------------使用了swapcase、chr、ord、islower、isupper函数进行处理，并进行循环运行
while True:
    zfc = input('请输入要进行处理的字符串，仅可输入大小写字母：')
    zfc = zfc.swapcase()                # 使用swapcase()函数进行大小写转换
    newZfc = ''                         # 用于存放新结果的字符串
    for x in zfc:
        if x.islower():                  # x为小写字母
            newZfc += chr(219 - ord(x))  # 使用chr()及ord()函数进行镜像转换
        elif x.isupper():
            newZfc += chr(155 - ord(x))
    print(newZfc)
    conti=input('退出请按N，继续按其余任意字符：')
    if conti=='N':
        break
    else:
        pass
