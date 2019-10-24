'''
调用外部程序作业
'''
#-*- coding:utf-8 -*-
import os,glob
import time
filepath='F://ffmpeg-20190518-c61d16c-win64-static/bin/ffmpeg.exe'
drive='F://'

#录制视频
def transcribe():
        filename=time.strftime('%Y%m%d_%H%M%S')+'.mp4'
        result=os.system(f"{filepath} -y -rtbufsize 100M -f gdigrab -framerate 10 -draw_mouse 1 -i desktop -c:v libx264 -r 20 -crf 35 -pix_fmt yuv420p -fs 100M {drive}{filename}")
#合并视频
def combine():
    os.chdir(drive)
    #列出所有视频
    mp4pathlist=glob.glob(drive+'*.mp4')
    mp4namelist=[os.path.basename(one) for one in mp4pathlist]
    ordernum=1
    print('目录中有这些视频文件：')
    for one in mp4namelist:
        print(ordernum,'- '+one)
        ordernum+=1
    combinelist=input('请选择要合并视频的视频文件序号(格式 1,2,3,4) :').strip().split(',')
    with open(drive+'concat.txt','w') as f:
        for one in combinelist:
            f.writelines('file '+mp4namelist[int(one)-1]+'\n')
        f.close()
    os.system(f'{filepath} -f concat -i concat.txt -codec copy {drive}out.mp4')


def choiceOperation():
    while True:
        choice = input('请选择您要做的操作：1：录制视频，2：合并视频：')
        if choice == '1':
            transcribe()
            break
        elif choice == '2':
            combine()
            break
        else:
            print('输入错误，请重新输入')

choiceOperation()
