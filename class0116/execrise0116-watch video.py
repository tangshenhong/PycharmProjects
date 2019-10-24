#-*- coding:utf-8 -*-
# @Time  :2019/1/17 13:38
#@Author :lenmon_tang
#@Email:140@qq.com
#@File:execrise0116-watch video.py

#看视频
videos=input('请输入您要看的视频类型及名称，如“科幻 盗梦空间”：')
def watch(*videos):
    print('您要收看的视频类型及名称是：')
    for v in videos:
        print(v)
    print('确定请按Y，退出请按任意键')
    choose=input()
    if choose=='Y':
        print('即将为您播放视频......')

watch(videos)