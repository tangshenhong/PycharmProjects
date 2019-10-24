#------------------------登录获取积分，1-10，概率验证
import requests
import time
def loginTest(username,password):
    head={
        "Host":"localhost:38850",
        "Content-Type":"application/json; charset=utf-8"
    }
    datas={
        "username":"%s"%username,
        "password": "%s"%password,
        "Verifycode": "1234",
        "VerifycodeRandom": "1234"
    }
    loginResponse=requests.post('http://localhost:38850/HXHome/LoginTest', headers=head, json=datas)
    return loginResponse.json()
starttime=time.time()
num=101

total=[[],[],[],[],[],[],[],[],[],[]]
for one in range(1,num):
    if loginTest('林伟强','123456')['Message']=='登录成功':
        continue
    integral=loginTest('林伟强','123456')['Message'].split('赠送')[-1].split('海西币')[0]
    for x in range(1,11):
        if int(integral)==x:
            total[x-1].append(int(integral))
endtime=time.time()
print('耗时：',(endtime-starttime),'s')

print(f'总共运行了:{num-1}次')
for one in range(1,11):
    per=float('%.2f' % float((len(total[one-1]) / (num-1))*100))
    print(f'{one}  的次数为：{len(total[one-1])}     {per}%')

