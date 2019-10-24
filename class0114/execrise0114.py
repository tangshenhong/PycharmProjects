#-*- coding:utf-8 -*-
# @Time  :2019/1/15 9:12
#@Author :lenmon_tang
#@Email:140@qq.com
#@File:execrise0114.py

#写一个餐厅菜单显示程序，根据不同的菜系分成顶级菜单：湘菜、粤菜等
#根据肉食、蔬菜、特色菜分为二级菜单，
# 根据每个选项里面的各个菜式分为三级菜单，可以根据你输入的菜系、菜类、菜式可以选择进入各子菜单，查看菜式，也可以选择退出菜单。
L1=['1.湘菜','2.粤菜']
L2=['1.肉菜','2.蔬菜','3.特色菜']
L3=[[['1.麻辣仔鸡','2.炒血鸭'],['1.板栗烧菜心','2.油辣莴笋'],['1.南瓜饼','2.上汤鱼生']],[['1.脆皮炸鸡','2.盐焗鸡'],['1.烟筒白菜','2.蚝油生菜'],['1.白切鸡','2.明炉烤乳猪']]]
num=[]
#while True:
panduan1=True
panduan2 = True
while panduan1:
    print('步骤一、请输入菜系号选择菜系：%s' % L1)
    caixi = input()
    while panduan2:
        for x in range(1, len(L3) + 1):
            if caixi == str(x):
                num.append(x - 1)
                print('\n步骤二、请输入菜类号选择菜类：%s' % L2)
                print('返回上一级请输入back')
                cailei = input()
                if cailei == 'back':
                    panduan2=False
                    break
                for y in range(1, len(L3[x - 1]) + 1):
                    if cailei == str(y):
                        num.append((y - 1))
                        print('步骤三、请输入菜式号选择菜式:%s' % L3[x - 1][y - 1])
                        caishi = int(input())
                        print('您选择了%s_%s_%s' % (
                        L1[num[0]], L2[num[1]], L3[x - 1][y - 1][caishi - 1]) + '退出请按Y\t重新开始请按N\t返回上一级请按back\n')
                        choose=input()
                        if choose == 'back':
                            break
                        elif choose=='N':
                            panduan2=False
                            break
                        elif choose=='Y':
                            panduan2=False
                            panduan1=False
                            break











