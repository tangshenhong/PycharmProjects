'''
多线程作业
'''
import threading,requests
r=threading.Lock()
#全局变量，用于存储获取的网页内容
content=''
def getUrlText(url):
    global content
    resp = requests.get(url)
    print(url+'\n',resp.text)
    r.acquire()
    #将获取到的内容累加存放到content字符串中
    content+=resp.text+'\n'
    print(resp.text)
    r.release()
#创建两个线程
t1=threading.Thread(target=getUrlText,args=('http://mirrors.163.com/centos/6/isos/x86_64/README.txt',))
t1.start()
t2=threading.Thread(target=getUrlText,args=('http://mirrors.163.com/centos/7/isos/x86_64/0_README.txt',))
t2.start()
t1.join()
t2.join()
#主线程等待这个两个子线程获取到信息后，将其内容依次合并后存入名为 readme89.TXT 的文件中
with open('readme89.TXT','a') as f:
    f.writelines(content)
    f.close()