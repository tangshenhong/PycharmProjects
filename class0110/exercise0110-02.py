#-*- coding:utf-8 -*-
# @Time  :2019/1/11 10:00
#@Author :lenmon_tang
#@Email:140@qq.com
#@File:exercise0110-02.py

#-------------------------------使用了replace、chr、ord、islower、isupper函数；切片、拼接字符串等方法进行处理
zfc='sdSdsfdAdsdsdfsfdsdASDSDFDSFa'
for i,x in enumerate(zfc):
    if x.islower():                          # x为小写字母
        x1=chr(155-ord(x.upper()))           #先将x转换为大写字母后，使用chr、ord函数进行镜像处理
        zfc=zfc[:i]+zfc[i:].replace(x,x1,1)  #使用切片、replace函数、字符拼接方式进行处理
    elif x.isupper():
        x2=chr(219-ord(x.lower()))
        zfc=zfc[:i]+zfc[i:].replace(x,x2,1)
print(zfc)

