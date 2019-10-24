#-*- coding:utf-8 -*-
# @Time  :2019/1/11 9:30
#@Author :lenmon_tang
#@Email:140@qq.com
#@File:exercise0110-01.py

#-----------------------------------使用了find、切片、字符串拼接等方法进行处理
zfc='sdSdsfdAdsdsdfsfdsdASDSDFDSFa'
small_letter='abcdefghijklmnopqrstuvwxyz'
big_letter='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i,x in enumerate(zfc):          #对原始字符串进行循环
    index1=small_letter.find(x)     #返回x在26个小写字母中的下标
    index2=big_letter.find(x)       #返回x在26个大写字母中的下标
    if index1!=-1:                  #如果index1!=-1，则x为小写字母
        x=small_letter[-(index1+1)] #先对x进行镜像处理
        zfc=zfc[:i]+x.upper()+zfc[(i+1):]   #将x进行大写处理后，拼接切片后的字符串
    elif index2!=-1:
        x = big_letter[-(index2 + 1)]
        zfc = zfc[:i] +x.lower() + zfc[(i + 1):]
print(zfc)
