# -*- coding: utf-8 -*-
# @Time  : 2019/1/10 21:38
# @Author: yu
# @Email : 15010020441@163.com
# @File  : homework.py

# 第一种解法：
L='sdSdsfdAdsdsdfsfdsdASDSDFDSFa'
a='abcdefghijklmnopqrstuvwxyz'
b='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
new_L=''
for i in L:
    if i in a:
       a1=a.find(i)
       a2=a[25-a1]
       new_L+=a2
    elif i in b:
       b1=b.find(i)
       b2=b[25-b1]
       new_L+=b2
print(new_L.swapcase())

# 第二种解法：
L='sdSdsfdAdsdsdfsfdsdASDSDFDSFa'
a='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMVOPQRSTUVWXYZ'
b='zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA'
trantab=str.maketrans(a,b)
new_L=L.translate(trantab)
print(new_L.swapcase())