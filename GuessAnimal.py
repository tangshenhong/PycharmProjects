'''
使用线程方式玩游戏（可避免等待输入时，计时暂停，导致计时不够准确的问题）
线程1：计时器
线程2：游戏主体
'''
from random import randint
import time,threading
class Tiger:
    name='Tiger'
    def __init__(self):
        self.weight=200
    def roar(self):
        print('WOW!')
        self.weight-=5
    def feed(self,food):
        if food=='meat':
            print('恭喜，喂对了，体重+10')
            self.weight+=10
        else:
            print('啊哦，喂错了，体重-10')
            self.weight-=10

class Sheep:
    name='Sheep'
    def __init__(self):
        self.weight=100
    def roar(self):
        print('mie~')
        self.weight-=5
    def feed(self,food):
        if food=='grass':
            print('恭喜，喂对了，体重+10')
            self.weight+=10
        else:
            print('啊哦，喂错了，体重-10')
            self.weight-=10

class Room:
    def __init__(self,num,animal):
        self.num=num
        self.animal=animal
#将游戏结束标识、房间信息列表设置为全局变量
gameover=True
roomList = []
#计时
def timekeeping():
    global  gameover
    time.sleep(20)
    gameover=False
    print()
    for num, one in enumerate(roomList):
        print('房间{}：{},体重{}'.format(num + 1, one.animal.name, one.animal.weight))
#玩游戏
def playgame():
    global roomList
    for num in range(0, 10):
        if randint(0, 1):
            room = Room(num, Tiger())
        else:
            room = Room(num, Sheep())
        roomList.append(room)
    while gameover:
        roomNum = randint(0, 9)
        print('-----------------')
        knock = input('现在访问的是{}号房间，要敲门吗？y/n：  '.format(roomNum + 1))
        if knock == 'y':
            roomList[roomNum].animal.roar()
        food = input('请输入要给动物喂食的食物：')
        roomList[roomNum].animal.feed(food)

#将计时和玩游戏分设为两个线程，互不影响
t1 = threading.Thread(target=timekeeping)
t1.start()
t2=threading.Thread(target=playgame)
#将t2设置为守护线程，即主线程结束时，强制结束t2（主线程指整个程序主体，主线程会等所有线程结束后才结束，此时由于t2是守护线程，因此主线程等t1结束后即结束，此时t2被强制结束）
t2.setDaemon(True)
t2.start()



